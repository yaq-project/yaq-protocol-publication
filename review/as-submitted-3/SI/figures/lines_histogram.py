import numpy as np
import pandas as pd
import pathlib
import matplotlib.pyplot as plt

__here__ = pathlib.Path(__file__).parent

data = pd.read_table(__here__ / "lines_histogram.txt")

bins = np.arange(0, 351, 10)

data["code"].hist(bins=bins)

fig = plt.gcf()
fig.set_size_inches(3.5, 2.5)
ax = plt.gca()
ax.set_xlabel("Lines of Code")
ax.set_ylabel("Number of Daemons")
ax.set_yticks(np.arange(9))
ax.set_xticks(np.arange(0, 352, 50))
ax.set_xlim(0, 350)

plt.savefig("lines_histogram.png", dpi=300, bbox_inches="tight")
