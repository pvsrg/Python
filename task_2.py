from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.size = v

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, v):
        if v < 24:
            self.__size = 24
        elif v > 64:
            self.__size = 24
        else:
            self.__size = v

    def calc(self):
        return self.__size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.height = h

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h < 100:
            self.__height = 100
        elif h > 200:
            self.__height = 200
        else:
            self.__height = h

    def calc(self):
        return 2 * self.__height + 0.3


my_coat = Coat(15)
print(f"Расход ткани на пальто {my_coat.size:2} размера составит {my_coat.calc():.2f} м2")

my_suit = Suit(186)
print(f"Расход ткани на костюм {my_suit.height:2} роста составит {my_suit.calc():.2f} м2")
