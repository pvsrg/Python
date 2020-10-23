class MyComplex:
    def __init__(self, rl, im):
        self.rl = rl
        self.im = im

    def __add__(self, other):
        return MyComplex(self.rl + other.rl, self.im + other.im)

    def __mul__(self, other):
        return MyComplex(self.rl * other.rl - self.im * other.im, self.rl * other.im + other.rl * self.im)

    def __str__(self):
        return f"{self.rl} + i*{self.im}"


a = MyComplex(2.5, 10.0)
b = MyComplex(5.2, 1.0)
print(a + b)
print(a * b)

