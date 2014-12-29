from motor import rover4wd
import sys
rover = rover4wd()

quit=False
turnTime=0.8
moveSpeed=1200
while(quit==False):
	sys.stdout.write( "Command: ")
	line=raw_input()
	if(line=='q'):
		quit=True
	elif(line=='w'):
		rover.go('forwards', moveSpeed,1)
	elif(line=='s'):
		rover.go('reverse', moveSpeed, 1)
	elif(line=='a'):
		rover.go('left', 1000, turnTime)
	elif(line=='d'):
		rover.go('right', 1000, turnTime)
	elif(line=="]"):
		if(moveSpeed+100<2000):
			moveSpeed+=100
			print "Move: "+str(moveSpeed)
		else:
			print "Speed must not exceed 1900"
	elif(line=="["):
		moveSpeed-=100
		print "Move: "+str(moveSpeed)
