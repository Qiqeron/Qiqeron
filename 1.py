#1 задание
import math
R = int(input("Введите значение радиуса в сантиметрах"))/100
print(f"Длина окружности: {round(2*math.pi*R, 3)} , площадь круга: {round(math.pi*R**2, 6)}")

#2 Задание
x, y = 10, 55
x, y = y, x
print(x, y)

#3 Задание
L = float(input("Введите значение длины в метрах"))
T = 2*math.pi*math.sqrt(L/9.81)
print(T)