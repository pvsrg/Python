class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix
        if min(sz := [len(rw) for rw in self.matrix]) != max(sz):
            raise Exception("Ошибка !!! Размерность строк матрицы должна быть одинакова")

    def __str__(self):
        return "\n".join("".join(map(lambda elm: f"{elm:>10.2f}", rw)) for rw in self.matrix)

    def __add__(self, other):
        return Matrix([[self.matrix[j][i] + other.matrix[j][i] for i in
            range(min(len(self.matrix[j]), len(other.matrix[j])))] + self.matrix[j][len(other.matrix[j]):len(self.matrix[j])] + other.matrix[j][len(self.matrix[j]):len(other.matrix[j])]
            for j in range(min(len(self.matrix), len(other.matrix)))] +
            [rw + [0 for _ in range(len(self.matrix[0]), len(other.matrix[0]))] for rw in self.matrix[len(other.matrix):]] +
            [rw + [0 for _ in range(len(other.matrix[0]), len(self.matrix[0]))] for rw in other.matrix[len(self.matrix):]])


try:
    my_matrix1 = Matrix([[1, 2, 3, 4], [4, 5, 6, 7]])
    my_matrix2 = Matrix([[1, 2], [3, 4], [55, 56], [71, 72]])
    print(my_matrix1 + my_matrix2)
except Exception as er:
    print(er)

