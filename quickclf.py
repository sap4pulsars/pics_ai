import sys
import numpy as np
from subprocess import call
sys.path.append('/home/psr')
import cPickle, glob, ubc_AI
from ubc_AI.data import pfdreader
AI_PATH = '/'.join(ubc_AI.__file__.split('/')[:-1])
classifier = cPickle.load(open(AI_PATH+'/trained_AI/clfl2_PALFA.pkl','rb'))


data= sys.stdin.read()
num=int(sys.argv[1])
for i in range(num):

    with open('test.pfd', 'wb') as f:
        f.write(data)


    AI_scores = classifier.report_score(pfdreader('test.pfd'))
    print 'Fake_%i.pfd %f' %(i,AI_scores)

