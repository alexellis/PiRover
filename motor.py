from RPIO import PWM
import time

# 4     LN4
# 17    LN3
# 27    LN2
# 22    LN1
class rover4wd:
	def __init__(self):
		PWM.setup()
		PWM.init_channel(0)
		ln4=10
		ln3=17
		ln2=27
		ln1=22
		self.v = [ln1,ln2,ln3,ln4]
		self.motorCombos={}
		self.pins={ "ln1":ln1,"ln2":ln2,"ln3":ln3,"ln4":ln4 }
		self.add_motor_comobos()

	def add_motor_comobos(self):
		self.add_motor_combo("left",["ln2","ln3"])
		self.add_motor_combo("right",["ln1","ln4"])
		self.add_motor_combo("forwards",["ln1","ln3"])
		self.add_motor_combo("reverse",["ln2","ln4"])

	def add_motor_combo(self,key,pinList):
		self.motorCombos[key] = pinList

	def go(self, key, spd, pause):
		pnlist=self.motorCombos[key]
		self.doublego(pnlist[0], pnlist[1],spd,pause)

	def doublego(self, lna,lnb,spd,pause):
        	pna = self.pins[lna]
	        pnb = self.pins[lnb]

	        PWM.add_channel_pulse(0,pna,0,spd)
	        PWM.add_channel_pulse(0,pnb,0,spd)

       		time.sleep(pause)
        	PWM.clear_channel_gpio(0,pna)
	        PWM.clear_channel_gpio(0,pnb)

	def dtest(self):
		for vv in v:
			print str(vv) + " pin"
			PWM.add_channel_pulse(0, vv, 0, 1000)
			time.sleep(1.5)
			PWM.clear_channel_gpio(0, vv)
