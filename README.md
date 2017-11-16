Dockerfile for PICS (Pulsar Image-based Classification System) AI based on W. W. Zhu et al. 2014. \
Contains: PRESTO TEMPO CALCEPH PSRCAT PYSLALIB THEANO \
Original Source code of the AI can be found at https://github.com/zhuww/ubc_AI \
The presto docker file is based on the work of https://github.com/ewanbarr/presto-docker




run the following command to obtain the score for your input file :

$ cat [filename] | docker run -i sap4pulsars/pics_ai:dev python quickclf.py > result1
the file  named 'result1' has your score 

Score Generated is between 0 and 1. \
1- Completely Pulsar Like \
0- Completely Non-Pulsar Like

