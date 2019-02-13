#!/bin/env python
import sys, subprocess, os
sys.path.append('/home/psr/software/psrchive/install/lib/python2.7/site-packages')
sys.path.append('/home/psr')
import numpy as np
import hashlib
import glob, ubc_AI
import psrchive

def extract_metadata_ar2(ar2file):

	Metadata = psrchive.Archive_load(ar2file)
	archive0 = Metadata[0]
        metadata = {}

	with open(ar2file,'rb') as f:
	    candidate_blob = f.read()

	hash_id_blob = hashlib.sha256(candidate_blob).hexdigest()
	filename = Metadata.get_filename()
	dm = Metadata.get_dispersion_measure()
	topo_period = archive0.get_folding_period()
	center_freq = Metadata.get_centre_frequency()
	bandwidth = Metadata.get_bandwidth()
	telescope = Metadata.get_telescope()
	nchans = archive0.get_nchan()
	coordinates = Metadata.get_coordinates()
	deg_tuple = coordinates.getDegrees()
	ra_deg = float(deg_tuple.split(',')[0].replace("(",""))
	dec_deg = float(deg_tuple.split(',')[1].replace(")",""))
	ra_hms = coordinates.getHMSDMS().split(' ')[0]
	dec_hms = coordinates.getHMSDMS().split(' ')[1]
	basename = os.path.basename(filename)
	pointing = basename[:19]
	beam = basename[20:22]
	skipped_seconds = float(basename.split('S')[1].split('-')[0])
	int_length = Metadata.integration_length()
	accel_value = basename.split('-')[-1][:-4]
	file_location = '/media/vishnu/htru_candidates/vishnu/accel_pipeline/all_candidates/'
	owner = 'Vishnu'
	survey = 'HTRU-S-LOWLAT'
	algorithm = 'Acceleration Search'
	subints = Metadata.get_nsubint()

	''' Unpleasant Hack to read negative and positive acceleration value from filename. Had to do this because we no longer 
				have epheremis of all htru candidates after folding '''

	if 'a' in accel_value:
	    accel_value = float(accel_value.replace("a",""))
	else:
	    accel_value = float(accel_value) * -1

        for i in ('filename', 'hash_id_blob', 'topo_period', 'dm', 'center_freq', 'bandwidth', 'telescope', 'nchans', 'ra_deg', 'dec_deg', 'ra_hms', 'dec_hms', 'pointing', \
                   'beam', 'skipped_seconds', 'int_length', 'accel_value', 'owner', 'survey', 'algorithm', 'subints'):
            metadata[i] = locals()[i]
        
        return metadata

if __name__ == "__main__":

    all_ar2files = glob.glob('/home/psr/full_kepler_search/real_pipeline/candidate_plots_downsampled/test_ar2_files_htru/*.ar2')
    
    for f in all_ar2files:
      
       metadata = extract_metadata_ar2(f)
       print metadata 
