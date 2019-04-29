from tkinter import *
from random import choice
from PIL import Image, ImageTk
from mood import Mood
from kitty import Kitty
from question import Question

window = Tk()
window.title(" Kitty Kitty ")
window.geometry("800x300")

image_paths = ["happy.gif", "sad.gif", "angry.gif", "cute.gif", "confused.gif", "heart-broken.gif"]

img = Image.open(image_paths[0])
img = ImageTk.PhotoImage(img)
panel = Label(window, image=img)
panel.grid(column=2, row=0)

user = StringVar()
kitty  = StringVar()

user_label = Label(window, text="you : ")
user_label.grid(column=1, row=1)

user_entry = Entry(window, textvariable=user)
user_entry.grid(column=2, row=1)

kitty_entry = Label(window, textvariable=kitty, font=("Helvetica", 20))
kitty_entry.grid(column=3, row=0)

def chat():
    global panel
    global img
    global window

    question = user.get().lower()

    if question in Question.hi:
        kitty.set(choice(Kitty.hi))
        current_mood = Mood.HAPPY
    elif question in Question.cuteness:
        kitty.set(choice(Kitty.cuteness))
        current_mood = Mood.CUTE
    elif question in Question.provoking:
        kitty.set(choice(Kitty.anger))
        current_mood = choice([Mood.ANGRY, Mood.SAD])
    elif question in Question.adoption:
        kitty.set(choice(Kitty.adoption_agencies))
        current_mood = Mood.HAPPY
    elif question == "":
        kitty.set(choice(Kitty.please))
        current_mood = Mood.HEART_BROKEN
    else:
        kitty.set(choice(Kitty.idk))
        current_mood = Mood.CONFUSED

    img = Image.open(image_paths[current_mood.value])
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img)
    panel.grid(column=2, row=0)

btn = Button(window, text="speak", command=chat)
btn.grid(column=2, row=1, sticky="E")

window.mainloop()
