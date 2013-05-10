#!/bin/bash
cd /home/ec2-user
rm *ipynb
wget https://raw.github.com/tavisrudd/llc_python/master/launch.sh
chmod +x launch.sh
su - ec2-user -c"/home/ec2-user/launch.sh" 2&> /var/log/ipython &
