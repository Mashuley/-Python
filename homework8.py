# Задание 1

from datetime import date


class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def type(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return 'Неверная дата'

    @staticmethod
    def valid(data):
        try:
            day, month, year = data.split('-')
            date(int(year), int(month), int(day))
            return 'Все верно'
        except ValueError:
            return 'Неверная дата'


print(Data.valid('11-06-2021'))
print(Data.type('11-06'))

# Задание 2

class DivisionByZero(Exception):
  def __init__(self, text):
    self.text = text

try:
    divisible = int(input('Введите делимое: '))
    divisor = int(input('Введите делитель: '))
    if not divisor:
        raise DivisionByZero('На ноль делить нельзя')
    print(f'Результат деления - {divisible / divisor}')

except ValueError:
    print('Это не число')
except DivisionByZero as error:
    print(error)

# Задание 3

class MyError(Exception):
    def __init__(self):
        pass

class TypeCheck:
    def __init__(self):
        self.new_list = []

    def check_value(self):
        global user_val
        while True:
            try:
                try:
                    user_val = int(input('Введите любое число: '))
                    ex = input(f'Ваше число добавлено в список. Хотите продолжить? да/нет: ').lower()
                    self.new_list.append(user_val)
                    if ex == 'нет':
                        print(f'Список добавленных вами чисел - {self.new_list}')
                        break
                except ValueError:
                    raise MyError
            except MyError:
                ex = input(f"Вы ввели не число! Хотите продолжить? да/нет: ").lower()
                if ex == 'нет':
                    print(f'Список добавленных вами чисел - {self.new_list}')
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()

# Задание 4, 5, 6

class FixedAssets:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Наименование устройства': self.name, 'Цена за единицу': self.price, 'Количество': self.quantity}

    def income(self):
        try:
            name = input(f'Введите наименование: ')
            price = int(input(f'Введите цену за единицу: '))
            quantity = int(input(f'Введите количество: '))
            item = {'Наименование устройства': name, 'Цена за единицу': price, 'Количество': quantity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Недопустимое значение.')


class Printer(FixedAssets):
    pass


class Scanner(FixedAssets):
    pass


class Xerox(FixedAssets):
    pass


p = Printer('Canon', 1000, 3)
s = Scanner('Cipherlab', 2000, 1)
x = Xerox('Xerox', 3000, 5)
p.income()
s.income()
x.income()


# Задание 7

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if self.b + other.b < 0:
            return f'Сумма равна: {self.a + other.a}{self.b + other.b}i'
        else:
            return f'Сумма равна: {self.a + other.a}+{self.b + other.b}i'

    def __mul__(self, other):
        if (self.a * other.b) + (self.b * other.a) < 0:
            return f'Произведение равно: {(self.a * other.a) - (self.b * other.b)}{(self.a * other.b) + (self.b * other.a)}i'
        else:
            return f'Произведение равно: {(self.a * other.a) - (self.b * other.b)}+{(self.a * other.b) + (self.b * other.a)}i'

c1 = ComplexNumber(5, -6)
c2 = ComplexNumber(3, 2)
print(c1 + c2)
print(c1 * c2)