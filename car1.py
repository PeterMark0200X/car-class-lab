class Car(object):
	def __init__(self, name='General', model='GM', vehicle_type=None, moving_speed = 0):
	self.name = name
	self.model = model
	self.vehicle_type = vehicle_type
	
	if self.name in ['Porshe', 'Koenigsegg']:
		self.num_of_doors = 2
	else:
		self.num_of_doors = 4
	if self.vehicle_type == 'trailer':
		self.num_of_wheels = 8
	else:
		self.num_of_wheels = 4
	
	def is_saloon(self):
		if self.vehicle_type is not 'trailer':
			self.vehicle_type == 'saloon'
			return True
		return False
		
	def drive(self, moving_speed):
		if moving_speed == 3:
			Car.speed = 1000
		elif moving_speed == 7:
			Car.speed = 77
		return self
		
car = Car(types = input("Bus,SUV,Truck,Saloon: "),model = input("Toyota, Benz, Isuzu, Infinity, GMT, Hyunda, Honda: "),name = input("Corolla,Harrier: "))
