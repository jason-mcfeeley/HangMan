# This is a file.
import random

def Main():
    word = Get_Word()
    end = False
    guesses = []
    correct_guesses = []
    while (end == False):
        word_with_blanks,correct = Check_Letter (word, word_with_blanks, guesses, correct_guesses)
        Draw_Man(guesses, correct_guesses)
        Write_Guesses(guesses)
        Write_Word_Guess(word_with_blanks)
        end = Check_end(word,word_with_blanks, guesses, correct_guesses)

def Get_Word():
    '''This function chooses a random word from the list of words and returns it'''
    words = ['dog', 'cat', 'wolf', 'fox', 'rabbit', 'parrot']
    return(random.choice(words))

    
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
 

def Right_or_wrong(guess):
    if guess == 1:
        print("You Guessed Right!")
    else:
        print("Oh No! You Guessed wrong")

def draw_man(guesses, correct_guesses):
    x = guesses-correct_guesses
    if x == 0:
        print(x," wrong,", 7-x, "lives left")
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


def Test_Check_Letter():
    Check_Letter("House", "H__S_",["H","S"],["H","S","G","Q"])
    Check_Letter("Computer","_o____er",["O","E","R"],["E","S","E","Q","R"])
    Check_Letter("Sweater","_we___r",["W","E","R"],["W","Q","E","R"])


def Test_Right_or_Wrong():
    Right_or_wrong(0)
    Right_or_wrong(1)

def test_draw_man():
    draw_man(1,1)
    draw_man(1,0)
    draw_man(4,2)
    draw_man(6,3)
    draw_man(9,5)
    draw_man(8,3)
    draw_man(8,2)
    draw_man(7,0)

def Test_Write_Guesses():
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
