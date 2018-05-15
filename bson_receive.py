import sys
import os
import numpy as np
from subprocess import call
sys.path.append('/home/psr')
import cPickle, glob, ubc_AI
from ubc_AI.data import pfdreader
from ubc_AI.prepfold import pfd
import bson
import hashlib
from pykafka import KafkaClient
 

def metadata_ai():

    client = KafkaClient(hosts="52.59.194.36:9092")
    topic = client.topics['MPIfR_beta5']
    consumer = topic.get_balanced_consumer(consumer_group='WDF_080518',auto_commit_enable=False,zookeeper_connect="52.59.194.36:2181",fetch_message_max_bytes=10000000)



    for msg in consumer:

        if msg is None:

            break

        for modelname in os.listdir('/home/psr/ubc_AI/trained_AI/'):

            if modelname.endswith(".pkl"):

                received_packet=bson.loads(msg.value)

                pfd_filename = str(received_packet['filename'])

                hasher = hashlib.sha256()

                hasher.update(received_packet['blob'])

                Candidate_ID = hasher.hexdigest()



                with open(pfd_filename,'wb') as f:

                    f.write(received_packet['blob'])

                modelpath = '/home/psr/ubc_AI/trained_AI/' + modelname

                classifier = cPickle.load(open(modelpath,'rb'))

                AI_score = classifier.report_score(pfdreader(pfd_filename))[0]

                print(Candidate_ID + "," + \
                    str(received_packet['filename']) + "," + \
                    modelname  + "," + \

                    str(received_packet['DM']) + "," + \

                    str(received_packet['Telescope']) + "," + \

                    str(received_packet['NChans']) + "," + \

                    str(received_packet['Azimuth']) + "," + \

                    str(received_packet['Elevation']) + "," + \

                    str(received_packet['Bandwidth']) + "," + \

                    str(received_packet['Period (topo)']) + "," + \

                    str(received_packet['Centre frequency:']) + "," + \
                    str(AI_score))




metadata_ai()
















#        print received_packet['blob']
#        print received_packet['filename']
#        print received_packet['Telescope']
#        print received_packet['Barycentric Epoch']
#        print received_packet['Topocentric Epoch']
#        print received_packet['DM']
#        print received_packet['Period (topo)']
#        print received_packet['Pdot (topo)']
#        print received_packet['P\'\'(topo)']
#        print received_packet['Period (bary)']
#        print received_packet['Pdot (bary)']
#        print received_packet['Eccentricity']
#        print received_packet['Orbital period']

