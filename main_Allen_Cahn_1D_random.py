import numpy as np
np.random.seed(0)
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation, FFMpegWriter

import plot_config

# Parameters
eps = 0.02
M = 1.0
L = 1.0
N = 200
dx = L / N
x = np.linspace(0, L, N, endpoint=False)
dt = 0.2 * dx**2 / M
steps = 1000  # total number of time steps to simulate

# Initial condition
t = 0.0
p = np.random.uniform(-1, 1, N)

# Animation setup
fig, ax = plt.subplots(dpi=200)
line, = ax.plot(x, p, color="white", linewidth=2)
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-1.1, 1.1)
ax.set_xlabel("$x$")
ax.set_ylabel("$p(x)$")
ax.minorticks_on()
ax.grid(which="major", linestyle="--", linewidth=0.3)
ax.grid(which="minor", linestyle="--", linewidth=0.3)
steps_per_frame = 1  # number of time steps to compute per animation frame
frames = steps // steps_per_frame # total number of animation frames

def update(frame):
    if frame > 0:
        for _ in range(steps_per_frame):
            laplacian = (np.roll(p,-1) - 2*p + np.roll(p,1)) / dx**2
            potential = p**3 - p
            p[:] = p + dt * M * (- (1/eps**2) * potential + laplacian)
            # print("p updated")
    t = frame * steps_per_frame * dt
    # print("t=", t)
    E = np.sum(0.25*(p**2-1)**2/eps**2 + 0.5*((np.roll(p,-1)-np.roll(p,1))/(2*dx))**2)*dx
    ax.set_title(f"$t = {t:.6f}$ \n$E = {E:.6f}$", loc="left")
    line.set_ydata(p)
    return line,

anim = FuncAnimation(fig, update, frames=frames, blit=True)
writer = FFMpegWriter(fps=20, bitrate=1800)
anim.save("media/videos/Allen_Cahn_1D_random.mp4", writer=writer)
print("Animation saved as media/videos/Allen_Cahn_1D_random.mp4")
