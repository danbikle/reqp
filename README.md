# README.md

This repo, reqp, should help me get and then prices.

This repo works well on Ubuntu 16.04.

Steps to install this repo are listed below:

* Boot a copy of Ubuntu 16.04.

* A VirtualBox image of Ubuntu 16.04 which should work well:

* https://drive.google.com/file/d/0Bx3iDDAtxxI4MmNNLXM4RTZvYTA

* I should boot the above instance and login as ann with password: 'a'

* I should issue a shell commands to create Linux account: 'reqp':

* sudo useradd -m -s /bin/bash -G sudo reqp

* sudo passwd reqp

* I should login as reqp

* I should install Anaconda with shell commands:

* wget https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh

* bash Anaconda3-4.4.0-Linux-x86_64.sh

* I should clone the reqp repo:

* cd ~reqp

* git clone https://github.com/danbikle/reqp

* I should get prices:

* cd ~reqp/reqp

* bin/reqp.bash

* I should serve the prices:

* cd ~reqp/reqp

* ./fflask.bash

* curl localhost:5047/static/csv/history/FB.csv > /tmp/FB.csv

* I should install heroku CLI

* I should deploy reqp to heroku

Questions?

e-me: bikle101 at gmail

Sincerely, Dan Bikle
Product Mgr: reqp
