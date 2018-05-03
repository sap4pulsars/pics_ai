import sys
import os
import numpy as np
from subprocess import call
sys.path.append('/home/psr')
import cPickle, glob, ubc_AI
from ubc_AI.data import pfdreader
from ubc_AI.prepfold import pfd
import time
pfdfile = glob.glob('/home/psr/ubc_AI/pfd_files/*.pfd')
    
for i in pfdfile:
	Metadata = pfd('/dev/shm/test.pfd')	
    	print 'Name:',os.path.basename(os.path.normpath(pfdfile[i]))
    	print 'Telescope:',Metadata.telescope
    	print 'Barycentric Epoch:',Metadata.bepoch
    	print 'Topocentric Epoch:',Metadata.tepoch
    	print 'DM:',Metadata.bestdm
    	print 'Period (topo):',Metadata.topo_p1
    	print 'Pdot (topo):',Metadata.topo_p2
    	print 'P\'\'(topo):',Metadata.topo_p3
    	print 'Period (bary):',Metadata.bary_p1
    	print 'Pdot (bary):',Metadata.bary_p2
    	print 'Eccentricity:',Metadata.orb_e
    	print 'Orbital period:',Metadata.orb_p
