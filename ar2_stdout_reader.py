
# coding: utf-8

# In[ ]:


import sys
import subprocess
import numpy as np
import time
import glob

pfdfile = glob.glob('ubc_AI/ar2_files/*.pfd') + glob.glob('ubc_AI/ar2_files/*.ar') + glob.glob('ubc_AI/ar2_files/*.ar2') + glob.glob('ubc_AI/ar2_files/*.spd')


def pfd_stdout():
    for i in range(len(pfdfile)):

        with open(pfdfile[i], 'rb') as g:
  
            print(g.read())
            print('eof')
            sys.stdout.flush()
            


            
       
def main():
    pfd_stdout()
if __name__ == '__main__':
    main()

