class Cell:

    def __init__(self, number):
        self.number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if number < 0:
            self.__number = 0
        else:
            self.__number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number < other.number:
            print("Уменьшаемая клентка меньше вычитаемой")
        return Cell(self.number - other.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(round(self.number // other.number))

    def make_order(self, cells_row):
        return "\n".join(["*" * cells_row for _ in range(self.number // cells_row)]+["*" * (self.number % cells_row)])


my_cell1 = Cell(7)
my_cell2 = Cell(3)
print((my_cell1 + my_cell2).number)
print((my_cell1 - my_cell2).number)
print((my_cell1 * my_cell2).number)
print((my_cell1 / my_cell2).number)
print()
print(my_cell1.make_order(7))
print()
print(my_cell1.make_order(5))
print()
print(my_cell1.make_order(3))
