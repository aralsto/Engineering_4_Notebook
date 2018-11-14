# Engineering 4 Notebook
This is where all my stuff will go.

## Assignments
This is where all of my assignments I do for the year will be documented.

### Dice Roller
This assignment was to creat a program in Python that randomly "rolled a die" when the user requested it. I decided to have the user input two integers in the form "a,b"
and output "a" number of "b" sided dice. Each dice roll was simply a random number ranging from 1 to "b." A couple other things to note: this program, as well as most all of
the ones following it, will exit when the user enters the phrase "quit." Secondly, pretty much whenever I accept input I put it in a try-except block so that I don't have to worry
about checking that the user's input is valid. If it's invalid, it will throw an error and be caught in the try-except block. This is a pretty poor practice, but for simple
programs like these it's far easier to just assume that errors are caused by user input and treat them as such. Here is my (code)[https://github.com/aralsto/Engineering_4_Notebook/Python/diceRoller.py]
