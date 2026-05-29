import tkinter as tk
from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        buttons[row][column]['text'] = player

        if check_winner() is True:
            label.config(text=f"{player} wins")

        elif check_winner() == "Tie":
            label.config(text="It's a tie!")

        else:
            if player == players[0]:
                player = players[1]
            else:
                player = players[0]

            label.config(text=f"{player} turn")

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="light blue")
            buttons[row][1].config(bg="light blue")
            buttons[row][2].config(bg="light blue")
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="light blue")
            buttons[1][column].config(bg="light blue")
            buttons[2][column].config(bg="light blue")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="light blue")
        buttons[1][1].config(bg="light blue")
        buttons[2][2].config(bg="light blue")
        return True
    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        buttons[2][0].config(bg="light blue")
        buttons[1][1].config(bg="light blue")
        buttons[0][2].config(bg="light blue")
        return True
    elif free_space() is False:
        return "Tie"
    else:
        return False



def free_space():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True



def reset_board():
    global player
    player = random.choice(players)
    label.config(text=(f"{player} turn"))
    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ""
            buttons[row][column].config(bg=root.cget("bg"))


root = Tk()
root.title("Tic Tac Toe")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
frame = Frame(root)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(
            frame,
            text="",
            font=('consolas', 40),
            width=5,
            height=2,
            command=lambda row=row, column=column: next_turn(row, column)
        )

        buttons[row][column].grid(row=row, column=column)
label = Label(root, text=f"{player} turn", font=('courier new', 35))
label.pack(side=TOP)
reset_button = Button(
    root,
    text="Restart game",
    font=('courier new', 25),
    command=reset_board
)
reset_button.pack(side=TOP)
print(buttons)
root.mainloop()
