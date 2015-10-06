PI Rover - motor class for Dagu Rover 5
========
This repository provides a simple motor class and ultrasonic sensor class in python. They can be used together to build an autonomous robot.

The code in the motor class assumes one L298N board is used for both left motors and both right motors using two different outputs.

#### Connection:

* 2S LiPo -> L298N
* 5v (PI) <- L298N
* Common ground


#### The code:

* motor.py - reusable motor class
* ultrasonic.py - takes measurements of distance
* drive.py - simple movement
* keyboard_drive - keyboard input for timed movements
* drive_then_halt - drive until ultrasonic sensor detects something within boundaries.


