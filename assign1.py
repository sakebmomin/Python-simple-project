# Write a python program which accept two numbers and print max and min between them.
#==============================================================================================
'''a=int(input("enter a no."))
b=int(input("enter a no."))

if a>b:
     print(a," is maximum")
     print(b," is minimum")
elif b>a:
     print(b," is maximum")
     print(a," is minimum")
else:
   print("equal")'''

#======================================================================================================
# Write a python program which accept three numbers and print max and min between them.
#==============================================================================================
'''a=int(input("enter a no."))
b=int(input("enter a no."))
c=int(input("enter a no."))

if a>b>c:
     print(a," is maximum")
     print(b," is minimum")
     print(c," is minimum")
elif b>a>c:
     print(b," is maximum")
     print(a," is minimum")
     print(c," is minimum")
elif c>b>a:
     print(c," is maximum")
     print(b," is minimum")
     print(a," is minimum")
else:
   print("equal")'''

#===============================================================================================
'''a=int(input("enter a no."))
b=int(input("enter a no."))
c=int(input("enter a no."))

if a>b and a>c:
     larg=a
elif b>a and a>c:
     larg=b
else:
   larg=c

print("the maximum no.",larg)'''
#==============================================================================================

#Write a python program find the given character is an uppercase letter or lowercase letter or a digit or a special character.


a=input("Enter the character")

if a>='0' and a<='9':
     print("Digit")
elif a.isupper():
     print("Upper case")
elif a.islower():
     print("Lower case")
else:
   print("Spacial character")  
