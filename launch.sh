#!/bin/bash
cd /home/ec2-user/

for F in llc_python.py 01_introduction.ipynb 02_hello_llc.ipynb \
    03-ColorsBlocks.ipynb 04-PlayGrid.ipynb 05-FeelingLoopy.ipynb 06-Functions.ipynb 07-MindBlown.ipynb; do
    wget https://raw.github.com/tavisrudd/llc_python/master/$F
done
echo 'starting ipython'
/home/ec2-user/anaconda/bin/ipython notebook --ip='0.0.0.0' --no-browser
