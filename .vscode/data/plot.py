
import numpy as np

numerical_fix_prob_06=np.loadtxt('/Users/yagoobi/Documents/GitHub/fixation-probability/.vscode/data/star-N_5-M_4-mig-1e-06.txt')
numerical_fix_prob_l_001=np.loadtxt('/Users/yagoobi/Documents/GitHub/fixation-probability/.vscode/data/star-N_5-M_4-mig-0.01.txt')
numerical_fix_prob_l_01=np.loadtxt('/Users/yagoobi/Documents/GitHub/fixation-probability/.vscode/data/star-N_5-M_4-mig-0.1.txt')
numerical_fix_prob_l_05=np.loadtxt('/Users/yagoobi/Documents/GitHub/fixation-probability/.vscode/data/star-N_5-M_4-mig-0.5.txt')
numerical_fix_prob_l_1=np.loadtxt('/Users/yagoobi/Documents/GitHub/fixation-probability/.vscode/data/star-N_5-M_4-mig-1.txt')

# import parameters
import parameters

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots(figsize=(10,7))
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.25))
ax.ticklabel_format(axis='y',style='sci',scilimits=(0,0))

ylim=[-0.01,0.06]
plt.xlim(left=0)

plt.xlim(right=2)
plt.ylim(top=ylim[1])
plt.ylim(bottom=ylim[0])
plt.fill_between(np.linspace(0,1,20),y1=0,y2=ylim[1], color='whitesmoke')
plt.fill_between(np.linspace(1.,2,20),y1=ylim[0],y2=0, color='whitesmoke')
ax.axhline(y=0, color='k')

#ax.plot(Fitness1,fix_prob_star_patch(Fitness1)-fix_prob_well_mixed(Fitness1,local_size*patch_number), color='g',label='low-migration')
ax.plot(parameters.Fitness, numerical_fix_prob_06[:,1] ,'P',color='tab:orange',markerfacecolor='none', label='$\lambda= 10^{-6}$')
ax.plot(parameters.Fitness, numerical_fix_prob_l_001[:,1] ,'s',color='b',markerfacecolor='none', label='$\lambda= 0.01$')
ax.plot(parameters.Fitness,numerical_fix_prob_l_01[:,1], '*',color='m',markerfacecolor='none', label='$\lambda=0.1$')
ax.plot(parameters.Fitness, numerical_fix_prob_l_05[:,1] ,'v',color='c',markerfacecolor='none', label='$\lambda= 0.5$')
ax.plot(parameters.Fitness, numerical_fix_prob_l_1[:,1],'o',color='darkred',markerfacecolor='none', label='$\lambda= 1$')
#ax.plot(Fitness1, phi(Fitness1,local_size,local_size*(patch_number-1))-fix_prob_well_mixed(Fitness1,local_size*patch_number), color='r', label='$\lambda= 1$')
ax.tick_params(labelsize=12, direction='out',top=True, right=True)
ax.set_xlabel(r'fitness ($\bf{r}$) ',fontsize=14)
ax.set_ylabel(r"Difference in fixation probabilities, $\phi_{\bigstar}- \phi_{\rm wm} $",fontsize=14)

plt.legend(fontsize=14)
plt.show()