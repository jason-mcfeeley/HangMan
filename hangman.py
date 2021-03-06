# This is a file.
import random

def PlayHangman():
    '''Joint Effort between Jason, Jack and Mr. H, runs the entire game'''
    word = Get_Word()
    word_with_blanks = Create_word_with_blanks(word)
    end = 0
    guesses = []
    correct_guesses = []
    while (end == 0):
        print(' ')
        draw_man(guesses, correct_guesses)
        write_guesses(guesses)
        write_word_guess(word_with_blanks)
        print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")
        letter_guess = Ask_letter(guesses)
        word_with_blanks = update_word_with_blanks(word, word_with_blanks, letter_guess)
        guesses = update_guesses(guesses, letter_guess)
        correct_guesses = update_correct_guesses(letter_guess, word, correct_guesses)
        Right_or_wrong(letter_guess, word)
        end = Check_End(word_with_blanks, correct_guesses, guesses)
    print("The End")

def write_word_guess(word_with_blanks):
    x = len(word_with_blanks)
    print(x," letters")
    print(word_with_blanks)


    
def Get_Word():
    '''Chooses a random word from the list of words and returns it'''
    # Created by Jason
    words = ['dog','cat', 'wolf', 'fox', 'car', 'orange','window','case','bike','computer','table','poster','sign','zebra','zinc','countryside','parking','plant','chair','arm','ibex']
    return(random.choice(words))
                                                   
def Create_word_with_blanks(word):

    '''Takes the word and returns a string with all letters replaced by underscores  made by Jack '''
    n = len(word)
    return  n * '_'
         
def Ask_letter(guesses):
    '''asks the user for their guess and returns that guess, uses guesses to ensure they don't re-use a letter '''
    #Created by Jack
    guess=raw_input('Guess a letter: ')
    if guess in guesses:
        while guess in guesses:
            print"You already guessed that letter, guess again"
            guess = raw_input('Guess a letter')
    return guess

def update_word_with_blanks(word, word_with_blanks, letter_guess):
    '''takes the word, word with blanks and the letter guess and returns an updated version of the word_with_blanks '''
    #Jason and Jack Togetherrrrrrr
    if letter_guess in word:
        pos = word.find(letter_guess)
        wwblist = list(word_with_blanks)
        wwblist[pos] = letter_guess
        word_with_blanks = ''.join(wwblist)
        return word_with_blanks
    else:
        return word_with_blanks
    
    

def update_guesses(guesses, letter_guess):
    '''Takes the guessed letter and guesses  and updates the guesses string'''
    #made by Jason
    if letter_guess in guesses:
        return guesses
    else:
        guesses.append(letter_guess)
        return guesses

    
def update_correct_guesses(letter_guess, word, correct_guesses):
    '''takes the guessed letter and word and updates list of correct guesses'''
    #Made by Jason
    if letter_guess in word:
        correct_guesses.append(letter_guess)
        return correct_guesses
    else:
        return correct_guesses

def Right_or_wrong(letter_guess, word):
    '''takes the word and guessed letter and prints if it was right or long'''
    #Made By Jason
    if letter_guess in word:
        print("Congratulations! ",letter_guess," Is in the word!")
    else:
        print("Sorry :(,", letter_guess, " is not in the word")


def draw_man(guesses, correct_guesses):
    '''draws the hangman/gallows based on the guesses and correct guess, no output'''
    #Made by Jason
    
    x = len(guesses)-len(correct_guesses)
    if x == 0:
        print(x,'wrong,', 7-x, 'lives left')
        print("   _______")
        print("  I        I")
        print("  I      ")
        print("  I    ")
        print("  I      ")
        print("__I__    ")
    elif x == 1:
        print(x," wrong,", 7-x, "lives left")
        print("   _______")
        print("  I        I")
        print("  I        O")
        print("  I    ")
        print("  I      ")
        print("__I__   ")
    elif x == 2:
        print(x," wrong,", 7-x, "lives left")
        print("   _______")
        print("  I        I")
        print("  I        O")
        print("  I        I")
        print("  I      ")
        print("__I__    ")
    elif x == 3:
        print(x," wrong,", 7-x, "lives left")      
        print("   _______")
        print("  I        I")
        print("  I        O")
        print("  I      --I")
        print("  I     ")
        print("__I__    ")
    elif x == 4:
        print(x," wrong", 7-x, "lives left")      
        print("   _______")
        print("  I        I")
        print("  I        O")
        print("  I      --I--")
        print("  I      ")
        print("__I__    ")
    elif x == 5:
        print(x," wrong,", 7-x, "lives left")      
        print("   _______")
        print("  I        I")
        print("  I        O")
        print("  I      --I--")
        print("  I        I")
        print("__I__     ")
    elif x == 6:
        print(x," wrong,", 7-x, "lives left")      
        print("   _______")
        print("  I        I")
        print("  I        O")
        print("  I      --I--")
        print("  I        I")
        print("__I__     /  ")
    elif x == 7:
        print(x," wrong,", 7-x, "lives left")      
        print("   _______")
        print("  I        I")
        print("  I        O")
        print("  I      --I--")
        print("  I        I")
        print("__I__     / \ ")

