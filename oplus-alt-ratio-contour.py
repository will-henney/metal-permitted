from __future__ import print_function
import sys
import numpy as np
import pyneb as pn
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

o1r = pn.RecAtom('O', 1, case='A')
o2c = pn.Atom('O', 2)

Ts = np.linspace(3000, 25000, 300)
Ds = 10**np.linspace(0.0, 9.0, 200)

def ratio_7773_7320(tem, den):
    em7320 = o2c.getEmissivity(tem, den, wave=7318.92)
    em7320 += o2c.getEmissivity(tem, den, wave=7319.98)
    em7773 = o1r.getEmissivity(tem, den, label='7773+')
    return em7773/em7320


figfile = sys.argv[0].replace('.py', '.pdf')

ratios = ratio_7773_7320(Ts, Ds).T
levels = [3.0, 1.0, 0.3, 0.1, 0.03, 0.01, 0.003, 0.001, 0.0003]
fig, ax = plt.subplots()

Ts = Ts[None, :]*np.ones_like(ratios)
Ds = Ds[:, None]*np.ones_like(ratios)

#ax.contour(Ts, Ds, Ds, levels=[100, 10000, 1e6], cmap='magma_r')
c = ax.contour(Ts, Ds, ratios,
               levels=levels[::-1],
               cmap='magma_r',
               norm=mpl.colors.LogNorm())
ax.clabel(c, levels[1::2], fontsize='x-small',
          inline=False)
ax.legend(ncol=2)

ax.set(
    xlabel="Temperature, K",
    ylabel="Density, [cc]",
    yscale='log',
)
sns.despine()
fig.tight_layout()
fig.savefig(figfile)
print(figfile, end='')
