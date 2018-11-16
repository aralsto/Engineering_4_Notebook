#Man-Shaped Pinata
import sys
men = {
1:"""
 -----
 |   |
 |   
 |
 |
 |
 |
----------
""",
2:"""
 -----
 |   |
 |   O
 |
 |
 |
 |
----------
""",
3:"""
 -----
 |   |
 |   O
 |   |
 |
 |
 |
----------
""",
4:"""
 -----
 |   |
 |   O
 |  /|
 |
 |
 |
----------
""",
5:"""
 -----
 |   |
 |   O
 |  /|\\
 |   |
 |
 |
----------
""",
6:"""
 -----
 |   |
 |   O
 |  /|\\
 |   |
 |  /
 |
----------
""",
7:"""
 -----
 |   |
 |   O
 |  /|\\
 |   |
 |  / \\
 |
----------
"""}

print("\n" * 100)
print("""Enter a word to initiate the game. Enter \"q\" to exit the program.
While guessing, enter \"quit\" to exit the program.""")

while(True):
    text = input()
    if(text == "q"):
        sys.exit()
    word = list(text)
    length = len(word)
    
    guessed = []
    state = 1
    health = 1
    
    print("\n" * 100)
    while(state == 1):
        print("\n" * 100, men[health], "Word: ", end = "")
        #printing censored word
        for i in range (0,length):
            if(word[i] in guessed):
                print(word[i], " ", end = "")
            else:
                print("_ ", end = "")
        print("\n")
        #end game conditions
        check = True
        for i in range (0,length):
            if(word[i] not in guessed):
                check = None
                break
        if(check):
            state = 2
            break
        if(health == 7):
            state = 0
            break
        #accept a guess,
        print("Guess: ", end = "")
        guess = input()
        if(guess == "quit"):
            sys.exit()
        #add guessed letter to list of guesses, check if it was correct
        if(guess not in guessed):
           guessed.append(guess)
           if(guess not in word):
               health += 1
        
    #win/lose conditions
    if(state == 0):
        print("You lost. Type in another word to play again.")
    if(state == 2):
        print("You won! Type in another word to play again.")