def write_guesses(guesses):
    '''prints out the list of guesses so far'''
    #made by Jason
    print("Your Guesses:", guesses)




def Check_End(word_with_blanks, correct_guesses, guesses):
    '''Determines if the game is won, lost, or should continue going. Uses word_with_blanks to determine if the game is won, Uses Correct_guess and Guesses to determine if it's lost  '''
    #Made By Jason
    a = len(guesses)
    b = len(correct_guesses)
    x = a-b
    underscore = '_'
    if x > 6:
        print("Game over! You Lose!")
        return(1)
    elif underscore in word_with_blanks:
        print("keep playing")
        return(0)
    else:
        print("You Win!!!!")
        print("The Word Was ",word_with_blanks)
        return(1)

######TESTS#####

def Test_Get_Word():
    print("test word 1")
    word = Get_Word()
    print(word)
    print("test word 2")
    word = Get_Word()
    print(word) 
    print("test word 3")
    word = Get_Word()
    print(word)

def Test_Create_word_with_blanks():
    '''Takes the word and returns a string with all letters replaced by underscores'''
    for word in (["dog","tree","orange"]):
        word_with_blanks = Create_word_with_blanks(word)
        print("word was:", word)
        print("with blanks is:", word_with_blanks)
    
def Test_Ask_letter():
    '''made by jack'''
    print("test 1:")
    letter_guess = Ask_letter(['a','r','t','y','l'])
    print("you guessed:", letter_guess, "which has not been guessed")
    print("test 2:")
    letter_guess = Ask_letter(['q','w','v','b','s'])
    print("you guessed:", letter_guess, "which has not been guessed")


def Test_update_word_with_blanks():
    '''takes the word, word with blanks and the letter guess and returns an updated version of the word_with_blanks '''
    word = "dog"
    word_with_blanks = "__g"
    letter_guess = "d"
    print("word was:", word, "word with blanks was", word_with_blanks,"letter guess was", letter_guess)
    word_with_blanks = update_word_with_blanks(word, word_with_blanks, letter_guess)
    print("new word with blanks is:", word_with_blanks)
    word = "tree"
    word_with_blanks = "__ee"
    letter_guess = "t"
    print("word was:", word, "word with blanks was", word_with_blanks,"letter guess was", letter_guess)
    word_with_blanks = update_word_with_blanks(word, word_with_blanks, letter_guess)
    print(word_with_blanks)
    word = "orange"
    word_with_blanks = "o____e"
    letter_guess = "q"
    print("word was:", word, "word with blanks was", word_with_blanks,"letter guess was", letter_guess)
    word_with_blanks = update_word_with_blanks(word, word_with_blanks, letter_guess)
    print(word_with_blanks)

    
def Test_update_guesses():
    '''Takes the guessed letter and guesses  and updates the guesses string'''
    
    guess = update_guesses(["a","s","d","f","g","h"],"i")
    print (guess)
    guess = update_guesses(["a","s","d",],"f")
    print (guess)
    guess = update_guesses(["a","s","d","f","g","h","i","j","k"],"l")
    print (guess)
    
def Test_update_correct_guesses():
    '''takes the guessed letter and word and updates list of correct guesses'''
    
    print("guess is a, word is bat, original list is [b]")
    new = update_correct_guesses("a", "bat", ["b"])
    print(new)
    print("guess is g, word is orange, list was [o,n]")
    new = update_correct_guesses("g", "orange", ["o","n"])
    print(new)
    
def Test_Right_or_Wrong():
    Right_or_wrong("a", "bat")
    Right_or_wrong("c", "boat")

def test_draw_man():
    draw_man(["a"],["a"])
    draw_man(["a","b"],["a"])
    draw_man(["a","b","c"],["a"])
    draw_man(["a","s","d","f"],["a","s"])
    draw_man(["a","s","d","f","g","h"],["a","s","d"])
    draw_man(["a","s","d","f","g","h","j","k","l"],["a","s","d","f","g"])
    draw_man(["a","s","d","f","g","h","j","k"],["a","s","d"])
    draw_man(["a","s","d","f","g","h","j","k"],["a","s"])
    draw_man(["a","s","d","f","g","h","j"],[])

def Test_write_guesses():
    write_guesses(["B","H","O","W"])
    write_guesses(["P","K","A","R","E"])

def Test_Write_Word_Guess():
    Write_Word_Guess("B_t")
    Write_Word_Guess("_om_u__r")
    Write_Word_Guess("O__n_e")

def Test_Check_End():
   end = (Check_End("H__S_",["H","S"],["H","S","G","Q"]))
   print(end)
   end = (Check_End("_o____er",["O","E","R"],["E","S","E","Q","R","A","B","C","D","F",]))
   print(end)
   end = (Check_End("BOAT",["B","O","A","T"],["B","S","O","T","A"]))
   print(end)

PlayHangman()
