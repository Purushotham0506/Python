'''
calculator  using  function 
'''
a=int(input("Enter the First Number : "))
b=int(input("Enter the second Number : "))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def modul(a,b):
    return a%b
def floor_div(a,b):
    return a//b
def power(a,b):
    return a**b
print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
print(modul(a,b))
print(floor_div(a,b))
print(power(a,b))

