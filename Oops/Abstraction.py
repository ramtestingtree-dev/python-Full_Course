from abc import ABC, abstractmethod

class Vechile(ABC):
    @abstractmethod
    def wheels(self):
        pass

    @abstractmethod
    def brand(self):
        pass


class Car(Vechile):
    # def wheels(self):
    #     return 4
    def brand(self):
        return 'TATA'

car = Car()

print(car.brand())