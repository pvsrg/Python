class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        return self._length * self._width * 25 * 5 / 1000


my_road = Road(5000, 20)
print(f"Масса асфальта = {my_road.calc():10.3f} т")