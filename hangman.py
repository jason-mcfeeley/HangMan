# This is a file.
import random

def Main():
    word = Get_Word()
    word_with_blanks = Create_word_with_blanks(word)
    end = False
    guesses = []
    correct_guesses = []
    while (end == False):
        letter_guess = Ask_letter(guesses)
        word_with_blanks = update_word_with_blanks(word, word_with_blanks, letter_guess)
        guesses = update_guesses(guesses, letter_guess)
        correct_guesses = update_correct_guesses
        '''word_with_blanks,correct = Check_Letter (word, word_with_blanks, guesses, correct_guesses)'''
        Draw_Man(guesses, correct_guesses)
        Write_Guesses(guesses)
        Write_Word_Guess(word_with_blanks)
        end = Check_end(word,word_with_blanks, guesses, correct_guesses)

def Get_Word():
    '''This function chooses a random word from the list of words and returns it'''
    words = ['dog', 'cat', 'wolf', 'fox', 'rabbit', 'parrot']
    return(random.choice(words))
                                                   
def Create_word_with_blanks(word):
    '''Takes the word and returns a string with all letters replaced by underscores'''
                                                   
def Ask_letter():
    '''asks the user for their guess and returns that guess, uses guesses to ensure they don't re-use a letter '''

def update_word_with_blanks(word, word_with_blanks, letter_guess):
    '''takes the word, word with blanks and the letter guess and returns an updated version of the word_with_blanks '''

def update_guesses(guesses, letter_guess):
    '''Takes the guessed letter and guesses  and updates the guesses string'''

def update_correct_guesses(letter_guess, word):
    '''takes the guessed letter and word and updates list of correct guesses'''


 ''' <This is being broken up into several new functions>
  
def Check_Letter(word, word_with_blanks, guesses, correct_guesses ):
    '''Asks user for input. Returns updated word list and if player is right or wrong

    e.g. if the word='cat' and the guess is 'a', it returns
    ["_A_",True] 
    and if the guess were 'o' it would return
    ['___',False]
    '''
    guess = raw_input('Guess a letter')
    if guess in word:
        search = guess
        x = word.find(search)
        s = word
        l = list(s)
        l[x] = guess
        news = "".join(l)
        print news, "You're right!"
    if guess not in word:
        print "guess again"
 '''

def Right_or_wrong(guess):
    '''takes the word and guessed letter and prints if it was right or long'''

'''   !!!!!Must be changed and rewritten!!!!
    if guess == 1:
        print("You Guessed Right!")
    else:
        print("Oh No! You Guessed wrong")
'''

def draw_man(guesses, correct_guesses):
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
    print("Your Guesses:", guesses)




def Check_End(word_with_blanks, correct_guesses, guesses):
    a = len(guesses)
    b = len(correct_guesses)
    x = a-b
    underscore = '_'
    if x > 6:
        print("Game over! You Lose!")
        return(0)
    elif underscore in word_with_blanks:
        print("keep playing")
        return(1)
    else:
        print("You Win!!!!")
        return(0)

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
        print("with blanks is:" word_with_blanks)
    
def Test_Ask_letter():
    '''asks the user for their guess and returns that guess, uses guesses to ensure they don't re-use a letter '''
    letter_guess = Ask_letter()
    print(letter_guess)
    letter_guess = Ask_letter()
    print(letter_guess)
    
def Test_update_word_with_blanks():
    '''takes the word, word with blanks and the letter guess and returns an updated version of the word_with_blanks '''
    word = "dog"
    word_with_blanks = "__g"
    letter_guess = "d"
    word_with_blanks = update_word_with_blanks(word, word_with_blanks, letter_guess)
    print(word_with_blanks)
    word = "tree"
    word_with_blanks = "__ee"
    letter_guess = "p"
    word_with_blanks = update_word_with_blanks(word, word_with_blanks, letter_guess)
    print(word_with_blanks)

    
def Test_update_guesses():
    '''Takes the guessed letter and guesses  and updates the guesses string'''
    update_guesses(guesses, letter_guess)
    
def Test_update_correct_guesses():
    '''takes the guessed letter and word and updates list of correct guesses'''
    update_correct_guesses(letter_guess, word)
    
def Test_Right_or_Wrong():
    '''!!!Must be changed and rewritten!!!'''
    Right_or_wrong(0)
    Right_or_wrong(1)

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
    Write_Guesses(["B","H","O","W"])
    Write_Guesses(["P","K","A","R","E"])

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

Test_write_guesses()
