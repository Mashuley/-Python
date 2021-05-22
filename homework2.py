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

