import sys
import os
import numpy as np
from subprocess import call
sys.path.append('/home/psr')
import cPickle, glob, ubc_AI
from ubc_AI.data import pfdreader
from ubc_AI.prepfold import pfd
import time
pfdfile = glob.glob('ubc_AI/pfd_files/*.pfd') + glob.glob('ubc_AI/pfd_files/*.ar') + glob.glob('ubc_AI/pfd_files/*.ar2') + glob.glob('ubc_AI/pfd_files/*.spd')
timeout = time.time() + 60*15 # 15 minutes from now
data = ''
i=0
while True:
    if time.time() > timeout:
        break
    line = sys.stdin.readline()
    if line.strip() != 'eof':
        data += line
        continue
    else:
        with open('/dev/shm/test.pfd', 'wb') as f:
            f.write(data)
        data = ''
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
    print  ' '
    sys.stdout.flush()
    time.sleep(1)
    i+=1

    

