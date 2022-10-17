#!/bin/bash

## Download and Install VNC Viewer for ubuntu

ls -lh ~/Downloads
sudo apt update
sudo apt install ~/Downloads/VNC-Viewer-6.22.515-Linux-x86.deb
sudo apt --fix-broken install
