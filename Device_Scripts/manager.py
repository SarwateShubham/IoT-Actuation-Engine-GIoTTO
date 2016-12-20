'''
About: This is the module manages the various devices 
connected to Actutaion Engine.

Usage: Inorder to add another device please enter the generic 
schema of the functions to actuate devices using
the following parameters :

Identity: The unique identity of the device that needs to 
be actuated.

Type: The type of the device that we need to actuate.

New_State: The new state that the device needs to be set to.

Generic device setup:
Inorder to set up any other alternate device to the actuation 
engine, the user must add a actuation script to the Scripts
folder, and add another elif line to this script.

Eg.:

elif type=="DeviceX" :
	DeviceX.actuate_DeviceX(indentity,new_state)

* There must be a file named DeviceX.py with the function 
actuate_DeviceX defined.

'''
import wemo as wemo
import Philips_hue as Hue 
import lifx as lifx_lamp
def actuate(type,identity,new_state):
    if type=="wemo" :
        wemo.Actuate_wemo(identity,(new_state))
    elif type=="lifx" :
	lifx_lamp.actuate_lifx(identity,new_state)

