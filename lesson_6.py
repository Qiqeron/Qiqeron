from random import randint, sample
# 5

m, n = randint(2, 10), randint(2, 10)
arr = list()
for i in range(m):
    brr = list()
    for j in range(n):
        brr.append(randint(-10, 10))
    arr.append(brr)
print(arr)
summi = {}
for i in arr:
    summi.update({sum(i):i})
print(f'максимальная сумма {max(summi.keys())} у строчки {summi.get(max(summi.keys()))}')
print(f'минимальная сумма {min(summi.keys())} у строчки {summi.get(min(summi.keys()))}')

# 6

m, n = randint(2, 10), randint(2, 10)
arr = list()
for i in range(n):
    brr = sample(range(-30, 30), m)
    arr.append(brr)
print(arr)
for i in arr:
    if i[i.index(min(i))] % 2 == 0:
        i[i.index(min(i))] = 0
    else:
        i[i.index(min(i))] = 1
print(arr)