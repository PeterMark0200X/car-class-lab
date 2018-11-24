class Car:
	def __init__(self, names, types, model):
		self.name = name
		self.types = types 
		self.model = model
		
car = Car(types = input("Bus,SUV,Truck,Saloon: "),model = input("Toyota, Benz, Isuzu, Infinity, GMT, Hyunda, Honda: "),name = input("Corolla,Harrier: "))
