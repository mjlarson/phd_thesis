#!/usr/bin/python
import os, sys, numpy, matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot



fig, ax = pyplot.subplots(1,1, figsize = (20, 3))
ax.set_xlim(1e6, 1e15)
ax.set_ylim(0, 1)
ax.set_xscale('log')
ax.get_yaxis().set_visible(False)
ax.set_xticks([1e6, #1e7, 1e8, 
               1e9, #1e10, 1e11, 
               1e12, #1e13, 1e14,
               1e15, #1e16, 1e17,
               1e18])

ax.set_xticklabels(['1 MeV', #'10 MeV', '100 MeV', 
                    '1 GeV', #'10 GeV', '100 GeV', 
                    '1 TeV', #'10 TeV', '100 TeV', 
                    '1 PeV', #'10 PeV', '100 PeV', 
                    '1 EeV',],
                   fontsize = 18)


pyplot.savefig('energy_range.pdf')