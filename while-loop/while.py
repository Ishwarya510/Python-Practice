num=int(input())
factorial=1
if num<0:
     print("factorial does not exist")
elif num==0:
     print(1) 
else:         
     for i in range(1,num+1):
              factorial=factorial*i
print(factorial)





"""a,b,c=str(input()),str(input()),
if noise=="lion":
    print("Grr ",end="")
elif noise=="Tigers":
     print("Rawr ",end="")  
elif noise=="Snakes":
     print("Ssss ",end="")  
elif noise=="Birds":
     print("Chirp ",end="")       """

"""num=7
fact=1
for i in range(1,num+1):
    fact=fact*i
    print(fact)"""