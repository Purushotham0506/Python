'''
__init__()
calulator witn __init__()
'''

class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return (self.a+self.b)
    def sub(self):
        return (self.a-self.b)
    def Muli(self):
        return (self.a*self.b)
    def div(self):
        return (self.a/self.b)
    def floor_div(self):
        return (self.a//self.b)
    def Modulus(self):
        return (self.a%self.b)
    def power(self):
        return (self.a**self.b)
a=int(input())
b=int(input())
obj=cal(a,b)
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor division")
    print("6. Modulus")
    print("7. Power")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",obj.add())
    elif choice==2:
        print("Result: ",obj.sub())
    elif choice==3:
        print("Result: ",obj.Muli())
    elif choice==4:
        print("Result: ",round(obj.div(),2))
    elif choice==5:
        print("Result: ",obj.floor_div())
    elif choice==6:
        print("Result: ",obj.Modulus())
    elif choice==7:
        print("Result: ",obj.power())
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!") 
        
print()


