import sys
sys.path.append('/home/psr')
from subprocess import call
import cPickle, glob, ubc_AI
from ubc_AI.data import pfdreader
AI_PATH = '/'.join(ubc_AI.__file__.split('/')[:-1])
classifier = cPickle.load(open(AI_PATH+'/trained_AI/clfl2_PALFA.pkl','rb'))
#pfdfile = glob.glob('*.pfd') + glob.glob('*.ar') + glob.glob('*.ar2') + glob.glob('*.spd')
#AI_scores = classifier.report_score([pfdreader(f) for f in pfdfile])
#fout=open('test_pfd','w')
#fout.write(sys.stdin)
#fout.close()
#script1 = "cd common_vol/"
#script2 = "rm  test.pfd"
#call(script1,shell=True)
pfdfile=glob.glob('common_vol/*.pfd')
AI_scores = classifier.report_score([pfdreader(f) for f in pfdfile])
for i in range(len(pfdfile)):
    print pfdfile[i],AI_scores[i]
#call(script2,shell=True)
#text = '\n'.join(['%s %s' % (pfdfile[i], AI_scores[i]) for i in range(len(pfdfile))])
#fout = open('clfresult.txt', 'w')
#fout.write(text)
#fout.close()
#print text
