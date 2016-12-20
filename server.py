'''
About:
This module is the way various devices connected to 
the Building Depot v3 can be actuated using a generic rest API
calls to the Actuation Engine.

The definations of the API's of the actuation engine are listed 
below.
'''
from flask import Flask
from flask import request
import json
import time
import requests
import time

import Scripts.manager as manager
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

def jsonString(obj,pretty=False):
    if pretty == True:
        return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')) + '\n'
    else:
        return json.dumps(obj)

@app.route("/")
def hello():
'''
A display page to see if the actuation engine is running.
'''
    return "<h1 style='color:blue'>Hello There!This is the actuation engine!</h1>"
    
@app.route('/time', methods=['GET'])
def get_time():
'''
Defination: A GET request to '/time' returns the time currently at 
the server this maybe useful incase the user wished to use the 
actuate the devices at specific time intervals, also if the location of the
actuation engine is another time zone compared to where it is
being accessed form.

Usage:


'''
    timestamp = time.time()
    dic = {
        'url':request.remote_addr,
        'method':request.method,
        'result':'ok',
        'ret':timestamp
    }
    return jsonString(dic)

@app.route('/api', methods=['POST'])
'''
Defination: This is the core API of the actuation engine , which 
allows the users of the Building Depot v3 to access and control 
the states of their devices using a generic API call.

Usage: 

POST /api HTTP/1.1
Accept: application/json; charset=utf-8
[
  {
   “type”:”lifx”,
   “new_state”:”on”,
   “identity”:”lifx-demo-room”  
  }
]

'''
def run_script():
    data=request.data
    print data
    js=json.loads(data)
    print js,type(js)
    typ=js['type']
    identity=js['identity']
    new_state=js['new_state']
    manager.actuate(typ,identity,new_state)
    return data

if __name__ == "__main__":
'''
The port for hosting the Actuation Engine can be defined below.
For eg. in this case the Actuation engine is hosted 
'''
    app.run(host='0.0.0.0',port=55,debug=True)
