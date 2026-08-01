import os
class Developer:
	def __init__(self,surname,position,salary):
		self.surname = surname
		self.position = position
		self.salary = salary

class SoftwareEngineer(Developer):
	def __init__(self,surname,position,salary,bonus,department):
		super().__init__(surname,position,salary)
		self.bonus = bonus
		self.department = department

def umumiy_summa(x):
	return x.salary + x.bonus

def task(res):
	dc,summa = {},{}
	for x in range(len(res)):
		itm = f"{res[x].department} bo'lim"
		if itm in dc.keys():
			dc[itm] += 1
			summa[itm] += umumiy_summa(res[x])
		else:
			dc[itm] = 1
			summa[itm] = umumiy_summa(res[x])

	for i,y in zip(dc,summa):
		print(f"{i}: {dc[i]} ta dasturchi, jami to'lov: {summa[y]}")


if __name__ == "__main__":
	os.system("clear")
	obj1 = SoftwareEngineer("Anvar","Junior",500,100,1)
	obj2 = SoftwareEngineer("Asror","Middle",1500,500,2)
	obj3 = SoftwareEngineer("Kamola","Senior",2500,100,3)
	obj4 = SoftwareEngineer("Vali","Junior",500,100,1)
	obj5 = SoftwareEngineer("Davron","Middle",1500,100,2)
	res = [obj1,obj2,obj3,obj4,obj5]
	task(res)
