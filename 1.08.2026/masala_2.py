import os
class Ishchi:
	def __init__(self,name,position,salary):
		self.name = name
		self.position = position
		self.salary = salary

	def __gt__(self,x):
		return self.salary > x.salary

	def __str__(self):
		return f"Employee: {self.name:8s} ({self.position} - ${self.salary})"


if __name__ == "__main__":
	os.system("clear")
	emp1 = Ishchi("Ali","Developer",900)
	emp2 = Ishchi("Vali","Data analist",1000)
	emp3 = Ishchi("Komil","SMM",850)
	emp4 = Ishchi("Sardor","Boshliq",1200)
	ls = [emp1,emp2,emp3,emp4]

	for x in range(len(ls) - 1):
		for y in range(x + 1,len(ls)):
			if ls[x] > ls[y]:
				ls[x],ls[y] = ls[y],ls[x]
	for i in ls:
		print(i)
