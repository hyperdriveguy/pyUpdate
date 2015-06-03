#!/bin/bash

# Resolve dependencies
sudo apt-get update
sudo apt-get install python3 git

git clone https://github.com/hyperdriveguy/pyUpdate.git
cd pyUpdate-master
sudo mv pyUpdate.py /bin/pyUpdate.py
sudo mv py-update /bin/py-update
rm install.sh
rm readme.md
cd $HOME
mkdir .pyUpdate
cd pyUpdate-master
mv updaterConfig.txt $HOME/.pyUpdate/updaterConfig.txt
rm .gitignore
cd $HOME
rm pyUpdate-master
exit
