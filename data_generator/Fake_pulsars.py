
# coding: utf-8

# In[57]:

import os, glob
import numpy as np
import docker
import sys
import curses

client = docker.APIClient(base_url='unix://var/run/docker.sock')



def generate_candidates(number):
    
    try:
        num = int(number)
    except ValueError:
        print('\nYou did not enter a valid integer')
        sys.exit(0)
        
    
    #image=client.pull('mpifrpsr/sigproc', tag='latest')
    
    for i in range(num):

        image='mpifrpsr/sigproc'

        dm = np.random.uniform(0,1500)
        period = np.random.uniform(10,10000)#ms
        snrpeak = np.random.uniform(0.6, 1.0)
        pulsewidth = np.random.uniform(0.5, 30)#percentage
        cwd=os.getcwd()

        container= client.create_container(
            image, '/bin/bash', stdin_open=True, tty=True, working_dir='/home/psr', \
            volumes=['/home/psr/data'], \
            host_config=client.create_host_config(binds={
                cwd +'/data/': {
                    'bind': '/home/psr/data',
                    'mode': 'rw',
                },}))

        client.start(container=container.get('Id'))
        cmds= 'fake -period %.2f -width %i -dm %.2f -tobs 42 -nbits 2 -snrpeak %.2f' %(period,pulsewidth,dm,snrpeak) 
        exe=client.exec_create(container=container.get('Id'), cmd= cmds, stdout=True)
        exe_start=client.exec_start(exec_id=exe, stream=True)
        with open(cwd + '/data/candidate_' + str(i) + '.fil', 'wb') as f: 
            for val in exe_start:
                f.write(val)

        client.stop(container=container.get('Id'))
        client.remove_container(container=container.get('Id'))
        
    
        #image=client.pull('mpifrpsr/sigproc', tag='latest')
        image='sap4pulsars/pics_ai:dev2'
        cwd=os.getcwd()
        container= client.create_container(
            image, '/bin/bash', stdin_open=True, tty=True, working_dir='/home/psr/ubc_AI', \
            volumes=['/home/psr/ubc_AI/data'], \
            host_config=client.create_host_config(binds={
                cwd +'/data/': {
                    'bind': '/home/psr/ubc_AI/data',
                    'mode': 'rw',
                },}))
        client.start(container=container.get('Id'))
        cmds= 'prepfold -filterbank -nodmsearch -dm %.2f -p %.2f data/candidate_' %(dm, period/1000) + str(i) + '.fil'
        exe=client.exec_create(container=container.get('Id'), cmd = cmds, stdout=True)
        exe_start=client.exec_start(exec_id=exe, stream=True)
        with open(cwd + '/data/prepfold.log', 'ab') as f: 
            for val in exe_start:
                f.write(val)
                
        client.stop(container=container.get('Id'))
        client.remove_container(container=container.get('Id'))
        
    image='sap4pulsars/pics_ai:dev2'            
    container= client.create_container(
        image, '/bin/bash', stdin_open=True, tty=True, working_dir='/home/psr/ubc_AI', \
        volumes=['/home/psr/ubc_AI/data'], \
        host_config=client.create_host_config(binds={
            cwd +'/data/': {
                'bind': '/home/psr/ubc_AI/data',
                'mode': 'rw',
            },}))
    client.start(container=container.get('Id'))

    cmds= 'python quickclf.py'
    exe=client.exec_create(container=container.get('Id'), cmd = cmds, stdout=True)
    exe_start=client.exec_start(exec_id=exe, stream=True)
    for val in exe_start:
        sys.stdout.buffer.write(val)

    client.stop(container=container.get('Id'))
    client.remove_container(container=container.get('Id'))

        



def main():
    generate_candidates(sys.argv[1])
if __name__ == '__main__':
    main()






