#!/bin/bash

# reqp.bash

# I should use this script to call Python to request prices.

# This script is often called by cron.

echo $0 busy
date
/home/reqp/anaconda3/bin/python /home/reqp/reqp/py/reqp.py /home/reqp/reqp/tkrlist.txt

# I should copy the prices to a folder which helps me serve them.
rsync -av /home/reqp/csv /home/reqp/reqp/static/
date

exit

