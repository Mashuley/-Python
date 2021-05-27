#Задание 1
new_list = [2, 'word', 9.5, (1, 2, 3), [4, 5, 6], {7, 8, 9}]
for el in new_list:
  print (type(el))

#Задание 2
my_list = []
while True:
  el_list = input('Введите элемент списка, для завершения заполнения введите Stop:')
  if el_list.title() == 'Stop':
    break
  my_list.append(el_list)
j = 0
for i in range(int(len(my_list) // 2)):
  my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
  j += 2
print(my_list)

#Задание 3. Решение через list
month = int(input("Введите месяц от 1 до 12: "))
season = [[12, 1, 2, "зима"], [3, 4, 5, "весна"], [6, 7, 8, "лето"], [9, 10, 11, "осень"]]
x = 0
for el in season:
  if month in season[x]:
    print(f"Месяц номер {month} – это {season[x][3]}")
    break
  else:
    x += 1

#Решение через dict
month = int(input("Введите месяц от 1 до 12: "))
season = {"зима": (12, 1, 2), "весна": (3, 4, 5), "лето": (6, 7, 8), "осень": (9, 10, 11)}
for element in season.keys():
  if month in season [element]:
    print(f"Месяц номер {month} – это {element}")

#Задание 4
word = input("Введите несколько слов, разделенных пробелом: ")
for number, el in enumerate (word.split(), 1):
  if len(el) <= 10:
    print(f" {number}. {el}")
  else:
    print(f" {number}. {el [0:10]}")

#Задание 5
my_list = [7, 5, 3, 3, 2]
print(f"Начальный рейтинг - {my_list}")
rating = int(input("Введите любое число: "))
my_list.insert(0, rating)
my_list.sort(reverse=True)
print(f"Рейтинг после ввода цифры '{rating}' - {my_list}")
my_list.pop(5)


#Альтернативное решение с множеством значений
my_list = [7, 5, 3, 3, 2]
print(f"Начальный рейтинг - {my_list}")
while True:
  rating = int(input("Введите любое число, для завершения 111: "))
  if rating == 111:
    break
  my_list.insert(0, rating)
  my_list.sort(reverse=True)
  print(f"Рейтинг после ввода цифры '{rating}' - {my_list}")
  my_list.pop(5)
