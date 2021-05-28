# Задание 1
from sys import argv

def wages(hours_prod, rate_per_hour, bonus):
  return hours_prod * rate_per_hour + bonus

wages_calc, hours_prod, rate_per_hour, bonus = argv

print("Имя скрипта: ", wages_calc)
print("Выработка в часах: ", hours_prod)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", bonus)
print("Зарплата: ", wages(int(hours_prod), int(rate_per_hour), int(bonus)))

#Задание 2
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in my_list[1:] if el > my_list[my_list.index(el)-1]]
my_list.pop(0)
print(new_list)

#Задание 3
print (f'Числа от 20 до 240, кратные 20 или 21 - это {", ".join(map(str, [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]))}')


#Задание 4
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)


#Задание 5
from functools import reduce

def my_func(el1, el2):
  return el1 + el2
print(reduce(my_func, [el for el in range(100, 1001, 2)]))


#Задание 6
#итератор, генерирующий целые числа, начиная с указанного
from itertools import count
for el in count(3):
  if el > 10:
    break
  else:
    print(el)


#итератор, повторяющий элементы некоторого списка, определённого заранее
from itertools import cycle
с = 0
for el in cycle("123"):
  if с > 14:
    break
  print(el)
  с += 1


#Задание 7
def fact(n):
  a = 1
  for el in range(1, n+1):
    a *= el
    yield a

n = int(input("Введите число, от которого нужно найти факториал: "))
for el in fact(n):
  print(el)
