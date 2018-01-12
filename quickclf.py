import sys
import numpy as np
from subprocess import call
sys.path.append('/home/psr')
import cPickle, glob, ubc_AI
from ubc_AI.data import pfdreader
import time
AI_PATH = '/'.join(ubc_AI.__file__.split('/')[:-1])
classifier = cPickle.load(open(AI_PATH+'/trained_AI/clfl2_PALFA.pkl','rb'))
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
        with open('test.pfd', 'wb') as f:
            f.write(data)
        data = ''
    AI_scores = classifier.report_score(pfdreader('test.pfd'))
    print 'Fake_%i.pfd %f' %(i,AI_scores)
    sys.stdout.flush()
    time.sleep(1)
    i+=1

    

