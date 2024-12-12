# 1 Задание
import re

vhod = "нннцыцнчНННинниыннННННННННнннннннННрцври"

arr = re.findall('[н]+',vhod)
mxn = arr[arr.index(max(arr, key=len))]
string_replaced = vhod.replace(mxn, '!'*len(mxn))

print(len(mxn))
print(string_replaced)

# 2 Задание
vh = "shkbewfj(lkjlknewdkkdhc)czyyfvwl;qm[ dd]"

i1 = vh.find("(")
i2 = vh.find(")")
print( vh[1+vh.find("("):vh.find(")")])

# 3 Задание
v = "РааРАроаломиряоаялоПЫЯроАпрмАрсАмярмя"
# print(re.findall(r'\bа[\w]*я\b', v))
res = re.findall(r'[аА][а-яА-Я]*?[яЯ]', v)
print(res)