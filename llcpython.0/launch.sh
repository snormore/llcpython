#!/bin/bash
cd /home/ec2-user/
rm *ipynb

for F in llc_python.py 01_introduction.ipynb 02_hello_llc.ipynb \
    03-ColorsBlocks.ipynb 04-PlayGrid.ipynb 05-FeelingLoopy.ipynb 06-Functions.ipynb 07-MindBlown.ipynb; do
    wget https://raw.github.com/tavisrudd/llc_python/master/$F
done
echo 'starting ipython'
/home/ec2-user/anaconda/bin/ipython notebook --ip='0.0.0.0' --no-browser &
sleep 10
python -c "from llc_python import hello_llc; hello_llc('http://`curl http://instance-data.ec2.internal/latest/meta-data/public-hostname`:8888')"
