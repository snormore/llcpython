ec2-run-instances ami-51492638 -n ${1-1} --kernel aki-b6aa75df -g quicklaunch-1 -k tr-default-keypair --availability-zone us-east-1a -t t1.micro -f llc-init.sh
