#Задание 1

class Matrix:
  
  def __init__(self, matr_1, matr_2):
    self.matr_1 = matr_1
    self.matr_2 = matr_2
    self.matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  def __add__(self):
    for el in range(len(self.matr_1)):
      for i in range (len(self.matr_2)):
        self.matrix[el][i] = self.matr_1[el][i] + self.matr_2[el][i]

    return str('\n'.join(['\t'.join([str(i) for i in el]) for el in self.matrix]))

  def __str__(self):
    return str('\n'.join(['\t'.join([str(i) for i in el]) for el in self.matrix]))


new_matrix = Matrix([[-6, 1, 0], [3, 4, 9], [6, 11, 10]],
                    [[-9, 7, 3], [5, 1, 6], [3, 11, 11]])


print(new_matrix.__add__())



# Задание 2

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    def get_full_textile(self):
        return f'Общий расход ткани {(self.param / 6.5 + 0.5) + (2 * self.param + 0.3)}  метра ткани'

    @abstractmethod
    def abstract(self):
        pass
#
class Coat(Clothes):
    def get_full_textile(self):
        return f'На пальто потребуется {self.param / 6.5 + 0.5 :.2f} метра ткани'

    def abstract(self):
        pass


class Suit(Clothes):
    def get_full_textile(self):
        return f'На костюм потребуется {2 * self.param + 0.3 :.2f} метра ткани'

    def abstract(self):
        pass

coat = Coat(44)
suit = Suit(1.67)


print(coat.get_full_textile())
print(suit.get_full_textile())

# Задание 3

class Cell:
  def __init__(self, quantity):
    self.quantity = int(quantity)

  def __add__(self, other):
    add = self.quantity + other.quantity
    return f'Две клетки объединились, и получилась клетка равная {add} ячейкам'

  def __sub__(self, other):
    sub = self.quantity - other.quantity
    if sub > 0:
      return f'Разность количества ячеек двух клеток равна {sub}'
    else:
      return 'Не получится вычесть, клетка не может быть меньше нуля ячеек'

  def __mul__(self, other):
    mul = self.quantity * other.quantity
    return f'Произведение количества ячеек двух клеток равно {mul}'


  def __truediv__(self, other):
    truediv = self.quantity // other.quantity
    return f'Деление количества ячеек двух клеток равно {truediv}'


  def make_order(self, line):
    result = ''
    for i in range(int(self.quantity / line)):
        result += '*' * line + '\n'
    result += '*' * (self.quantity % line) + '\n'
    return result


cell_1 = Cell(15)
cell_2 = Cell(7)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
print(cell_2.make_order(5))