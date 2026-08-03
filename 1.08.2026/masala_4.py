class Email:
	def __init__(self,name = "Email"):
		self.name = name

	def send(self,message):
		print(f"{self.name} orqali yuborildi: {message}")

class SMS(Email):
	def __init__(self,name = "SMS"):
		self.name = name

	def send(self,message):
		super().send(message)

class Telegram(Email):
	def __init__(self,name = "Telegram"):
		self.name = name

	def send(self,message):
		super().send(message)

if __name__ == "__main__":
	message = input("Xabar kiriting: ")
	e = Email()
	s = SMS()
	t = Telegram()
	messengers = [e,s,t]

	for x in messengers:
		x.send(message)
