class Car:
	def __init__(self,model,color,hp,price):
		self.model = model
		self.color = color
		self.horsepower = hp
		self.price = price

	def __str__(self):
		return f"    === Car info ===\nModel:      {self.model}\nColor:      {self.color}\nHorsePower: {self.horsepower}\nPrice:      {self.price}"

class Cars:
	def __init__(self):
		self.cars = []

	def add_car(self,c):
		self.cars.append(car)

	def __contains__(self,y):
		for x in self.cars:
			if x.model == y:
				return True
		return False


if __name__ == "__main__":
	c1 = Car("BMW M5", "Black", 617, 105000)
	c2 = Car("Porsche 911 Turbo S", "White", 640, 230000)
	c3 = Car("Ferrari 488 GTB", "Red", 661, 280000)
	c4 = Car("Mercedes-AMG GT", "Silver", 577, 160000)
	c5 = Car("Audi RS7", "Gray", 591, 120000)

	cs = [c1,c2,c3,c4,c5]
	x = "Porsche 911 Turbo S"
	id = None

	for y in cs:
		if x in y.model:
			print(y)
			id = True
			break
	if id is None:
		print("Ma'lumot topilmadi")
