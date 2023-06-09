'''
This the super market program 

'''
Name=input("Enter the Name :")
list='''
Rice  Rs 20/kg
oil   Rs 40/kg
boost Rs 50/kg
'''
k={"Rice":20,"oil":40,"boost":50}
user=int(input("for list of items press 1 :"))
if user==1:
    print(list)
    pr=int(input("if you want to buy press 1 or 2 for exit :"))
    if pr==1:
        item=str(input("Enter the item :"))
        quantity=int(input("Enter the quantity :"))
        opr=input("can i bill the items yes or no :")
        value=(k.get(item))
        price=value*quantity
        totalamount=price
        gstamount=totalamount*0.18
        finalamount=totalamount+gstamount
        if opr=='yes':
            print("===============================================Super Market=======================================")
            print(Name,"                                                                                  ",    "date")
            print("SLNO                                      items        Quantity                              Price")
            print("00","                                   ",item,"     ",quantity,'                     ', "RS",price)
            print("==================================================================================================")
            print("Total Amount""                                                                  " "Rs", totalamount)
            print("GST Amount(18%)","                                                                      ",gstamount)
            print("==================================================================================================")
            print("Final Amount                                                             "         "Rs",finalamount)
            print("====================================Thank you for Visting our super market========================")
        elif opr=='no':
            print("Thank you")
        else :
            print("please select yes or no ")
    elif pr==2:
        print("Thank you ")
    else:
        print("enter the wrong Number")
else :
    print("your are pressed wrong number ")
    print("Thank you visit again")