"""
reqp.py

This script should request prices.

Demo:
/home/reqp/anaconda3/bin/python /home/reqp/reqp/py/reqp.py
"""

import datetime
import os
import re
import requests
import sys
import time
import pdb

# I should use tkrlist.txt drive a loop

with open('/home/reqp/reqp/tkrlist.txt') as fh:
  tkrlist_s = fh.read()
  tkrlist_l = tkrlist_s.split()
  for tkr in tkrlist_l:
    pdb.set_trace()
    tkr
  
'bye'
