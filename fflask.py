"""
fflask.py

This script should help me run a flask server on my laptop.

Demo:
/home/reqp/anaconda3/bin/python /home/reqp/reqp/fflask.py
"""
import os
from   flask import Flask
from   flask import send_from_directory
application = Flask(__name__)

@application.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@application.route("/")
def index():
    return send_from_directory(os.path.join(application.root_path, 'static'),'index.html')
                               
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5047))
    application.run(host='0.0.0.0', port=port)
'bye'
