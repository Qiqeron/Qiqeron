import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Mall_Customers.csv")

print(df.groupby("Genre")["Annual Income (k$)"].mean())


print(df.groupby("Genre")["Spending Score (1-100)"].idxmax())

m=df[df['Genre']=='Male']
dt=m.groupby('Age')['Annual Income (k$)'].mean()
plt.plot(dt)
plt.xlabel("age")
plt.ylabel("Annual Income (k$)")
plt.show()


fig,ax=plt.subplots()
m=df[df['Genre']=='Male']
w=df[df['Genre']=='Female']
men=m.groupby('Annual Income (k$)')['Spending Score (1-100)'].mean()
wen=w.groupby('Annual Income (k$)')['Spending Score (1-100)'].mean()
men.plot.bar(color='blue')
wen.plot.bar(color='pink')
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.show()