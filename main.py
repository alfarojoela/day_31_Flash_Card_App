# -------------------------SOLUTION FOR UI LAYOUT---------------------------- #
from tkinter import *
from pandas import *
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records") #argument changes format of to_learn dictionary
#print(to_learn)
current_card = {}

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)

    # was previously getting length of csv file and then using randomint within range
    current_card = random.choice(to_learn)
    # rather than attempting to clear existing text, solution uses configuration to assign new values to variables.
    # this gets around using delete method for canvas object which appears to be less precise.
    canvas.itemconfig(card_title, text = "French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)





window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#after method allows delay in milliseconds.  second argument is function call.
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, heigh=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)

language = "Title"

word= "word"


# -----overlooked saving function calls to variables ------- #
#need to change this with function
card_title = canvas.create_text(400, 150, text=f"{language}", font=("Arial", 40, "italic"))  #prior solution used label instead of canvas text
#need to change this
card_word = canvas.create_text(400, 263, text=f"{word}", font=("Arial", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image= PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.grid(row=1, column=0)

check_image=PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=next_card)
known_button.grid(row=1, column=1)

next_card()  #first call when app is started.  avoids place holder





window.mainloop()




















# --------------------------------ORIGINAL EFFORT FOR UI LAYOUT-----------------------------------#
# from tkinter import *
# from tkinter import messagebox
#
# BACKGROUND_COLOR = "#B1DDC6"
# #LANGUAGE_FONT = (font="Arial", 40, "italic")
#
# window=Tk()
# window.title("Flash Card")
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#
# canvas = Canvas(width=800, height=526, highlightthickness=0)  #place width first and then height as
#                                                             # a reminder so it forms x, y format
#                                                             #will reduce confusion in the future
#
# canvas.config(bg=BACKGROUND_COLOR)
#
# card_front = PhotoImage(file="./images/card_front.png")
# canvas.create_image(400, 263, image=card_front)  #placement is half of width, half of height
# canvas.grid(row=0, column=0, columnspan=2)
#
# language_label = Label(text="French", bg="white", font=("Arial", 20, "italic"))
# language_label.grid(row=0, column=0, columnspan=2)
#
# word_label = Label(text="Word", bg="white", font=("Arial", 60, "bold"))
# word_label.grid(row=1, column=0, columnspan=2)
#
# right_image = PhotoImage(file="./images/right.png")
# right_button = Button(image=right_image)
# right_button.grid(row=3, column=1)
#
# wrong_image = PhotoImage(file="./images/wrong.png")
# wrong_button = Button(image=wrong_image)
# wrong_button.grid(row=3, column=0)
#
#
#
#
#
# window.mainloop()