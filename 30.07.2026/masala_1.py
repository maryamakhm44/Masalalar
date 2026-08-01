import os
class Employee:
	def __init__(self,surname,position,salary):
		self.surname = surname
		self.position = position
		self.salary = salary

	def get_info(self):
		print(f"Surname:     {self.surname}")
		print(f"Position:    {self.position}")
		print(f"Salary:      {self.salary}")

class EnterpriseEmployee(Employee):
	def __init__(self,surname,position,salary,rating):
		super().__init__(surname,position,salary)
		if rating >= 0 and rating <= 100:
			self.rating = rating

	def oshirilgan_oylik(self):
		oylik = self.salary
		if 60 <= self.rating and self.rating < 75:
			return oylik * 0.15 + oylik
		elif 75 <= self.rating and self.rating < 90:
			return oylik * 0.4 + oylik
		elif 90 <= self.rating and self.rating <= 100:
			return oylik * 0.6 + oylik
		else:
			return oylik


if __name__ == "__main__":
	os.system("clear")
	emp1 = EnterpriseEmployee("Karimov","Boshliq",10000,85)
	try:
		res = emp1.oshirilgan_oylik()
		emp1.get_info()
		print(f"Oshirilgan oylik: {res}")
	except:
		print("Rating xato kiritildi")
