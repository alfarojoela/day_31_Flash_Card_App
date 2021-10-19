from tkinter import *
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
#LANGUAGE_FONT = (font="Arial", 40, "italic")

window=Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)  #place width first and then height as
                                                            # a reminder so it forms x, y format
                                                            #will reduce confusion in the future

canvas.config(bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front)  #placement is half of width, half of height
canvas.grid(row=0, column=0, columnspan=2)

language_label = Label(text="French", bg="white", font=("Arial", 20, "italic"))
language_label.grid(row=0, column=0, columnspan=2)

word_label = Label(text="Word", bg="white", font=("Arial", 60, "bold"))
word_label.grid(row=1, column=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image)
right_button.grid(row=3, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image)
wrong_button.grid(row=3, column=0)





window.mainloop()