class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def __init__(self):
        super().__init__("Pen")

    def draw(self):
        print("Отрисовка ручкой.")


class Pencil(Stationery):

    def __init__(self):
        super().__init__("Pencil")

    def draw(self):
        print("Отрисовка карандашом.")


class Handle(Stationery):

    def __init__(self):
        super().__init__("Handle")

    def draw(self):
        print("Отрисовка маркером.")


my_pen = Pen()
my_pen.draw()

my_pencil = Pencil()
my_pencil.draw()

my_handle = Handle()
my_handle.draw()
