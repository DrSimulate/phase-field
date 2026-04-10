import numpy as np
np.random.seed(0)
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation, FFMpegWriter

# Set plot style
import plot_config
smooth = True
if smooth:
    interpolation = 'bicubic'
else:
    interpolation = 'nearest'

# Parameters
eps = 0.02
M = 1.0
Lx = 1.0
Nx, Ny = 200, 200
dx = Lx / Nx
dy = dx
Ly = Ny * dy
dt = 0.01 * 0.2 * dx**2 / M
steps = 2000  # total time steps
kx = 2*np.pi * np.fft.fftfreq(Nx, d=dx)
ky = 2*np.pi * np.fft.fftfreq(Ny, d=dy)
KX, KY = np.meshgrid(kx, ky, indexing='ij')
K2 = KX**2 + KY**2
K4 = K2**2
denom = 1 + dt * M * K4

# 2D grid
x = np.linspace(0, Lx, Nx, endpoint=False)
y = np.linspace(0, Ly, Ny, endpoint=False)
X, Y = np.meshgrid(x, y, indexing='ij')

# Initial condition
p = np.ones((Nx, Ny))
p[:Nx//4, :] = -1
p[-Nx//4:, :] = -1
p[:, :Ny//4] = -1
p[:, -Ny//4:] = -1

# Animation setup
fig, ax = plt.subplots(dpi=200)
im = ax.imshow(p, cmap=plot_config.cmap_CH, origin='lower', extent=[0, Lx, 0, Ly], vmin=-1, vmax=1, interpolation=interpolation)
cbar = plt.colorbar(im, ax=ax)
cbar.set_label("$p(x_1,x_2)$")
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")

steps_per_frame = 10
frames = steps // steps_per_frame

def update(frame):
    if frame > 0:
        for _ in range(steps_per_frame):
            p_hat = np.fft.fft2(p)
            nonlinear = p**3 - p
            nonlinear_hat = np.fft.fft2(nonlinear)
            p_hat_new = (p_hat - dt * M * K2 * (1/eps**2) * nonlinear_hat) / denom
            p[:] = np.real(np.fft.ifft2(p_hat_new))
    
    t = frame * steps_per_frame * dt
    E = np.sum(0.25*(p**2-1)**2/eps**2 + 0.5*((np.roll(p,-1,axis=0)-np.roll(p,1,axis=0))/(2*dx))**2 + 
               0.5*((np.roll(p,-1,axis=1)-np.roll(p,1,axis=1))/(2*dy))**2) * dx * dy
    ax.set_title(f"$t = {t:.6f}$ \n$E = {E:.6f}$", loc="left")
    im.set_data(p)
    return im,

anim = FuncAnimation(fig, update, frames=frames, blit=True)
writer = FFMpegWriter(fps=20, bitrate=1800)
anim.save("media/videos/Cahn_Hilliard_2D_square.mp4", writer=writer)
print("Animation saved as media/videos/Cahn_Hilliard_2D_square.mp4")