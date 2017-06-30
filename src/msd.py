# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-22 23:26:28
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-22 23:31:16
import numpy as np
from aces.graph import pl, fig


def reducemsd():
    msd = np.loadtxt('bi.md/600K/msd.txt')
    time = msd[:, 0]
    aa = []
    aa.append(np.loadtxt('bi.md/msd.txt')[:500, 1])
    aa.append(np.loadtxt('bi.md/600K/msd.txt')[:, 1])
    aa.append(np.loadtxt('bi.md/700K/msd.txt')[:, 1])
    aa.append(np.loadtxt('bi.md/800K/msd.txt')[:, 1])
    aa.append(np.loadtxt('bi.md/900K/msd.txt')[:, 1])
    aa = np.array(aa)
    ll = [300, 600, 700, 800, 900]
    import matplotlib
    matplotlib.rcParams['legend.fontsize'] = 12
    with fig('msd.eps', legend=True):
        for i, x in enumerate(aa):
            pl.plot(time, x, lw=2, label="%sK" % ll[i])

        pl.xlabel("Time (fs)")
        pl.ylabel("Mean Square Displacement (Angstrom)")
reducemsd()
