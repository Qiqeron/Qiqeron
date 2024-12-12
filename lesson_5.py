# Задание 1

import math
#Ввод
print("Введите координаты вида `x, y` для каждой точки:")
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
ugarr.extend([ugol(X), ugol(Y), ugol(Z)])

#Вывод
print(f"Минимальный угол :{min(ugarr)} , для точки {marks[ugarr.index(min(ugarr))]}")


#Задание 2
def prost(n):
    if n <= 1:  
        return False
    for i in range(2,int(n**0.5)+1):  
        if n%i==0:
            return False
    return True
n=int(input("Input a number:"))
k=0
for i in range(n):
    if prost(i):
        if bin(i)[2:]==bin(i)[2:][::-1]:
            k+=1
            print(bin(i)[2:],i)
print(k)