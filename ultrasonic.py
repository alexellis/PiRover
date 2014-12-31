import RPi.GPIO as GPIO
import time

class distanceMeasure:
	def __init__(self,trigger,echo):
		self.GPIO_ECHO=echo
		self.GPIO_TRIGGER=trigger
        
	def setup(self):
		GPIO.setmode(GPIO.BCM)
		print "trigger = " + str(self.GPIO_TRIGGER)
		print "echo = " + str(self.GPIO_ECHO)
		# Set pins as output and input
		GPIO.setup(self.GPIO_TRIGGER,GPIO.OUT)  # Trigger
		GPIO.setup(self.GPIO_ECHO,GPIO.IN)      # Echo

	def measureDistance(self, settleTime):
		# Set trigger to False (Low)
		GPIO.output(self.GPIO_TRIGGER, False)

		# Allow module to settle
		time.sleep(settleTime)

		# Send 10us pulse to trigger
		GPIO.output(self.GPIO_TRIGGER, True)
		time.sleep(0.00001)
		GPIO.output(self.GPIO_TRIGGER, False)
		start = time.time()
		while GPIO.input(self.GPIO_ECHO)==0:
		  start = time.time()

		while GPIO.input(self.GPIO_ECHO)==1:
		  stop = time.time()

		# Calculate pulse length
		elapsed = stop-start

		# Distance pulse travelled in that time is time
		# multiplied by the speed of sound (cm/s)
		distance = elapsed * 34000

		# That was the distance there and back so halve the value
		distance = distance / 2

		#print "Distance : %.1f" % distance
		return distance

	def cleanup(self):
		GPIO.cleanup()

