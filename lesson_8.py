import re


#1
vh = input()
if re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', vh):
    print('private')
elif re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{5,6}', vh):
    print('Taxiii!!!')
else:
    print('Well... It`s not a taxi...')

#2
vv = input()
print(len(re.findall(r'\b[a-zA-Zа-яА-ЯёЁ]*[-]*[a-zA-Zа-яА-ЯёЁ+]+\b', vv)))

#3
a="Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю."
for i in re.findall(r'((?:[01]\d|2[0-3])\:(?:[0-5]\d)(?:\:[0-5]\d)?)', a):
     a = a.replace(i, '(TBD)')
print(a)

#4
abba = input()
print(re.findall(r'[А-Я]{2,}(?: [А-Я]{2,})*"', abba))