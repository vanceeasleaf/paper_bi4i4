# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-23 22:24:34
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-23 22:32:14
from aces.io.phonopy.bandplot import plotbanddos
import numpy as np
dir = "bi4i4c.1/0/secondorder/"


def getpdos():
    xx = np.loadtxt(dir + 'partial_dos.dat', skiprows=1)
    freq = xx[:, 0]
    pdos = xx[:, 1:]
    return freq, pdos
freq, pdos = getpdos()
bandpath = ['Gamma', 'Y', "X", "L", "Z", "M", "Gamma"]
plotbanddos(
    freq=freq,
    dos=np.sum(pdos, axis=1), output_filename='phonon.eps',
    labels=' '.join(bandpath), filename0=dir + 'band.yaml', f_max=4.1)
