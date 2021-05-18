#задание 1
name = input("Введите ваше имя: ")
lastname = input("Введите вашу фамилию: ")
age = int(input("Введите ваш возраст: "))
print(f"Добро пожаловать в систему {lastname} {name}, {age} лет")

#задание 2
seconds = int(input("Введите время в секундах: "))
hour = (seconds // 3600)
hour_ost = (seconds % 3600)
minute = (hour_ost // 60)
second = (hour_ost % 60)
print(f"Время {hour:02}:{minute:02}:{second:02}")

#задание 3
s1 = input("Введите число от 1 до 9: ")
a = int(s1)
b = int(s1 * 2)
c = int(s1 * 3)
sum = a + b + c
print(f"Сумма чисел равна {sum}")

#задание 4
a = int(input("Введите любое целое положительное число: "))
b = a % 10
a //= 10

while a > 0:
  if a % 10 > b:
    b = a % 10
  a //= 10
print(f"Наибольшая цифра в числе - {b}.")

#задание 5
revenue = int(input("Выручка за год составила: "))
costs = int(input("Издержки за год составили: "))
result = revenue - costs
if result > 0:
  print("За год у Вас положительный финансовый результат")
  rent = result / revenue
  sotr = int(input("Сколько сотрудников работает в вашей компании? "))
  i = result / sotr
  print(f"Прибыль фирмы в расчете на одного сотрудника составит {i} рублей.")
else:
  print("За год у Вас отрицательный финансовый результат")

#задание 6
a = int(input("Сколько километров Вы пробежали сегодня: "))
b = int(input("Сколько километров Вы хотите пробегать: "))
i = 1
while a < b:
  a *= 1.1
  i += 1
print(f"На {i} день Вы достигнете результата - не менее {b} км.")
