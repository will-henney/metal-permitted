from __future__ import print_function
import sys
import numpy as np
import pyneb as pn
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

fe3 = pn.Atom('Fe', 3)

Ts = np.linspace(4000, 20000, 100)
Ds = 10**np.linspace(1.0, 5.0, 200)

def ratio_4702_4658(tem, den):
    em4702 = fe3.getEmissivity(tem, den, wave=4701.53)
    em4658 = fe3.getEmissivity(tem, den, wave=4658.05)
    return em4702/em4658


figfile = sys.argv[0].replace('.py', '.pdf')

ratios = ratio_4702_4658(Ts, Ds)
levels = np.linspace(0.24, 0.40, 17)
fig, ax = plt.subplots(figsize=(6, 6))

Ts = Ts[:, None]*np.ones_like(ratios)
Ds = Ds[None, :]*np.ones_like(ratios)

#ax.contour(Ts, Ds, Ds, levels=[100, 10000, 1e6], cmap='magma_r')
c = ax.contour(Ds, Ts, ratios,
               levels=levels,
               cmap='tab20b_r', linewidths=3)
# ax.clabel(c, levels[1::2], fontsize='x-small',
#           inline=False, rightside_up=True, use_clabeltext=True)
cb = fig.colorbar(c, orientation='horizontal')
cb.set_label("[Fe III] 4702 / 4658")

ax.set(
    ylabel="Temperature, K",
    xlabel="Density, cm$^{-3}$",
    xscale='log',
)
sns.despine()
fig.tight_layout()
fig.savefig(figfile)
print(figfile, end='')
