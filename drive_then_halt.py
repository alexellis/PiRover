from motor import rover4wd
from ultrasonic import distanceMeasure

def stop(rover):
	rover.stopgoing()
def driving(rover,moveSpeed):
	rover.startgo("forwards",moveSpeed)	

def drive(haltDistance):
	rover=rover4wd()
	distance=distanceMeasure(9,11)
	distance.setup()
	moveSpeed=1000
	
	moving=True
	while(moving):
		cms = distance.measureDistance( 0.10)
		if(cms > haltDistance):
			driving(rover,moveSpeed)
		else:
			stop(rover)
			moving=False
	print "Arrived at destination"

if(__name__=='__main__'):
	haltDistance=20 #cm
	print "Driving with ultrasound sensor"
	drive(haltDistance)

