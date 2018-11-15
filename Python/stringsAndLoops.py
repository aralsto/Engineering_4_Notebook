#Strings and Loops

print("""Input a string to get it back letter by letter, split on spaces.
input \"q\" to exit the program.""")

while(True):
    text = input()
    if(text == "q"):
        break
    array = text.split()
    for i in range (0, len(array)):
        wArray = list(array[i])
        for j in range (0, len(wArray)):
            print(wArray[j])
        if(i != len(array)-1):
            print("---")
