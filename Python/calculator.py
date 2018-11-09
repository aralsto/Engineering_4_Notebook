opDict = {0:"Addition: ",1:"Subtraction: ",2:"Multiplication: ",
          3:"Dividion: ",4:"Remainder: "}

def calc(a,b,c):
    if(c == 0):
        return a+b
    if(c == 1):
        return a-b
    if(c == 2):
        return a*b
    if(c == 3):
        return round(a/b,2)
    if(c == 4):
        return a%b

print("""Input two integers separated by a comma like \"x,y\"\n
to perform some operations on them. Type \"quit\" to exit the program.""")

while(True):
    try:
        text = input()
        if(text == "quit"):
            break
        array = text.split(",")
        for i in range(0,5):
            print(opDict[i],calc(int(array[0]),int(array[1]),i))
    except:
        print("Invalid input.")
