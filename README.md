# Engineering 4 Notebook
This is where all my stuff will go.

## Assignments
This is where all of my assignments I do for the year will be documented.

### Dice Roller
This assignment was to create a program in Python that randomly "rolled a die" when the user requested it. I decided to have the user input two integers in the form "a,b"
and output "a" number of "b" sided dice. Each dice roll was simply a random number ranging from 1 to "b." A couple other things to note: this program, as well as most all of
the ones following it, will exit when the user enters the phrase "quit." Secondly, pretty much whenever I accept input I put it in a try-except block so that I don't have to worry
about checking that the user's input is valid. If it's invalid, it will throw an error and be caught in the try-except block. This is a pretty poor practice, but for simple
programs like these it's far easier to just assume that errors are caused by user input and treat them as such. Here is my [code](https://github.com/aralsto/Engineering_4_Notebook/blob/master/Python/diceRoller.py).

### Calculator
This assignment was to create a program in Python that, when given two numbers "a" and "b," would return the results of the operations "a+b," "a-b," "a*b," "a/b," and "a%b." It was required that
a function return one operation at a time, and not print the result within the function. This meant calling the function 5 times with a different parameter each time, then printing that result after
each call. Other than that, there isn't much to say. The notes about exiting the program and excepting errors from my first assignment still stands, and from now on will not be mentioned (unless an
assignment does something differently in that regard). Here is my [code](https://github.com/aralsto/Engineering_4_Notebook/blob/master/Python/calculator.py).

### Quadratic Solver
This assignment was to create a program in Python that when given the coefficients to a polynomial (ax^2 + bx + c, where "a," "b," and "c" are the coefficients) would return the real roots if they existed. This was
done by first taking the determinant of the quadratic (b^2 - 4ac) and performing the quadratic formula if it is positive. Otherwise the user recieves a message telling them that no real roots exist. There is not much
else to say about this assignment, so here is my [code](https://github.com/aralsto/Engineering_4_Notebook/blob/master/Python/quadraticSolver.py).

### Strings and Loops
This assignment was to create a program in Python that would spit back whatever input the user gave it letter by letter, split on spaces. I split the input on spaces, giving me a list of strings. For every element
of the list, I used the list() command on that element. That split the strings into lists of single characters, which I then printed in a for loop. After printing out the letters of a word, I printed three dashes
if it was not the last word in the overall list. Here is my [code](https://github.com/aralsto/Engineering_4_Notebook/blob/master/Python/stringsAndLoops.py).

### GPIO Pins - Bash
This assignment was to blink two LEDs 10 times with the GPIO pins on the Pi using a bash script. I soldered male connectors to the Pi and hooked it up to a t-cobbler using a ribbon connector. From there, all I had to do
was wire up two LEDs like normal (the only issue being the different numbering of the pins in the bash script and on the t-cobbler) and write the simple script. Here is my [code](https://github.com/aralsto/Engineering_4_Notebook/blob/master/Scripts/gpioLED.sh)
and a useful [website](https://projects.drogon.net/raspberry-pi/wiringpi/pins/) with pin diagrams to use for the bash scripts. This becomes unneccessary in Python with the GPIO.setmode() function.
