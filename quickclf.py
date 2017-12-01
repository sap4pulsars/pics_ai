import sys
sys.path.append('/home/psr')
#from subprocess import call
import cPickle, glob, ubc_AI
from ubc_AI.data import pfdreader
AI_PATH = '/'.join(ubc_AI.__file__.split('/')[:-1])
classifier = cPickle.load(open(AI_PATH+'/trained_AI/clfl2_PALFA.pkl','rb'))

with open('test.pfd', 'wb') as g:
    while True:
        buffer = sys.stdin.read(2330049) # Returns *at most* 2330049 bytes, maybe less
        if buffer == '':
            break
        g.write(buffer)
        #print(buffer)
        pfdfile=glob.glob('*.pfd')
        AI_scores = classifier.report_score([pfdreader(f) for f in pfdfile])
        print AI_scores[0]

