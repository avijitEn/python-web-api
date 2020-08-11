import os
import sys
import requests
from flask import render_template
import socket
from flask import Flask
import random
#from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)
color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

SUPPORTED_COLORS = ",".join(color_codes.keys())

# Get color from Environment variable
COLOR_FROM_ENV = os.environ.get('APP_COLOR')
# Generate a random color
COLOR = random.choice(["red", "green", "blue", "blue2", "darkblue", "pink"])

@app.route('/')
def index():

    return render_template('webapi.html', name=socket.gethostname(),webapiHostName=get_webapi_hostname(),color=color_codes[COLOR])


def get_hostname():
    return socket.gethostname();

def get_webapi_hostname():
    # the web container MUST be run with --link <appName>:helloapp
    # link_alias = 'helloapp'

    # Load the environment variables from the .env file.
    # They will be overwritten if environment vars are set
    #load_dotenv(find_dotenv())
    url = os.environ.get("APPURL")
    #url='http://127.0.0.2:5000/'

    # Request data from the app container
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
