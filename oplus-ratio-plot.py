from __future__ import print_function
import sys
import numpy as np
import pyneb as pn
import matplotlib.pyplot as plt
import seaborn as sns

o1r = pn.RecAtom('O', 1, case='A')
o2c = pn.Atom('O', 2)

Ts = np.linspace(5000, 15000)
Ds = 10**np.linspace(0.0, 7.0, 8)

def ratio_7773_7330(tem, den):
    em7330 = o2c.getEmissivity(tem, den, wave=7330.73)
    em7330 += o2c.getEmissivity(tem, den, wave=7329.66)
    em7773 = o1r.getEmissivity(tem, den, label='7773+')
    return em7773/em7330


figfile = sys.argv[0].replace('.py', '.pdf')
nD = len(Ds)
sns.set_palette('magma_r', n_colors=nD)
lws = np.linspace(2.0, 0.5, nD)
fig, ax = plt.subplots()

for D, lw in zip(Ds, lws):
    dstring = str(np.log10(D))
    label = r"$n = 10^{" + dstring + r"}\ \mathrm{cm}^{-3}$"
    ax.plot(Ts, ratio_7773_7330(Ts, D), lw=lw, label=label)

ax.legend(ncol=2)

ax.set(
    xlabel="Temperature, K",
    ylabel="O I 7773 / [O II] 7330",
    yscale='log',
)
sns.despine()
fig.tight_layout()
fig.savefig(figfile)
print(figfile, end='')
