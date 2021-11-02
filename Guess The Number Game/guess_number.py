from tkinter import *
from random import *

#Lives
currentLives = 10;
#Picking a random number
randomNum = randint(1,100)
#--------------Functions-------------------------
#Process User Input
def press(event = None):
    #Obtainging user input from textbox
    num = enterGuess.get()
    #Check if it is an integer number
    if (str(num).isdecimal()):
        global currentLives;
        currentLives -= 1
        if(int(num) > randomNum and currentLives >= 0):
            statusLabel.config(text=f"My number is less than {num}")
            livesLabel.config(text=f"You have {currentLives} remaining lives")
        elif(int(num) < randomNum and currentLives >= 0):
            statusLabel.config(text=f"My number is higher than {num}")
            livesLabel.config(text=f"You have {currentLives} remaining lives")
        elif(int(num) == randomNum and currentLives >= 0):
            statusLabel.config(text="You Win!", font='arial 12 bold')
            livesLabel.config(text=f"You have {currentLives} remaining guesses")
            enterGuess.delete(0, "end")
            enterGuess['state'] = 'disabled'
        elif(currentLives < 0):
            statusLabel.config(text="You Lost!", font='arial 12 bold')
            enterGuess.delete(0, "end")
            enterGuess['state'] = 'disabled'
    #Invalid user input
    elif(currentLives >= 0):
        statusLabel.config(text="Enter a valir number")
    else:
        statusLabel.config(text="You Lost!", font='arial 12 bold')
        enterGuess.delete(0, "end")
        enterGuess['state'] = 'disabled'
    enterGuess.delete(0, "end")
#Reset Button
def reset_button():
    global currentLives, randomNum
    randomNum = randint(1,100)
    currentLives = 10;
    statusLabel.config(text="Enter a number from 1 to 100 to guess:", font='arial 11')
    livesLabel.config(text=f"You have {currentLives} remaining guesses")
    enterGuess['state'] = 'normal'
    enterGuess.delete(0, "end")
#Giviving name to window
root = Tk()
#Giving Size
root.geometry('350x115')
#Don't resize
root.resizable(False,False)
#Adding Title
root.title('Guess The Number Game')
#Addign Labels
instructionLabel = Label(root, text='Play With Me!', font = 'arial 12 bold')
instructionLabel.pack()
statusLabel = Label(root, text="Enter a number from 1 to 100 to guess:", font='arial 11')
statusLabel.pack()
#Adding TextBox
enterGuess = Entry()
enterGuess.pack()
#Adding Buttons
guessButon = Button(root, text="Guess", command = press)
guessButon.pack()
root.bind('<Return>', press)
resetBtn = Button(root, text="Reset", command = reset_button)
resetBtn.pack(side=LEFT)
#Label that shows lives
livesLabel = Label(root, text=f"You have {currentLives} remaining guesses")
livesLabel.pack(side=RIGHT)
#Open Window
root.mainloop()