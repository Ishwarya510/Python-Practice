def factorial(num):
    if num==1:
        print(num)
    else:
        print(num*factorial(num-1))
factorial(5)