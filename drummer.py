"""
Explorer HAT Drummer
Les Pounder 2016 http://bigl.es
This code is released under a CC-BY-SA 2.0 licence

TO INSTALL
With your Raspberry Pi turned off attach the Explorer HAT Pro to all of the GPIO pins.
Attach your keyboard, mouse, HDMI, and then power to the Raspberry Pi and boot to the desktop.
You will need an Internet connection for your Raspberry Pi.
Open a terminal and follow the "Easy Way" instructions at https://github.com/pimoroni/explorer-hat/

TO RUN THIS CODE
Open this code in the Python 3 application, found in the main Raspbian menu under Programming.
Click on Run >> Run Module and then press button 1 on the Explorer HAT to start the drummer.
Try tinkering with the timings "sleep(0.1)" to create a different beat.
"""

#Import the modules that will power our code.
#Explorer HAT module enables our code to talk to the board.
import explorerhat
#We import the sleep function from the time module, this means we can pause the code by using sleep(x)
from time import sleep

"""
In this next block of code we create a function which we shall use to group together the code.

We call the function drummer, and instruct it to look for a channel and event.
The channel is the number of the button that has been pressed.
The Event is how the button has been pressed.
"""
def drummer(channel, event):
	#We can flash all of the LEDs at once, with a pattern of 0.5s on and 0.5s off.
    explorerhat.light.blink(0.5,0.5)
    #We use a for loop to create a loop of four beats.
    for beat in range(4):
    	#Motor one turns on for 0.1s.
    	explorerhat.motor.one.forward(100)
    	#We delay for a tenth of a second.
    	sleep(0.1)
    	#Motor two turns on for 0.1s
    	explorerhat.motor.two.forward(100)
    	#We delay for a tenth of a second.
    	sleep(0.1)
    	#We stop all of the motors
    	explorerhat.motor.stop()
    #We turn off the lights
    explorerhat.light.off()

"""
Here we call the function "drummer" everytime button one is pressed.
We do not need to tell our drummer function the channel or event, as that is implied by pressing (the event) button 1 (the channel)
"""
explorerhat.touch.one.pressed(drummer)
 