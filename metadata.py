import sys
import os
import numpy as np
from subprocess import call
sys.path.append('/home/psr')
import cPickle, glob, ubc_AI
from ubc_AI.data import pfdreader
from ubc_AI.prepfold import pfd
from ubc_AI.psrarchive_reader import ar2data
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
        with open('/dev/shm/test.ar2', 'wb') as f:
            f.write(data)
        data = ''
    Metadata = ar2data('/dev/shm/test.ar2')	
    print 'Name:',Metadata.filename
    print 'DM:',Metadata.dm
    print 'Period (topo):',Metadata.period
    print 'Centre frequency:',Metadata.freq
    print 'Bandwidth:',Metadata.bandwidth
    print  ' '
    sys.stdout.flush()
    time.sleep(1)
    i+=1

    

