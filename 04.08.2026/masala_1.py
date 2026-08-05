class Student:
	def __init__(self,name):
		self.name = name
		self.__grade = []

	def set_grade(self,g):
		if g >= 0 and g <= 100:
			self.__grade.append(g)

	def get_grade(self):
		return self.__grade

if __name__ == "__main__":
	St1 = Student("Ali")
	St1.set_grade(90)
	St2 = Student("Vali")
	St2.set_grade(-90)
	print(St1.get_grade() if len(St1.get_grade()) > 0 else "Ball xato kiritilgan!")
	print(St2.get_grade() if len(St2.get_grade()) > 0 else "Ball xato kiritilgan!")
