import sys
import os
import numpy as np
from subprocess import call
sys.path.append('/home/psr')
import cPickle, glob, ubc_AI
from ubc_AI.data import pfdreader
from ubc_AI.prepfold import pfd
import time
AI_PATH = '/'.join(ubc_AI.__file__.split('/')[:-1])
#classifier = cPickle.load(open(AI_PATH+'/trained_AI/clfl2_PALFA.pkl','rb'))
classifier = cPickle.load(open(AI_PATH+'/trained_AI/'+sys.argv[1],'rb'))
#pfdfile = glob.glob('ubc_AI/pfd_files/*.pfd') + glob.glob('ubc_AI/pfd_files/*.ar') + glob.glob('ubc_AI/pfd_files/*.ar2') + glob.glob('ubc_AI/pfd_files/*.spd')
pfdfile = glob.glob('/home/psr/ubc_AI/pfd_files/*.pfd')
AI_scores = classifier.report_score([pfdreader(f) for f in pfdfile])
text = '\n'.join(['%s %s' % (pfdfile[i], AI_scores[i]) for i in range(len(pfdfile))])
fout = open('clfresult.txt', 'w')
fout.write(text)
fout.close()

