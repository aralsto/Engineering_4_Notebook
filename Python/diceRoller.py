#Dice Roller
import random

print("""Input two integers separated by a comma like \"x,y\"\n
to roll x number of y-sided dice. Type \"quit\" to exit the program.""")

while(True):
    try:
        text = input()
        if(text == "quit"):
            break
        array = text.split(",")
        for i in range(0,int(array[0])):
            print(random.randint(1,int(array[1])))
    except:
        print("Invalid input.")
