"""list=[]
num=int(input())

for n in range(num):
    if n%2==0:
        list.append(n)
        print(sum(list))"""
import random
num=int(input())
dollar=random.randint(3,num)
f=(dollar/num)*100
print(round(f))