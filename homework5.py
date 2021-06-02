# Задание 1
my_list = []
while True:
  string = input("Введите данные: ")
  if string == '':
    print(my_list)
    break
  else:
    new_string = string + '\n'
    my_list.append(new_string)
    with open("1.txt", "w") as file_obj:
      file_obj.writelines(my_list)

# Задание 2
with open("2.txt", "r") as f_obj:
  str = f_obj.readlines()
  print(f'Количество строк в файле -{len(str)}')

  for index, value in enumerate(str):
    word = len(value.split())
    print(f'В {index + 1}-ой строке {word} слов')

# Задание 3
with open('3.txt', 'r', encoding='utf8') as my_file:
  salary = []
  name = []
  my_list = my_file.read().split('\n')
  for i in my_list:
    i = i.split()
    if float(i[1]) < 20000:
      name.append(i[0])
    salary.append(i[1])
  print(f'Оклад меньше 20 000 у следующих сотрудников: {name}, средний оклад у этих сотрудников - {sum(map(float, salary)) / len(salary)}')

# Задание 4
translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('4.txt', 'r', encoding='utf8') as file_obj:
  for el in file_obj:
    el = el.split(' ', 1)
    new_file.append(translate[el[0]] + ' ' + el[1])
    with open('4_new.txt', 'w', encoding='utf8') as file_obj:
      file_obj.writelines(new_file)

# Задание 5
str = input("Введите несколько чисел, разделенных пробелом: ")
with open("5.txt", "w") as file_obj:
  file_obj.writelines(str)
with open("5.txt", "r") as file_obj:
  str = file_obj.read()
s = 0
y = str.split()
int_str = 0
for el in y:
  int_str += int(el)
s += int_str
print(f'Сумма ваших чисел - {s}')

# Задание 6
with open("6.txt", "r", encoding='utf8') as file_obj:
    dict = {}
    key = 'empty'
    s = 0
    for line in file_obj:
        for el in line.split():
            b = el[:el.find('(')]
            if b.isalpha():
                if key != 'empty':
                    dict[key[:-1]] = s
                    s = 0
                key = el
            elif b != '':
                s += int(b)
                dict[key[:-1]] = s
    print(dict)

# Задание 7
import json

firms = {}
profit = {'average_profit': []}
i = 1
with open("7.txt", "r", encoding='utf8') as f_obj:
    for line in f_obj:
        name, prop, revenue, costs = line.split()
        value = int(revenue) - int(costs)

        firms[name] = value
        if value >= 0:
            profit['average_profit'].append(value)

profit['average_profit'] = sum(profit['average_profit']) / len(profit['average_profit'])
output = [firms, profit]
with open('output.json', 'w') as file:
    json.dump(output, file)
