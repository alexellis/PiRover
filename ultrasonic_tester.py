from ultrasonic import distanceMeasure

dm = distanceMeasure(9, 11)
dm.setup()
out = dm.measureDistance( 0.25)
print "Distance : %.1f" %  out
dm.cleanup()

