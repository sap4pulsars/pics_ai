Dockerfile for PICS (Pulsar Image-based Classification System) AI based on W. W. Zhu et al. 2014. \
Contains: PRESTO TEMPO CALCEPH PSRCAT PYSLALIB THEANO \
Original Source code of the AI can be found at https://github.com/zhuww/ubc_AI \
The presto docker file is based on the work of https://github.com/ewanbarr/presto-docker



Run following commands
1. docker run -it -v *path to current repo*/common_vol:/home/psr/ubc_AI/common_vol [image_name] sh generate_pfd.sh [no. of arguements]

2. docker run -it -v path to current repo*/common_vol:/home/psr/ubc_AI/common_vol sap_30nov_v5 python quickclf.py
 
