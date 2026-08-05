class Library:
	def __init__(self,id,name):
		self.id = id
		self.name = name
		self.books = {"Data Sciense": 2,"Python Basics": 3}
		self.members = {"Umar": "Data Sciense", "Vali": "Python Basics"}

	def getName(self):
		return self.name

	def addBook(self,title,quantity):
		if title in self.books:
			self.books[title] += quantity
		else:
			self.books[title] = quantity

	def lendBook(self,member,title):
		if title in self.books:
			if self.books[title] > 0:
				self.members[member] = title
				print(f"\n'{title}' kitobi {member}ga topshirildi")
				self.books[title] -= 1
			else:
				print(f"\n'{title}' kitob nusxalari qolmadi")
		else:
			print(f"\n'{title}' kitob kutubxonada yo'q")

	def returnBook(self,member,title):
		if member in self.members:
			self.books[title] += 1
			self.members.pop(member)
			print(f"\n{member} a'zodan '{title}' kitobi qabul qilindi!")
		else:
			print(f"\n{member} a'zo ro'yxatda mavjud emas!")

	def library_info(self):
		print(f"\n\n\t=== {self.getName()} ===")
		print("\t|-----------------------|")
		print("\t|    Kitob nomi   |Soni |")
		print("\t|-----------------------|")
		for x in self.books:
			print(f"\t|{x:17s}|{self.books[x]:2} ta|")
			print("\t|-----------------------|")


if __name__ == "__main__":
	lib = Library(1,"Central Library")
	lib.addBook("Python Basics",3)
	lib.addBook("Iroda tarbiyasi",8)
	lib.library_info()
	lib.lendBook("Ali","Python Basics")
	lib.lendBook("Azamat","Iroda tarbiyasi")
	lib.library_info()
	lib.returnBook("Ali","Python Basics")
	lib.library_info()

