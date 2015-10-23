# This is a file.


def Main():
    word = Get_Word()
    while (end == false):
        Check_Letter (word, word_with_blanks, guesses, correct_guesses Jack)
        Print_Right_or_Wrong 
        Draw_Man (Jason)
        Write_Guesses
        Write_Word_Guess
        Check_end



Def Get_Word():
    words = [‘dog’, ’cat’, ’wolf’, ‘fox’, ‘rabbit’, ‘parrot’]
            return(random.choice(words))

    
Def Check_Letter(word, word_with_blanks, guesses, correct_guesses ):
    "guess" = raw_input(‘Guess a letter’)
    word =  
    if "guess" in word:       # from stack exchange 
    print "you are right"
    if "guess" not in word:
    print "guess again"  


Def Right_or_wrong(guess)
    if guess == 1:
        print("You Guessed Right!")
    else:
        print("Oh No! You Guessed wrong")

Def Draw_Man(guesses, correct_guesses):
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

Def write_guesses(guesses):
    print("Your Guesses:", guesses)




Def Check_End(word, word_with_blanks, guesses, correct_guesses):
    x = guesses-correct_guesses
    if x == 7:
        print(“Game over! You Lose!”)
        #!!!!!! - Some Sort Of End Thing - !!!!!!!
    elif word == word_with_blanks:
        print(“You Win! Congrats!”)
    else:
        print(“Keep Playing”)

######TESTS#####

def Test_Get_Word():
    print(“test word 1”)
    word = Get_Word()
    print(word)
    print(“test word 2”)
    word = Get_Word()
    print(word) 
    print(“test word 3”)
    word = Get_Word()
    print(word)


def Test_Check_Letter():
    Check_Letter(“House”, [“H__S_”],[”H”,”S”],[“H”,”S”,”G”,”Q”])
    Check_Letter(“Computer”,“_o____er”,[“O”,”E”,”R”],[“E”,”S”,”E”,”Q”,”R”])
    Check_Letter(“Sweater”,“_we___r”,[“W”,”E”,”R”],[“W”,”Q”,”E”,”R”])


def Test_Print_Right_Or_Wrong():
    Print_Right_Or_Wrong(0)
    Print_Right_Or_Wrong(1)

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
    Write_Guesses([“B”,”H”,”O”,”W”])
    Write_Guesses([“P”,”K”,”A”,”R”,”E”])

def Test_Write_Word_Guess():
    Write_Word_Guess(“B_t”)
    Write_Word_Guess(“_om_u__r”)
    Write_Word_Guess(“O__n_e”)

def Test_Check_End():
    Check_End(“House”,“H__S_”],[”H”,”S”],[“H”,”S”,”G”,”Q”])
    Check_End(“Computer”,”_o____er”,[“O”,”E”,”R”],[“E”,”S”,”E”,”Q”,”R”])

