import sys
import os
import numpy as np
from subprocess import call
sys.path.append('/home/psr')
import cPickle, glob, ubc_AI
from ubc_AI.data import pfdreader
from ubc_AI.prepfold import pfd
import bson
from pykafka import KafkaClient




client = KafkaClient(hosts="52.59.194.36:9092")

topic = client.topics['MPIfR_test']

consumer=topic.get_balanced_consumer(consumer_group='test1',auto_commit_enable=False,zookeeper=None,fetch_message_max_bytes=10000000)

for msg in consumer:
        if msg is None:
                break
        received_packet=bson.loads(msg.value)
        with open('%s'%received_packet['filename'],'wb') as f:
                f.write(received_packet['blob'])
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

