n = 20

guess_no = 1
print("no. of guess is only 5 time")

while (guess_no <= 5):
    a = int(input("Guess the No. \n"))
    if a < 20:
        print(" You enter less no. plz enter greter no.")
    elif a > 20:
        print(" You enter greter no. plz enter less no.")
    else:
        print("Congratulations!Right guess you win \n")
        print(guess_no, "No. of guess you took to finish")
        break

    print(5 - guess_no, "No.of guesses left")
    guess_no = guess_no + 1

if guess_no > 5:
    print("you fail", "Game Over")