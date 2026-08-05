from abc import ABC,abstractmethod
class Car(ABC):
	def __init__(self,status):
		self._engine_status = status

	@abstractmethod
	def start_engine(self):
		pass

	@abstractmethod
	def stop_engine(self):
		pass

class ElectricCar(Car):
	def __init__(self,status):
		super().__init__(status)

	def start_engine(self):
		print("Dvigatel yoqildi (Electric)")

	def stop_engine(self):
		print("Dvigatel to'xtatildi (Electric)")


class GasolineCar(Car):
	def __init__(self,status):
		super().__init__(status)

	def start_engine(self):
		print("Dvigatel yoqildi (Gasoline)")


	def stop_engine(self):
		print("Dvigatel to'xtatildi (Gasoline)")


if __name__ == "__main__":
	c1 = ElectricCar(True)
	c2 = GasolineCar(False)
	c1.start_engine()
	c1.stop_engine()
	c2.start_engine()
	c2.stop_engine()
