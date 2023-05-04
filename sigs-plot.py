from matplotlib import pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# PYTHIA
sqrts = []
sigtot = []
sigdif = []
with open('sigma.txt') as f:
    for l in f:
        s1, s2, s3 = l.split()
        sqrts.append(float(s1))
        sigtot.append(float(s2)/1000.)
        sigdif.append(float(s3)/1000.)
ax.plot(sqrts,sigtot, label=r'PYTHIA $\sigma_{tot}$')
ax.plot(sqrts,sigdif, label=r'PYTHIA $\sigma_{diff}$')

ax.legend()
ax.set_xlabel(r'$\sqrt{s}$ [GeV]')
ax.set_ylabel(r'$\sigma$ [mb]')

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_ylim(0.01,1)
plt.show()
