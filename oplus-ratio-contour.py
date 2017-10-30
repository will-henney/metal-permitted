from __future__ import print_function
import sys
import numpy as np
import pyneb as pn
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

o1r = pn.RecAtom('O', 1, case='A')
o2c = pn.Atom('O', 2)

Ts = np.linspace(4000, 20000, 300)
Ds = 10**np.linspace(1.0, 9.0, 200)

def ratio_7773_7330(tem, den):
    em7330 = o2c.getEmissivity(tem, den, wave=7330.73)
    em7330 += o2c.getEmissivity(tem, den, wave=7329.66)
    em7773 = o1r.getEmissivity(tem, den, label='7773+')
    return em7773/em7330


figfile = sys.argv[0].replace('.py', '.pdf')

ratios = ratio_7773_7330(Ts, Ds)
levels = [3.0, 1.0, 0.3, 0.1, 0.03, 0.01, 0.003, 0.001, 0.0003]
fig, ax = plt.subplots(figsize=(6, 6))

Ts = Ts[:, None]*np.ones_like(ratios)
Ds = Ds[None, :]*np.ones_like(ratios)

#ax.contour(Ts, Ds, Ds, levels=[100, 10000, 1e6], cmap='magma_r')
c = ax.contour(Ds, Ts, ratios,
               levels=levels[::-1],
               cmap='tab20b_r', linewidths=3,
               norm=mpl.colors.LogNorm())
# ax.clabel(c, levels[1::2], fontsize='x-small',
#           inline=False, rightside_up=True, use_clabeltext=True)
cb = fig.colorbar(c, orientation='horizontal')
cb.set_label("O I 7773 / [O II] 7330")
# ax.annotate("O I 7773 / [O II] 7330", (1e4, 18000))

ax.set(
    ylabel="Temperature, K",
    xlabel="Density, cm$^{-3}$",
    xscale='log',
)
sns.despine()
fig.tight_layout()
fig.savefig(figfile)
print(figfile, end='')
