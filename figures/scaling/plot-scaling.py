import pathlib

import pandas as pd
import matplotlib.pyplot as plt

__here__ = pathlib.Path(__file__).parent

data = pd.read_csv(__here__ / "scaling.csv")

fig, ax = plt.subplots()

ax.errorbar(data["npts"], data["mean"], yerr=data["stdev"], marker="o", lw=0, elinewidth=2, capsize=3, capthick=2, zorder=3)
ax.grid()
ax.set_xscale("log", base=2)
ax.set_yscale("log")

ax.set_xlabel("Number of Pixels")
ax.set_ylabel("Time (seconds)")

for pt in data.itertuples():
    if pt.shapex != 1:
        ax.errorbar([pt.npts], [pt.mean], yerr=[pt.stdev], marker="o", lw=0, elinewidth=2, capsize=3, capthick=2, zorder=3.1)
        ax.annotate(
            str((pt.shapex, pt.shapey)),
            (pt.npts, pt.mean),
            xytext=(-80, 10),
            textcoords="offset points",
            arrowprops=dict(arrowstyle="->"),
        )

plt.show()
#fig.savefig("scaling.png", dpi=300)
