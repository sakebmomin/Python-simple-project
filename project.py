
choice=0
tot_sum=0

a=("1.Smart Watch","2.Bluetooth Speaker","3.Mobile","4.Payment")
stock1=1
stock2=1
stock3=1
stock4=1


for i in a:
    print(i)

print("-----------------------------")


while(stock1<=10):
     name = int(input("select your choice NO."))
     print("------------------------------------------------------------------------")
     if name == 1:
         print("Brand Name                Prize                  Available Stock")
         print("-----------------------------------------------------------------------")
         bnm=("1.Mi                      3000rs                   10 Peace Available",
              "2.Noise                   2000rs                   11 Peace Available",
              "3.HONOR                   3500rs                   12 Peace Available",
              "4.Samsung                 2500rs                   5 Peace Available")

         for brand in bnm:
             print(brand)
         print("-----------------------------------------------------------------------")
         brand=int(input("Select Your Brand Choice:"))
         if brand  == 1:
          print("YOU ORDERD:","'Mi'",3000,"rs")

          tot_sum=tot_sum+3000
          print("Your Bill is",tot_sum)
          print("-----------------------------")
          print(10 - stock1, "Peace is left out of",10)
          stock1 = stock1 + 1
          print("-----------------------------")

         elif brand == 2:
           print("YOU ORDERD:","'Noise'",2000,"rs")
           tot_sum = tot_sum + 2000
           print("Your Bill is", tot_sum)
           print("-----------------------------")
           print(11 - stock2, "Peace is left out of", 11)
           stock2 = stock2 + 1
           print("-----------------------------")

         elif brand == 3:
           print("YOU ORDERD:","'HONOR'",3500,"rs")
           tot_sum = tot_sum + 3500
           print("Your Bill is", tot_sum)
           print("-----------------------------")
           print(12 - stock3, "Peace is left out of", 10)
           stock3 = stock3 + 1
           print("-----------------------------")

         elif brand == 4:
           print("YOU ORDERD:","'Samsung'",2500,"rs")
           tot_sum = tot_sum + 2500
           print("Your Bill is", tot_sum)
           print("-----------------------------")
           print(5 - stock4, "Peace is left out of", 10)
           stock4 = stock4 + 1

         print("-----------------------------")

     elif name == 2:
         print("Brand Name                Prize                  Available Stock")
         print("-----------------------------------------------------------------------")
         bbn = ("1.JBL                    8000rs                   20 Peace Available",
                "2.Bose                   7000rs                   25 Peace Available",
                "3.Anker                  9000rs                   10 Peace Available",
                "4.Sony                   10000rs                   7 Peace Available")

         for brand in bbn:
             print(brand)

         print("-----------------------------------------------------------------------")
         brand = int(input("Select Your Brand Choice:"))
         if brand == 1:
             print("YOU ORDERD:", "'JBL'",8000, "rs")

             tot_sum = tot_sum + 8000
             print("Your Bill is", tot_sum)
             print("-----------------------------")
             print(20 - stock1, "Peace is left out of", 20)
             stock1 = stock1 + 1
             print("-----------------------------")

         elif brand == 2:
             print("YOU ORDERD:", "'Bose'", 7000, "rs")

             tot_sum = tot_sum + 7000
             print("Your Bill is", tot_sum)
             print("-----------------------------")
             print(25 - stock2, "Peace is left out of", 25)
             stock2 = stock2 + 1
             print("-----------------------------")

         elif brand == 3:
             print("YOU ORDERD:", "'Anker'", 9000, "rs")

             tot_sum = tot_sum + 9000
             print("Your Bill is", tot_sum)
             print("-----------------------------")
             print(10 - stock3, "Peace is left out of", 10)
             stock3 = stock3 + 1
             print("-----------------------------")

         elif brand == 4:
             print("YOU ORDERD:", "'Sony'", 10000, "rs")

             tot_sum = tot_sum + 10000
             print("Your Bill is", tot_sum)
             print("-----------------------------")
             print(7 - stock3, "Peace is left out of", 7)
             stock3 = stock3 + 1
             print("-----------------------------")


     elif name == 3:
        print("Brand Name                Prize                  Available Stock")
        print("-----------------------------------------------------------------------")
        mbn = ("1.iphone13                 28000rs                   11 Peace Available",
               "2.Redmi Note 9             17000rs                   50 Peace Available",
               "3.Samsung                  19000rs                   20 Peace Available",
               "4.Realme                   10000rs                   15 Peace Available")

        for brand in mbn:
            print(brand)

        print("-----------------------------------------------------------------------")
        brand = int(input("Select Your Brand Choice:"))

        if brand == 1:
                 print("YOU ORDERD:", "'iphone13'", 28000, "rs")

                 tot_sum = tot_sum + 28000
                 print("Your Bill is", tot_sum)
                 print("-----------------------------")
                 print(11 - stock1, "Peace is left out of", 11)
                 stock1 = stock1 + 1
                 print("-----------------------------")

        elif brand==2:
                 print("YOU ORDERD:", "'Redmi Note 9'", 17000, "rs")

                 tot_sum = tot_sum + 17000
                 print("Your Bill is", tot_sum)
                 print("-----------------------------")
                 print(50 - stock2, "Peace is left out of", 50)
                 stock2 = stock2 + 1
                 print("-----------------------------")

        elif brand==3:
                 print("YOU ORDERD:", "'Samsung'", 19000, "rs")

                 tot_sum = tot_sum + 19000
                 print("Your Bill is", tot_sum)
                 print("-----------------------------")
                 print(20 - stock3, "Peace is left out of", 20)
                 stock3 = stock3 + 1
                 print("-----------------------------")

        elif brand==4:
                 print("YOU ORDERD:", "'Realme'", 10000, "rs")

                 tot_sum = tot_sum + 10000
                 print("Your Bill is", tot_sum)
                 print("-----------------------------")
                 print(15 - stock4, "Peace is left out of", 15)
                 stock4 = stock4 + 1
                 print("-----------------------------")

     if name==4:
         print("YOUR BILL TOTAL IS",tot_sum,"rs")

         print("-----------------------------")





