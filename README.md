Dockerfile for PICS (Pulsar Image-based Classification System) AI based on W. W. Zhu et al. 2014. \
Contains: PRESTO TEMPO CALCEPH PSRCAT PYSLALIB THEANO \
Original Source code of the AI can be found at https://github.com/zhuww/ubc_AI \
The presto docker file is based on the work of https://github.com/ewanbarr/presto-docker


For Producing to Kafka Client:

python bson_send.py

For Consuming from Kafka Client:

python bson_receive.py

Consumer loops over all models kept in ubc_AI/trained_AI. List of all models currently available is given below.

clfl2_BD.pkl
clfl2_FL.pkl
clfl2_HTRU.pkl
clfl2_HTRU_0.pkl
clfl2_HTRU_1.pkl
clfl2_HTRU_2.pkl
clfl2_PALFA.pkl
clfl2_SP_0.0.pkl
clfsvm_HTRU_2.pkl

Results will be outputted to stdout

Score Generated is between 0 and 1. \
1- Pulsar \
0- Not a Pulsar 

To stream *.ar2 files from hercules cluster:

singularity exec -H /u/vishnu:/home1 -B /u/vishnu/HTRU-S-LOWLAT/storage/View/ar2_files_htru/:/home/psr/ubc_AI/ar2_files_htru /u/vishnu/sap4pulsars_pics_ai_dev10.img  python /home/psr/ubc_AI/ar2_files_htru/bson_send_modified.py

