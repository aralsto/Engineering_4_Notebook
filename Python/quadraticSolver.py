def calc(a,b,c):
    det = b**2 - 4*a*c
    if(det<0):
        return(None)
    else:
        return((((-b+det**(1/2.0))/(2*a)),((-b-det**(1/2.0))/(2*a))))

print("""Input three integers separated by commas like \"a,b,c\" to get the\n
roots of the polynomial defined by \"ax^2 + bx + c\".\n
Type \"quit\" to exit the program.""")

while(True):
    try:
        text = input()
        if(text == "quit"):
            break
        array = text.split(",")
        roots = calc(int(array[0]),int(array[1]),int(array[2]))
        if(roots == None):
            print("There are no real roots")
        else:
            print(round(roots[0],3),", ",round(roots[1],3))
    except:
        print("Invalid input.")
