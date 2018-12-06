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

### GPIO Pins - Python
This was exactly the same as the last assignment, but in python. The only thing to note is that I used GPIO.setmode(BCM) in order to get the pin numbers to match up with the t-cobbler. Here is my [code](https://github.com/aralsto/Engineering_4_Notebook/blob/master/Python/gpioLED_Python.py)

### Hello Flask
This assignment was to create a flask app that spits out "Hello world!" when you access it from another computer. It was pretty straight forward, here is my [code](https://github.com/aralsto/Engineering_4_Notebook/blob/master/Python/Flask/hello_world/app.py).

### GPIO Pins - Flask
This assignment was to create a flask app that allowed you to control the two LEDs that were set up in the GPIO Pins - Bash and GPIO Pins - Python assignments. The challenge was working with HTML, which I hadn't
had much experience with previously. I got two buttons on the website controlling the LEDs pretty fast, then it took me another period or so to figure out how to have the background color of the webpage reflect what LEDs
were on or off. Here is my [code for the app](https://github.com/aralsto/Engineering_4_Notebook/blob/master/Python/Flask/flask_gpio/app.py) and here is my [html](https://github.com/aralsto/Engineering_4_Notebook/blob/master/Python/Flask/flask_gpio/templates/index.html).

### GPIO Pins - I2C
This assignment was to set up an LSM303 accelerometer and an SSD1306 OLED screen and display the accelerometer data on the screen. I had to solder pins to both devices, as well as download libraries for them. There was
example code in the libraries, so from there it was very easy to get them doing what I needed. There isn't too much else to say, so here is my [code](https://github.com/aralsto/Engineering_4_Notebook/blob/master/Python/GPIO_I2C.py).
