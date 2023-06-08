'''
ATM program
'''

Username=input("Enter the UserName :")
Password=input("Enter the Password :")
Amount=1000
if Username=="Purushotham" and Password=="12345678":
    print("Welcome to Purushotham Bank")
    opr=input("Enter the operator :")
    if opr=='credit':
        credit=int(input("Enter the credit amount :"))
        print(Amount+credit,"credited")
        print("Thank you")
    elif opr=='debit':
        debit=int(input("Enter the debit amount :"))
        print(Amount-debit,"balance")
        print("Thank you")
    elif opr=='balance':
        print("Balance amount",Amount)
        print("Thank you")
    elif opr=='Ministatement':
        ministatements=int(input("how many months of ministatemnets :"))
        print(ministatements,Amount)
        print("Thank you")
    else :
        print("Enter wrong operator ")
        print("Thank you")
else:
    print("Enter wrong username and password")