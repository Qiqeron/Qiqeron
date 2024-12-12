import matplotlib.pyplot as plt
import numpy as np
def f(x,a,b):
    return 1+(a**b)/(x**b)
x=np.linspace(-10,0,100)
fig,ax=plt.subplots()
a,b=1,1
ax.plot(x,f(x,a,b),label='a=1 b=1',color='blue')
a,b=2,1
ax.plot(x,f(x,a,b),label='a=2 b=1',color='green')
a,b=1,2
ax.plot(x,f(x,a,b),label='a=1 b=2',color='red')
x=np.linspace(0,10,100)
a,b=1,1
ax.plot(x,f(x,a,b),label='a=1 b=1',color='blue')
a,b=2,1
ax.plot(x,f(x,a,b),label='a=2 b=1',color='green')
a,b=1,2
ax.plot(x,f(x,a,b),label='a=1 b=2',color='red')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Функция f(x)=(x**b+a**b)/(x**b)')
ax.legend()
ax.grid(True)
plt.savefig('1funct.svg')
plt.show()


#2
fig,ax=plt.subplots()
x=np.linspace(0,10,100)
a,b=1,1
ax.plot(x,f(x,a,b),label='a=1 b=1',color='blue')
a,b=2,1
ax.plot(x,f(x,a,b),label='a=2 b=1',color='green')
a,b=1,2
ax.plot(x,f(x,a,b),label='a=1 b=2',color='red')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Функция f(x)=(x**b+a**b)/(x**b)')
ax.legend()
ax.grid(True)
n1=fig.add_axes([0.15,0.55,0.3,0.3])
x=np.linspace(0,0.1,100)
a,b=1,1
n1.plot(x,f(x,a,b),label='a=1 b=1',color='blue')
a,b=2,1
n1.plot(x,f(x,a,b),label='a=2 b=1',color='green')
a,b=1,2
n1.plot(x,f(x,a,b),label='a=1 b=2',color='red')
n1.set_title("малые х")
n1.grid(True)
n2=fig.add_axes([0.6,0.2,0.3,0.3])
x=np.linspace(10000,100000,100)
a,b=1,1
n2.plot(x,f(x,a,b),label='a=1 b=1',color='blue')
a,b=2,1
n2.plot(x,f(x,a,b),label='a=2 b=1',color='green')
a,b=1,2
n2.plot(x,f(x,a,b),label='a=1 b=2',color='red')
n2.set_title("большие х")
n2.grid(True)
plt.savefig('2funct.svg')
plt.show()

#3
fig,ax=plt.subplots()
x=np.linspace(-10,0,100)
a,b=1,1
ax.plot(x,f(x,a,b),label='a=1 b=1',color='blue')
a,b=2,1
ax.plot(x,f(x,a,b),label='a=2 b=1',color='green')
a,b=1,2
ax.plot(x,f(x,a,b),label='a=1 b=2',color='red')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Функция f(x)=(x**b+a**b)/(x**b)')
ax.legend()
ax.grid(True)
n1=fig.add_axes([0.2,0.35,0.3,0.3])
x=np.linspace(0,-1000,100)
a,b=1,1
n1.plot(x,f(x,a,b),label='a=1 b=1',color='blue')
a,b=2,1
n1.plot(x,f(x,a,b),label='a=2 b=1',color='green')
a,b=1,2
n1.plot(x,f(x,a,b),label='a=1 b=2',color='red')
n1.set_title("малые х")
n1.grid(True)
plt.savefig('3funct.svg')
plt.show()

#4
fig,ax=plt.subplots()
x=np.linspace(0,4,50)
a,b=1,1
ax.plot(x,f(x,a,b),label='a=1 b=1',color='blue')
a,b=2,1
ax.plot(x,f(x,a,b),label='a=2 b=1',color='green')
a,b=1,2
ax.plot(x,f(x,a,b),label='a=1 b=2',color='red')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Функция f(x)=(x**b+a**b)/(x**b)')
ax.plot(1,2,'ko',label='Точка(1,2)')
ax.legend()
ax.grid(True)
plt.savefig('4funct.svg')
plt.show()
fig,ax=plt.subplots(1,3, figsize=(18, 6))
x=np.linspace(0,10,100)
ax[0].plot(x,f(x,1,0),label='a=1 b=0',color='b')
ax[0].plot(x,f(x,1,-1),label='a=1 b=-1',color='r')
ax[0].plot(x,f(x,1,0.5),label='a=1 b=0.5',color='g')
ax[0].plot(x,f(x,1,0.8),label='a=1 b=0.8',color='black')
ax[1].plot(x,f(x,1,0),label='a=1 b=0',color='b')
ax[1].plot(x,f(x,1,-1),label='a=1 b=-1',color='r')
ax[1].plot(x,f(x,1,-0.5),label='a=1 b=-0.5',color='g')
ax[1].plot(x,f(x,1,-0.8),label='a=1 b=-0.8',color='black')
ax[2].plot(x,f(x,1,0),label='a=1 b=0',color='b')
ax[2].plot(x,f(x,1,-1),label='a=1 b=-1',color='r')
ax[2].plot(x,f(x,1,-1.5),label='a=1 b=-1.5',color='g')
ax[2].plot(x,f(x,1,-2.5),label='a=1 b=-2.5',color='black')
ax[0].set_xlabel('x')
ax[0].set_ylabel('f(x)')
ax[0].set_title('Функция f(x)=(x**b+a**b)/(x**b)')
ax[0].legend()
ax[0].grid(True)
ax[1].set_xlabel('x')
ax[1].set_ylabel('f(x)')
ax[1].set_title('Функция f(x)=(x**b+a**b)/(x**b)')
ax[1].legend()
ax[1].grid(True)
ax[2].set_xlabel('x')
ax[2].set_ylabel('f(x)')
ax[2].set_title('Функция f(x)=(x**b+a**b)/(x**b)')
ax[2].legend()
ax[2].grid(True)
plt.savefig('5funct.svg')
plt.show()