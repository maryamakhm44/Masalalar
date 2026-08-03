class Car:
	def __init__(self,model,hp,price):
		self.model = model
		self.horsepower = hp
		self.price = price

	def __eq__(self,x):
		return self.horsepower == x.horsepower and self.price == x.price


if __name__ == "__main__":
	m1 = Car("Mersedes AMG",1400,450000)
	m2 = Car("BMW M8",1350,450000)
	print(m1 == m2)
