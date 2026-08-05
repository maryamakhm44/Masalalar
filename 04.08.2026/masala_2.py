class Student:
	def __init__(self):
		self.__first_name = None
		self.__last_name = None
		self.__age = None
		self.__student_id = None
		self.__course = 1


	def show_info(self):
		print("\t|---------------------------------------------|")
		print("\t| ID |First name|   Last name  | Age | Course |")
		print("\t|---------------------------------------------|")
		print(f"\t|{self.__student_id:4d}|{self.__first_name:10s}|{self.__last_name:14s}|{self.__age:5d}|{self.__course:8d}|")
		print("\t|---------------------------------------------|")

	def set_age(self,age):
		if age > 17 and age <= 30:
			self.__age = age

		else:
			print("Age value out of range")

	def set_full_name(self,fname,lname):
		self.__first_name = fname
		self.__last_name = lname

	def increase_course(self):
		if self.__course <= 3:
			self.__course += 1
			print("Kurs qo'shildi")
		else:
			print("Kurslar soni max limitga yetgan")

	def update_student_id(self,new_id):
		self.__student_id = new_id


if __name__ == "__main__":
	s = Student()
	s.set_full_name("Ali","Valiyev")
	s.set_age(24)
	s.increase_course()
	s.increase_course()
	s.increase_course()
	s.increase_course()
	s.update_student_id(1001)
	s.show_info()
