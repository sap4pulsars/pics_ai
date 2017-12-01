for FILE in `seq 1 $1`; do cp J1857+0943_PSR_1857+0943.pfd  Pulsar_$FILE.pfd; done
rm J1857+0943_PSR_1857+0943.pfd
mv *.pfd common_vol/
