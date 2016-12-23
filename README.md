# IoT-Actuation-Engine-GIoTTO

##Introduction :

The Actuation Engine is a generic actuation system which allows users to access a set of API&#39;s using which he can actuate the devices registered on the Building Depot .

The Flask server has been hosted on a port on BD server(https://bd-exp.andrew.cmu.edu:69). The devices that have been already connected to the actuation engine are Philips Hue, Wemo and Lifx bulbs. In order connect more type of devices Building Depot, the user needs to upload the new device actuation script into the &quot;Scripts&quot; folder of the Actuation Engine and edit the &quot;manager.py&quot; file to enable access to the device.

##Salient Features :

- **Generic in nature :** A generic access technique to control a large set of devices.
- **Customizable :** New device scripts can be easily added to the engine with little effort.
- **Independent :** It can function independently and can be accessed for any actuation of devices with proper credentials.

The location of the Actuation Engine in the System Block Diagram :
Inline-style: 
![alt text][logo]
https://github.com/SarwateShubham/IoT-Actuation-Engine-GIoTTO/blob/master/Actuation%20Engine.png "Actuation Engine Block Diagram")


##How to access the API :

**POST /api**

Within a single POST provide parameters to send request. The format for each sensor point in the list should be as follows.


|**API Access Template**| **JSON Parameter**|
| ------------- |:-------------:|
|Parameter 1|**Type :** The type of the device that needs to be actuated Eg. Wemo,Lifx,Philips Hue|
|Parameter 2|**New\_state :** The new state that device needs to be in. Eg. on,off,{&#39;color&#39; : &#39;green&#39;}etc.|
|Parameter 3| **Identity** : The unique identity of the device which can be used to identify the device on the network.Eg.MAC address, IP address, Device names etc.|
| **Returns:** | **success** (string) – Returns &#39;True&#39; if data is posted successfully otherwise &#39;False&#39; |
###API access example:

POST **/api**** HTTP**/1.1
>Accept: application/json; charset=utf-8
```javascript
[
  {
   "type":"lifx",
   "new_state":"on",
   "identity":"lifx-demo-room"
  }
]
```

