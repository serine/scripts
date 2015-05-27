#! /bin/bash

#also want to include in this file git cloning of my dot-files
# google-chrome comes in .deb package
# RStudio cames in .deb packaged
# ubuntu-extra-essentials 
ESSENTIALS=(ubuntu-restricted-extras \
	    vlc \
	    clementine \
	    python \
	    python-pip \
	    ipython \
	    python-biopython \
	    python-matplotlib \
	    curl \
	    vim \
	    r-base 
            git \
	    tmux \
	    sl \
            mosh \
	    htop \
	    dconf-editor \
	    libgnome2-bin \
	   )

GETRIDOFF=(rhythmbox \
	   unity-webapps-common \
	  )

echo sudo apt-get remove --purge ${GETRIDOFF[*]} && \
echo sudo apt-get autoremove && \
echo sudo apt-get autoclean && \
echo sudo apt-get update && \
echo sudo apt-get upgrade && \
echo sudo apt-get autoremove && \
echo sudo apt-get autoclean && \
echo sudo apt-get install ${ESSENTIALS[*]}  && \
echo sudo apt-get update && \
echo sudo apt-get upgrade && \
echo sudo apt-get -f install && \
echo sudo apt-get autoremove && \
echo sudo apt-get autoclean && \
echo sudo reboot 
