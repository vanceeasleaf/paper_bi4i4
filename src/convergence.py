# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-22 23:33:17
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-22 23:53:21


from scanf import sscanf
from aces.graph import fig, pl, setLegend
import matplotlib as mpl
import aces.tools as tl
import numpy as np
mpl.rcParams['axes.color_cycle'] = ['#e24a33', '#2A749A', '#988ed5']
us = []
dirs = tl.ls('bi4i4computed.3/0/shengold*')
print(dirs)
for d in dirs:
    f = tl.shell_exec('grep ngrid %s/CONTROL' % d)
    ks = sscanf(f, "   ngrid(:)=%d %d %d")
    f = np.loadtxt('%s/BTE.kappa_tensor' % d)
    print(ks)
    if len(f.shape) == 2:
        x = f[-1]
    else:
        x = f
    x = x[1:].reshape([3, 3])
    # print(x)
    us.append([ks, x])

with fig('convergence.eps'):
    # kkappa_64nn
    fi, axes = pl.subplots(1, 2, sharey=True)
    ax = axes[0]
    p1 = filter(lambda u: u[0][0] == 64, us)
    print(p1)
    k1 = []
    k2 = []
    k3 = []
    ks = []
    for u in p1:
        ks.append(u[0][1])
        k1.append(u[1][0, 0])
        k2.append(u[1][1, 1])
        k3.append(u[1][2, 2])
    f = np.argsort(ks)
    ks = np.array(ks)[f]
    k1 = np.array(k1)[f]
    k2 = np.array(k2)[f]
    k3 = np.array(k3)[f]
    ax.plot(
        ks,
        k1,
        markersize=30,
        linestyle='--',
        markeredgecolor='w',
        marker=".",
        label="${\kappa_{xx}}$")
    ax.plot(
        ks,
        k2,
        markersize=15,
        linestyle='--',
        markeredgecolor='w',
        marker="v",
        label="${\kappa_{yy}}$")
    ax.plot(
        ks,
        k3,
        markersize=15,
        linestyle='--',
        markeredgecolor='w',
        marker="^",
        label="${\kappa_{zz}}$")
    ax.set_ylim([0, 0.35])
    ax.set_xlim([0, np.array(ks).max() + 1.5])
    ax.set_xlabel("$Nq_y$ and $Nq_z$")
    ax.set_ylabel("Themal Conductivity (W/mK)")
    setLegend(ax)
    ax = axes[1]
    # kkappa_n44.png
    p1 = filter(lambda u: u[0][1] == 4, us)
    k1 = []
    k2 = []
    k3 = []
    ks = []
    for u in p1:
        ks.append(u[0][0])
        k1.append(u[1][0, 0])
        k2.append(u[1][1, 1])
        k3.append(u[1][2, 2])
    f = np.argsort(ks)
    ks = np.array(ks)[f]
    k1 = np.array(k1)[f]
    k2 = np.array(k2)[f]
    k3 = np.array(k3)[f]
    ax.plot(
        ks,
        k1,
        markersize=30,
        linestyle='--',
        markeredgecolor='w',
        marker=".",
        label="${\kappa_{xx}}$")
    ax.plot(
        ks,
        k2,
        markersize=15,
        linestyle='--',
        markeredgecolor='w',
        marker="v",
        label="${\kappa_{yy}}$")
    ax.plot(
        ks,
        k3,
        markersize=15,
        linestyle='--',
        markeredgecolor='w',
        marker="^",
        label="${\kappa_{zz}}$")
    ax.set_ylim([0, 0.35])
    ax.set_xlim([0, np.array(ks).max() + 100])
    ax.set_xlabel("$Nq_x$")
    setLegend(ax)
    fi.subplots_adjust(
        left=None,
        bottom=None,
        right=None,
        top=None,
        wspace=0,
        hspace=0)
