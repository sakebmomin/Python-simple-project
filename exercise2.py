print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Exponential")


num1=int(input("Enter first no. "))
num2=int(input("Enter Secound no. "))

choice=int(input("Enter your choice No. "))

if num1==56 and num2==9 and choice==1:
    print(77)
elif num1==45 and num2==3 and choice==3:
    print(555)
elif num1==56 and num2==6 and choice==4:
    print(4)
elif choice==1:
    print("Addition is",num1+num2)
elif choice==2:
    print("Substraction is",num1-num2)
elif choice==3:
    print("Multiplication is",num1*num2)
elif choice==4:
    print("Division is",num1//num2)
elif choice==5:
    print("Exponential is",num1**num2)
else:
    print("wrong choice...try again")