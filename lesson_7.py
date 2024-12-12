import os

# 1
def read_last(lines,file):
   if not isinstance(lines,int) or lines<=0:
       return("Ошибка в количестве строк")
   p=open(file,encoding="utf-8")
   p1=p.readlines()
   for i in range(lines):
       print(p1[i].replace("\n",""))

# 2
def print_docs(directory):
       
       for root, dirs, files in os.walk(directory):
            print("Содержимое папки:", root)
            for dir_name in dirs:
                print(f"  Подпапка: {dir_name}")
            for file_name in files:
                print(f"  Файл: {file_name}")
print_docs(r"C:\Users\Asus\OneDrive\Documents")

# 3
def longest_words(file):
       b=[]
       p=open(file,encoding="utf-8")
       p1=p.read()
       s=p1.split()
       a=max(len(i) for i in s)
       for i in s:
               if len(i)==a:
                       b.append(i)
       return b

# 4
fname = (input("Input newfile`s name: "))+".txt"
f=open(fname,"w",encoding="utf-8")
while True:
        a=input()
        if not a:
                break
        f.write(a+"\n")
f.close()