#print no. in pyramid pattern
n=5

for i in range(1,n+1):  # no. of raws
    for j in range(1,i+1):  #no.of column
        print(j,end="")
    print()

#print * in pyramid pattarn
n=5

for i in range(0,n):
    for j in range(0,i+1):
        print("*",end='')
    print()

#swap no. using third veriable
a=2
b=5

temp = a
a = b
b = temp
print(" A:-"+str(a)+" B:-"+str(b))

#swap no. in python
a=2
b=5

a,b=b,a # using ROT_TWO


