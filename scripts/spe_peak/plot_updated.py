#!/usr/bin/python
import os, sys, numpy, scipy, matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot

# The TA0003 parameters
def f(q, 
      exp_width=0.5057, 
      gaus_mean=1, 
      gaus_width=0.2916, 
      amp_ratio=1.624367847034316,
      exp_scale=1.):
    
    return exp_scale*numpy.exp(-q/exp_width) + amp_ratio/(numpy.sqrt(2*numpy.pi)*gaus_width) * numpy.exp(-(q-gaus_mean)**2/(2*gaus_width**2))

nom_rel, nom_exp, nom_gaus = 1.20638606785, 0.484848920822, 0.317171259177
hqe_rel, hqe_exp, hqe_gaus = 1.06866079978, 0.560924038403, 0.307780277986


q = numpy.linspace(0, 2, 101)
ta003 = f(q)

nom_full = f(q, exp_width=0.484848920822, gaus_width=0.317171259177, amp_ratio=1.20638606785)
hqe_full = f(q, exp_width=0.560924038403, gaus_width=0.307780277986, amp_ratio=1.06866079978)

# normalize all of them too
ta003 *= 100/numpy.sum(ta003)
nom_full *= 100/numpy.sum(nom_full)
hqe_full *= 100/numpy.sum(hqe_full)

fig = pyplot.figure(figsize=(8,5))
ax1 = fig.add_axes([0.1, 0.28, 0.86, 0.7])
ax2 = fig.add_axes([0.1, 0.10, 0.86, 0.15])
ax1.plot(q, ta003, 
         linewidth=3,
         color='k',
         label = 'Old SPE Model'
         )
ax1.plot(q, nom_full, 
         linewidth=3,
         linestyle='--',
         color='#CB4335',
         label = 'New SPE Model (Standard DOMs)'
         )
ax1.plot(q, hqe_full, 
         linewidth=3,
         linestyle='-.',
         color='#3498DB',
         label = 'New SPE Model (HQE DOMs)'
         )

# Ratios of the new to old
ax2.plot(q, (ta003-ta003)/ta003,
         color='k',
         linewidth=3)
ax2.plot(q, (nom_full-ta003)/ta003,
         linestyle='--',
         color='#CB4335',
         linewidth=3)
ax2.plot(q, (hqe_full-ta003)/ta003,
         linestyle='-.',
         color='#3498DB',
         linewidth=3)

ax1.set_xlim(0, 2)
ax1.set_ylim(ymin=0)
ax1.set_xticklabels([])
ax1.grid(alpha=0.2)

ax2.set_xlim(0, 2)
ax2.set_ylim(-0.5, 0.5)
ax2.set_yticklabels(["-50%", "0", "+50%"])
ax2.grid(alpha=0.2)

ax1.legend()
ax2.set_xlabel("Charge (PE)")
ax1.set_ylabel("Response (AU)")
ax2.set_ylabel("(New-Old)/Old")
pyplot.tight_layout()
pyplot.savefig('updated_models.pdf')
