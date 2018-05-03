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
pfdfile = glob.glob('/home/psr/ubc_AI/pfd_files/*.pfd')



for i in pfdfile:
	Metadata = pfd(i)

	with open('%s'%i,'rb') as f:
        	data = f.read()

	data_packet={}
	data_packet['blob']=data
	data_packet['filename']=Metadata.pgdev[:-7]
	data_packet['Telescope']=Metadata.telescope
	data_packet['Barycentric Epoch']=Metadata.bepoch
	data_packet['Topocentric Epoch']=Metadata.tepoch
	data_packet['DM']=Metadata.bestdm
	data_packet['Period (topo)']=Metadata.topo_p1
	data_packet['Pdot (topo)']=Metadata.topo_p2
	data_packet['P\'\'(topo)']=Metadata.topo_p3
	data_packet['Period (bary)']=Metadata.bary_p1
	data_packet['Pdot (bary)']=Metadata.bary_p2
	data_packet['Eccentricity']=Metadata.orb_e
	data_packet['Orbital period']=Metadata.orb_p


	json_send_packet=bson.dumps(data_packet)
	client = KafkaClient(hosts="52.59.194.36:9092")
	topic = client.topics['MPIfR_test']
	producer = topic.get_sync_producer(max_request_size=10000012)

	try:
        	producer.produce(json_send_packet)
	except:
        	print 'Did not produce'

