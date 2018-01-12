
# coding: utf-8

# In[ ]:


import sys
import subprocess
import numpy as np
import time
import binascii
import glob
#from bitstring import ConstBitStream

def pfd_stdout(num):
    num=int(num)

    for i in range(num):

        with open('/home/psr/ubc_AI/J1857+0943_PSR_1857+0943.pfd', 'rb') as g:
  
            print(g.read())
            print('eof')
            sys.stdout.flush()
            


            
       
def main():
    pfd_stdout(sys.argv[1])
if __name__ == '__main__':
    main()

