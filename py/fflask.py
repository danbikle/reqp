"""
fflask.py
Demo:
/home/reqp/anaconda3/bin/python /home/reqp/reqp/py/fflask.py
"""
import os
from   flask import Flask
application = Flask(__name__)
                               
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5047))
    application.run(host='0.0.0.0', port=port)
'bye'
