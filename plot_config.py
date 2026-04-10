import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

sns.set_theme(style="dark")
plt.style.use("dark_background")

mygreen = "#66FF00"
myorange ="#FFC300"
myturquoise = "#00FFFF"

# default colormap
cmap_AC = "RdYlBu" # for Allen-Cahn
cmap_CH = "GnBu" # for Cahn-Hilliard

cmaporange = mcolors.LinearSegmentedColormap.from_list(
    "white_to_orange",
    ["white", myorange]
)
cmapturquoise = mcolors.LinearSegmentedColormap.from_list(
    "white_to_turquoise",
    ["white", myturquoise]
)
