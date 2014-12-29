from RPIO import PWM
import time
from motor import rover4wd

rover = rover4wd()
rover.go("forwards", 1000,1)
rover.go("left", 1000,1)
rover.go("reverse", 1000,1)

