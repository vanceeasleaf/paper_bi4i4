# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-22 23:47:49
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-23 00:18:41
import numpy as np
from aces.graph import fig, pl
import matplotlib as mpl
import os
mpl.rcParams['axes.color_cycle'] = ['#e24a33', '#2A749A', '#988ed5']
ts = np.arange(200, 801, 100)
a = []
for dir in ts:
    print(dir)
    x = np.loadtxt(
        "bi4i4computed.3/0/12844." +
        str(dir) +
        "K/BTE.kappa_tensor")
    a.append(x)
a = np.array(a)

name = os.path.basename(__file__).replace("py", "eps")
with fig(name, legend=True):
    k1 = a[:, 1]
    k2 = a[:, 5]
    k3 = a[:, 9]
    pl.plot(
        ts,
        k1,
        lw=3,
        markersize=30,
        linestyle='--',
        markeredgecolor='w',
        marker=".",
        label="${\kappa_{xx}}$")
    pl.plot(
        ts,
        k2,
        lw=3,
        markersize=15,
        linestyle='--',
        markeredgecolor='w',
        marker="v",
        label="${\kappa_{yy}}$")
    pl.plot(
        ts,
        k3,
        lw=3,
        markersize=15,
        linestyle='--',
        markeredgecolor='w',
        marker="^",
        label="${\kappa_{zz}}$")
    pl.xlabel("Tempeature (K)")
    pl.ylabel('Thermal Conductivity (W/mK)')
    pl.xlim([150, 850])
