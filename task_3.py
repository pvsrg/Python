class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus=0):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


empl_1 = Position("Иван", "Иванов", "прораб", 12000.0, 4000.0)
print(f"{empl_1.get_full_name()} {empl_1.get_total_income()}")

empl_2 = Position("Петр", "Петров", "штукатур", 8000.0)
print(f"{empl_2.get_full_name()} {empl_2.get_total_income()}")
