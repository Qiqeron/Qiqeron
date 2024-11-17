# Задание 1

import math
#Ввод
print("Введите координаты вида `x, y` (без кавычек) для каждой точки:")
X = (input("Координаты X").split(","))
Y = (input("Координаты Y").split(","))
Z = (input("Координаты Z").split(","))

#Процедура нахождения угла
def ugol(a):
  a = list(map(float, a))

  if a[0] == 0:
    return 90
  return round(math.atan(abs(a[1]/a[0])) * 180 / math.pi, 3)

marks = ["X", "Y", "Z"]
ugarr = []
ugarr.append(ugol(X))
ugarr.append(ugol(Y))
ugarr.append(ugol(Z))

#Вывод
print(f"Минимальный угол :{min(ugarr)} , для точки {marks[ugarr.index(min(ugarr))]}")


#Задание 2