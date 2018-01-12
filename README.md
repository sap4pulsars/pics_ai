Dockerfile for PICS (Pulsar Image-based Classification System) AI based on W. W. Zhu et al. 2014. \
Contains: PRESTO TEMPO CALCEPH PSRCAT PYSLALIB THEANO \
Original Source code of the AI can be found at https://github.com/zhuww/ubc_AI \
The presto docker file is based on the work of https://github.com/ewanbarr/presto-docker

docker run -i sap4pulsars/pics_ai:dev7 python /home/psr/ubc_AI/pfd_stdout_reader.py | docker run -i sap4pulsars/pics_ai:dev7 python /home/psr/ubc_AI/quickclf.py



Results will be outputted to stdout

Score Generated is between 0 and 1. \
1- Pulsar \
0- Not a Pulsar 

