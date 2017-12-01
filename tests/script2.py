
from bitstring import ConstBitStream
import sys
import numpy as np

#s = ConstBitStream(sys.stdin.readlines())
#s= bytearray(sys.stdin.readlines())
#print(sys.stdin.readlines())
#for something in sys.stdin:
    #s=ConstBitStream(something)
#s = ConstBitStream(sys.stdin.read())

with open('test.pfd', 'wb') as g:
    while True:
        buffer = sys.stdin.read(2330049) # Returns *at most* 2330049 bytes, maybe less
        if buffer == '':
            break
        g.write(buffer)
        print(buffer)
        #pfdfile=glob.glob('*t.pfd')
        #AI_scores = classifier.report_score([pfdreader(f) for f in pfdfile])
        #print AI_scores[0]
   

