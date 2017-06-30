# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-22 23:55:19
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-23 22:59:45
from aces.tools import parseyaml
from aces.graph import fig, pl
from aces.f import binmeanx
import numpy as np
dir = "bi4i4c.1/0/secondorder/"
file = dir + "groupv/mesh.yaml"
data = parseyaml(file)
freqs = []
gvs = []
for phonon in data['phonon']:
    qp = phonon['q-position']
    for band in phonon['band']:
        frequency = band['frequency']
        gv = np.array(band['group_velocity'])
        freqs.append(frequency)
        gvs.append(gv)
freqs = np.array(freqs)
gvs = np.array(gvs)
gvs = np.abs(gvs)
x, y = binmeanx(np.c_[freqs, gvs], [0, 4], 0.02)
with fig("gv.eps"):
    pl.plot(x, y, color="r", ls="-", lw=2)
