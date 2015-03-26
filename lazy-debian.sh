#! /bin/bash

#also want to include in this file git cloning of my dot-files
# google-chrome comes in .deb package
# RStudio cames in .deb packaged
# ubuntu-extra-essentials 
ESSENTIALS=('ipython',
            'python-biopython',
	    'python-matplotlib',
	     'curl',
	     'vim',
	     'r-base',
	     'mendeley',
	     'klavaro',
	     'git',
	     'tmux',
	     'sl',
	     'vim',
	     'chromium',
	     'python-pip'
	     )

for i in $ESSENTIALS
do
  echo $i	
done
#sudo apt-get install 
