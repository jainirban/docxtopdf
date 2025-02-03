#!/bin/bash

sudo apt-get update -y
sudo apt-get install -y ttf-mscorefonts-installer fontconfig
sudo fc-cache -f -v
