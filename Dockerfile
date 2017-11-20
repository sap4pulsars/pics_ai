FROM sap4pulsars/pics_ai:latest
COPY J1857+0943_PSR_1857+0943.pfd $HOME/ubc_AI
COPY generate_pfd.sh $HOME/ubc_AI
WORKDIR $HOME/ubc_AI
RUN sh generate_pfd.sh 5
RUN rm J1857+0943_PSR_1857+0943.pfd
