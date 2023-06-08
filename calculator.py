'''
Calculator Program in the Python 
'''
Num1=int(input("Enter the Number :"))
Num2=int(input("Enter the number :"))
opr=input("Enter the operator :")
if opr=='+':
    print(Num1+Num2)
elif opr=='-':
    print(Num1-Num2)
elif opr=='*':
    print(Num1*Num2)
elif opr=='/':
    print(Num1/Num2)
elif opr=='**':
    print(Num1**Num2)
elif opr=='%':
    print(Num1%Num2)
else:
    print("Enter wrong operator")