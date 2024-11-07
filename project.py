import random
target = random.randint(0,100)

while True:
    UserChoice = input("Guess the target Between 1 - 100 or Quit :")
    if(UserChoice == "Quit"):
        break
    UserChoice = int(UserChoice)
    if(UserChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(UserChoice < target):
        print("your number was too small. Take a bigger guess...")

    else:
        print("your number was too Big. Take a Smaller guess...")

print("-----GAME OVER-----")