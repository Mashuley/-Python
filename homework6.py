#Задание 1

from time import sleep

class TrafficLight:
  __color = ['Красный', 'Жёлтый', 'Зелёный']

  def running(self):
    i = 0
    while i != 3:
      print(TrafficLight.__color[i])
      if i == 0:
        sleep(7)
      elif i == 1:
        sleep(2)
      elif i == 2:
        sleep(11)
      i += 1

t = TrafficLight()
t.running()


#Задание 2

class Road:

  def __init__(self, length, width):
    self._length = length
    self._width = width
    self.weight = 25
    self.thickness = 5

  def mass(self):
    mass = self._length * self._width * self.weight * self.thickness / 1000
    print(f'Для покрытия дорожного полотна потребуется {int(mass)} тонн асфальта')

quantity = Road(5000, 20)
quantity.mass()


#Задание 3

class Worker:

  def __init__(self, name, surname, position, wage, bonus):
    self.name = name
    self.surname = surname
    self.position = position
    self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

  def __init__(self, name, surname, position, wage, bonus):
    super().__init__(name, surname, position, wage, bonus)

  def get_full_name(self):
    return self.name + ' ' + self.surname

  def get_total_income(self):
    return self._income["wage"] + self._income["bonus"]

employee = Position('Мария', 'Гришанова', 'Кредитный аналитик', 55000, 20000)
print(f'Сотрудник {employee.get_full_name()} за месяц заработает {employee.get_total_income()}')


#Задание 4

class Car:

  def __init__ (self, speed, color, name, is_police):
    self.speed = speed
    self.color = color
    self.name = name
    self.is_police = is_police

  def go(self):
    return (f'{self.name} поехала.')

  def stop(self):
    return (f'{self.name} остановилась.')

  def turn_left(self):
    return (f'{self.name} повернула влево.')

  def turn_right(self):
    return (f'{self.name} повернула вправо.')

  def show_speed(self):
    return (f'{self.name} едет со скоростью {self.speed} км в час.')


class TownCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)

  def show_speed(self):
    if self.speed > 60:
      return f'{self.name} - ваша машина превышает скорость. Максимальная скорость - 60 км в час. Пожалуйста, снизьте скорость.'
    else:
      return f'{self.name} - продолжайте движение.'


class SportCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)


class WorkCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)

  def show_speed(self):
    if self.speed > 40:
      return f'{self.name} - ваша машина превышает скорость. Максимальная скорость - 60 км в час. Пожалуйста, снизьте скорость.'
    else:
      return f'{self.name} - продолжайте движение.'


class PoliceCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)



town = TownCar(20, 'blue', 'Mazda', False)
sport = SportCar(60, 'white', 'BMW', False)
work = WorkCar(130, 'white', 'Audi', False)
police = PoliceCar(120, 'black', 'Toyota', True)


print(town.go(), sport.go(), work.go(), police.go())
print(town.stop(), sport.stop(), work.stop(), police.stop())
print(town.turn_left(), sport.turn_left(), work.turn_right(), police.turn_right())
print(town.show_speed(), sport.show_speed(), work.show_speed(), police.show_speed())
print(town.is_police, sport.is_police, work.is_police, police.is_police)
print(f'{sport.name} это полицейская машина? Нет, полицейская машина это {police.name}.')
print(f'{police.name} это полицейская машина? Да {police.name} - это полицейская машина.')
print(f'{town.name} полицейская машина? - {town.is_police}')



#Задание 5

class Stationery:

  def __init__(self, title):
    self.title = title

  def draw(self):
    return f'Запуск отрисовки'

class Pen(Stationery):
  def draw(self):
    return f'{self.title} - поможет написать лекцию.'

class Pencil(Stationery):
  def draw(self):
    return f'{self.title} - поможет нарисовать любой рисунок.'

class Handle(Stationery):
  def draw(self):
    return f'{self.title} - поможет раскрасить любую раскраску.'



pen = Pen('Ручка Parker')
pencil = Pencil('Карандаш Koh-i-Noor')
handle = Handle('Маркер Faber-Castell')


print(pen.draw())
print(pencil.draw())
print(handle.draw())