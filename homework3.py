# Задание 1
def finc_div(a, b):
  try:
    div = a / b
    print(f'Результат деления - {div}')
  except ZeroDivisionError:
    print("На ноль делить нельзя")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
finc_div(a, b)

# Задание 2
def my_func(name, surname, year, city, email, phone):
  print(name, surname, year, city, email, phone)

my_func(name=input("Введите имя: "),
        surname=input("Введите фамилию: "),
        year = int(input("Введите год рождения: ")),
        city = input("Введите город проживания: "),
        email = input("Введите электронную почту: "),
        phone = input("Введите номер телефона: "))

# Задание 3
def return_sum(v1, v2, v3):
  x = [v1, v2, v3]
  x.sort()
  out = x[1] + x[2]
  return out

val1 = 10
val2 = 6
val3 = 30

out = return_sum(val1, val2, val3)
print(out)

# Задание 4
def my_func(x, y):
  return x ** y

print(my_func(10, -2))


def my_func(x, y):
  return 1 / pow(x, abs(y))

print(my_func(10, -2))



def my_func(a, b):
  c = -1
  result = 1
  while c >= b:
    result /= a
    c -= 1
  return result


a = int(input("Введите число, которое необходимо возвести в степень: "))
b = int(input("Введите отрицательное число - степень: "))
x = my_func(a, b)
print(x)


# Задание 5
s = 0
loop = True
while loop:
  str = input('Введите несколько цифр, разделенных пробелом. Для выхода Q: ')

  y = str.split()
  int_str = 0
  for el in y:
    if el == 'Q':
      loop = False
      break
    int_str += int(el)
  s += int_str
  print(s)


# Задание 6
def int_func(a):
  print(a.title())

int_func("text")

# Задание 7
def int_func(a):
  print(a.title())

a = input("Введите несколько слов, разделенных пробелом: ")
int_func(a)
