Dockerfile for PICS (Pulsar Image-based Classification System) AI based on W. W. Zhu et al. 2014. \
Contains: PRESTO TEMPO CALCEPH PSRCAT PYSLALIB THEANO \
Original Source code of the AI can be found at https://github.com/zhuww/ubc_AI \
The presto docker file is based on the work of https://github.com/ewanbarr/presto-docker


For generating Metadata:

docker run -i sap4pulsars/pics_ai:dev8 python /home/psr/ubc_AI/pfd_stdout_reader.py | docker run -i sap4pulsars/pics_ai:dev8 python /home/psr/ubc_AI/metadata.py


For generating AI score based on particular model

docker run -i sap4pulsars/pics_ai:dev8 python /home/psr/ubc_AI/pfd_stdout_reader.py | docker run -i sap4pulsars/pics_ai:dev8 python /home/psr/ubc_AI/ai_score.py <name_of_model>

Model names to choose from :

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

