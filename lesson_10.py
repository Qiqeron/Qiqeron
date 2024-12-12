
import pandas as pd
import numpy as np
import matplotlib as plt

#1
ppd1 = pd.Series([4.313, 4.338, 4.358, 4.378, 4.4, 4.425, 4.447, 4.468])
print(ppd1)
ppd2 = pd.Series(np.arange(0, 20, 2))
print(ppd2)
ppd3 = pd.Series({'Color': "one", 'Shyz': "Gg", 'Phizika': "interesnaya", 'Otel': "Trivago"})
print(ppd3)

#2
b=np.arange(-10,10,1)
lol1=pd.Series(b)
a={1:"Январь",2:"Февраль",3:"Март",4:"Апрель",5:"Май",6:"Июнь",7:"Июль",8:"Август",9:"Сентябрь",10:"Октябрь",11:"Ноябрь",12:"Декабрь"}
lol2=pd.Series(a)
lol=list(set(lol1))
lo=(list(set(lol2)))
print(list(set(lol+lo)))

#3
gender=pd.Series({0: 'female', 1: 'male', 2: 'male', 3: 'female', 4: 'female', 5: 'male',
              6: 'male', 7: 'male', 8: 'male', 9: 'female', 10: 'female', 11: 'female', 12: 'female',
              13: 'female', 14: 'male', 15: 'male', 16: 'male', 17: 'male', 18: 'male', 19: 'female',
              20: 'female', 21: 'female', 22: 'male', 23: 'male', 24: 'male', 25: 'male', 26: 'female',
              27: 'female', 28: 'male', 29: 'female', 30: 'male', 31: 'female', 32: 'female',
              33: 'male', 34: 'female'})
plt.bar(gender.value_counts().index, gender.value_counts().values, color=['pink', 'blue'])
plt.xlabel('Gender')
plt.ylabel('Amount')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#4
name={0: 'John Deo', 1: 'Max Ruin', 2: 'Arnold', 3: 'Krish Star', 4: 'John Mike',
            5: 'Alex John', 6: 'My John Rob', 7: 'Asruid', 8: 'Tes Qry', 9: 'Big John',
            10: 'Ronald', 11: 'Recky', 12: 'Kty', 13: 'Bigy', 14: 'Tade Row', 15: 'Gimmy',
            16: 'Tumyu', 17: 'Honny', 18: 'Tinny', 19: 'Jackly', 20: 'Babby John', 21: 'Reggid',
            22: 'Herod', 23: 'Tiddy Now', 24: 'Giff Tow', 25: 'Crelea', 26: 'Big Nose',
            27: 'Rojj Base', 28: 'Tess Played', 29: 'Reppy Red', 30: 'Marry Toeey',
            31: 'Binn Rott', 32: 'Kenn Rein', 33: 'Gain Toe', 34: 'Rows Noump'}
gender={0: 'female', 1: 'male', 2: 'male', 3: 'female', 4: 'female', 5: 'male',
              6: 'male', 7: 'male', 8: 'male', 9: 'female', 10: 'female', 11: 'female', 12: 'female',
              13: 'female', 14: 'male', 15: 'male', 16: 'male', 17: 'male', 18: 'male', 19: 'female',
              20: 'female', 21: 'female', 22: 'male', 23: 'male', 24: 'male', 25: 'male', 26: 'female',
              27: 'female', 28: 'male', 29: 'female', 30: 'male', 31: 'female', 32: 'female',
              33: 'male', 34: 'female'}
name=pd.DataFrame({"names":name.values(),
                  "id":name.keys()})
gender=pd.DataFrame({"names2":gender.values(),
                  "id":gender.keys()})
merge=pd.merge(name,gender,on="id")
merge2=name.insert(2,"names2",gender.names2)

#5
dt={'mark':{0: 75, 1: 85, 2: 55, 3: 60, 4: 60, 5: 55, 6: 78,
             7: 85, 8: 78, 9: 55, 10: 89, 11: 94, 12: 88, 13: 88, 14: 88, 15: 88, 16: 54, 17: 75,
             18: 18, 19: 65, 20: 69, 21: 55, 22: 79, 23: 78, 24: 88, 25: 79, 26: 81, 27: 86, 28: 55,
             29: 79, 30: 88, 31: 90, 32: 96, 33: 69, 34: 88}}
df=pd.DataFrame(dt)
plt.figure()
plt.plot(df.index,df["mark"])
plt.show()