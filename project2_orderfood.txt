#Pyton Project To Order Food And Manage Bill.

choice=0
total_sum=0

while(choice<=7):
  print("MENU")
  print("1.Upma")
  print("2.Poha")
  print("3.Edli Sambhar")
  print("4.Vada Pav")
  print("5.Samosa")
  print("-----------------------")

  name=input("select your choice NO.")
  name=int(name)
  print("-----------------------")

  if name==1:
    print("Upma")
    print("prize 30rs")
    total_sum=total_sum+30
    print("-----------------------")

  elif name==2:
    print("Poha")
    print("prize 25rs")
    total_sum = total_sum + 25
    print("-----------------------")
  elif name==3:
    print("Edli Sambhar")
    print("prize 40rs")
    total_sum = total_sum + 40
    print("-----------------------")
  elif name==4:
    print("Vada Pav")
    print("prize 20rs")
    total_sum = total_sum + 20
    print("-----------------------")
  elif name==5:
    print("Samosa")
    print("prize 20rs")
    total_sum = total_sum + 20

    print("-----------------------")
  else:
    print("Invalid")

  print("Bill is",total_sum)

  name=input("select your choice NO.")



