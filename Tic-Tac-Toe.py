import tkinter
from tkinter import *
import pygame.mixer
import random, time
import os

def ai_easy():
    def next_turn(row, column):
        global player
        global x_win
        global o_win
        global tie_win

        if player_info.get("buttons")[row][column]["text"] == "" and check_winner() is False:

            if player == player_info.get("players")[0]:

                player_info.get("buttons")[row][column]["text"] = player

                if check_winner() is True:
                    label.config(text=(player_info.get("players")[0] + " Wins"))
                    x_win += 1
                    label_x.config(text="X's Wins " + str(x_win))

                elif check_winner() == "Tie":
                    label.config(text="Tie")
                    tie_win += 1
                    label_tie.config(text="Tie Win " + str(tie_win))

                elif check_winner() is False:
                    player = player_info.get("players")[1]
                    label.config(text=(player + "'s Turn"))
                    ai_turn()

            else:
                player_info.get("buttons")[row][column]["text"] = player

                if check_winner() is True:
                    label.config(text=(player_info.get("players")[1] + " Wins"))
                    o_win += 1
                    label_o.config(text="O's Wins " + str(o_win))

                elif check_winner() == "Tie":
                    label.config(text="Tie")
                    tie_win += 1
                    label_tie.config(text="Tie Win " + str(tie_win))

                elif check_winner() is False:
                    player = player_info.get("players")[0]
                    label.config(text=(player + "'s Turn"))

    def check_winner():

        for row in range(3):
            if (player_info.get("buttons")[row][0]["text"] == player_info.get("buttons")[row][1]["text"] ==
                    player_info.get("buttons")[row][2]["text"] != ""):
                player_info.get("buttons")[row][0].config(bg="green")
                player_info.get("buttons")[row][1].config(bg="green")
                player_info.get("buttons")[row][2].config(bg="green")
                return True

        for column in range(3):
            if (player_info.get("buttons")[0][column]["text"] == player_info.get("buttons")[1][column]["text"] ==
                    player_info.get("buttons")[2][column]["text"] != ""):
                player_info.get("buttons")[0][column].config(bg="green")
                player_info.get("buttons")[1][column].config(bg="green")
                player_info.get("buttons")[2][column].config(bg="green")
                return True

        if (player_info.get("buttons")[0][0]["text"] == player_info.get("buttons")[1][1]["text"] ==
                player_info.get("buttons")[2][2]["text"] != ""):
            player_info.get("buttons")[0][0].config(bg="green")
            player_info.get("buttons")[1][1].config(bg="green")
            player_info.get("buttons")[2][2].config(bg="green")
            return True

        elif (player_info.get("buttons")[0][2]["text"] == player_info.get("buttons")[1][1]["text"] ==
                player_info.get("buttons")[2][0]["text"] != ""):
            player_info.get("buttons")[0][2].config(bg="green")
            player_info.get("buttons")[1][1].config(bg="green")
            player_info.get("buttons")[2][0].config(bg="green")
            return True

        elif empty_spaces() is False:

            for row in range(3):

                for column in range(3):
                    player_info.get('buttons')[row][column].config(bg="yellow")

            return "Tie"

        return False

    def empty_spaces():
        spaces = 9

        for row in range(3):
            for column in range(3):
                if player_info.get("buttons")[row][column]["text"] != "":
                    spaces -= 1

        if spaces == 0:
            return False
        else:
            return True

    def ai_turn():
        while True:
            row = random.choice(value)
            column = random.choice(value)
            if player_info.get("buttons")[row][column]["text"] == "":
                next_turn(row, column)
                break

    def new_game():
        global player

        player = random.choice(players)

        label.config(text=player + "'s turn")

        for row in range(3):
            for column in range(3):
                player_info.get('buttons')[row][column].config(text="", bg="#F0F0F0")

        if player == "O":
            ai_turn()

    frame1.destroy()
    label_title.destroy()
    window = Frame(root, bg="light blue")
    window.pack()

    menubar = Menu(root)
    root.config(menu=menubar)
    file_menu = Menu(root)
    file_menu.add_command(label="Main Menu", command=lambda: main_menu(window))
    file_menu.add_command(label="Exit", command=end_game)
    menubar.add_cascade(label="File", menu=file_menu, underline=0)

    player_info = dict(players=["X", "O"],
                       player=random.choice(players),
                       buttons=[["", "", ""],
                                ["", "", ""],
                                ["", "", ""]])

    label = Label(window, text=player_info.get('player') + "'s Turn", font=('consolas', 40), bg="light blue")
    label.pack(side="top")

    reset_button = Button(window, text="restart", font=('consolas', 20), command=new_game, bg="blue")
    reset_button.pack(side="bottom")

    x_win = 0
    label_x = Label(window, text="X's Wins " + str(x_win), font=('consolas', 40), bg="light blue")
    label_x.pack(side="bottom")

    o_win = 0
    label_o = Label(window, text="O's Wins " + str(o_win), font=('consolas', 40), bg="light blue")
    label_o.pack(side="bottom")

    tie_win = 0
    label_tie = Label(window, text="Tie's Wins " + str(tie_win), font=('consolas', 40), bg="light blue")
    label_tie.pack(side="bottom")

    value = [0, 1, 2]

    frame = Frame(window, padx=20, pady=100, bg="light blue")
    frame.pack()

    for row in range(3):
        for column in range(3):
            player_info.get('buttons')[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                                             command=lambda row=row, column=column:
                                                             next_turn(row,column))
            player_info.get('buttons')[row][column].grid(row=row, column=column)

    if player_info.get("player") == "O":
        ai_turn()

def ai_medium():
    def next_turn(row, column):
        global player
        global x_win
        global o_win
        global tie_win

        if player_info.get("buttons")[row][column]["text"] == "" and check_winner() is False:

            if player == player_info.get("players")[0]:

                player_info.get("buttons")[row][column]["text"] = player

                if check_winner() is True:
                    label.config(text=(player_info.get("players")[0] + " Wins"))
                    x_win += 1
                    label_x.config(text="X's Wins " + str(x_win))

                elif check_winner() == "Tie":
                    label.config(text="Tie")
                    tie_win += 1
                    label_tie.config(text="Tie Win " + str(tie_win))

                elif check_winner() is False:
                    player = player_info.get("players")[1]
                    label.config(text=(player + "'s Turn"))
                    ai_turn()

            else:
                player_info.get("buttons")[row][column]["text"] = player

                if check_winner() is True:
                    label.config(text=(player_info.get("players")[1] + " Wins"))
                    o_win += 1
                    label_o.config(text="O's Wins " + str(o_win))

                elif check_winner() == "Tie":
                    label.config(text="Tie")
                    tie_win += 1
                    label_tie.config(text="Tie Win " + str(tie_win))

                elif check_winner() is False:
                    player = player_info.get("players")[0]
                    label.config(text=(player + "'s Turn"))

    def check_winner():

        for row in range(3):
            if (player_info.get("buttons")[row][0]["text"] == player_info.get("buttons")[row][1]["text"] ==
                    player_info.get("buttons")[row][2]["text"] != ""):
                player_info.get("buttons")[row][0].config(bg="green")
                player_info.get("buttons")[row][1].config(bg="green")
                player_info.get("buttons")[row][2].config(bg="green")
                return True

        for column in range(3):
            if (player_info.get("buttons")[0][column]["text"] == player_info.get("buttons")[1][column]["text"] ==
                    player_info.get("buttons")[2][column]["text"] != ""):
                player_info.get("buttons")[0][column].config(bg="green")
                player_info.get("buttons")[1][column].config(bg="green")
                player_info.get("buttons")[2][column].config(bg="green")
                return True

        if (player_info.get("buttons")[0][0]["text"] == player_info.get("buttons")[1][1]["text"] ==
                player_info.get("buttons")[2][2]["text"] != ""):
            player_info.get("buttons")[0][0].config(bg="green")
            player_info.get("buttons")[1][1].config(bg="green")
            player_info.get("buttons")[2][2].config(bg="green")
            return True

        elif (player_info.get("buttons")[0][2]["text"] == player_info.get("buttons")[1][1]["text"] ==
              player_info.get("buttons")[2][0]["text"] != ""):
            player_info.get("buttons")[0][2].config(bg="green")
            player_info.get("buttons")[1][1].config(bg="green")
            player_info.get("buttons")[2][0].config(bg="green")
            return True

        elif empty_spaces() is False:

            for row in range(3):

                for column in range(3):
                    player_info.get('buttons')[row][column].config(bg="yellow")

            return "Tie"

        return False

    def empty_spaces():
        spaces = 9

        for row in range(3):
            for column in range(3):
                if player_info.get("buttons")[row][column]["text"] != "":
                    spaces -= 1

        if spaces == 0:
            return False
        else:
            return True

    def ai_turn():
        for row in range(3):
            if (player_info.get('buttons')[row][0]["text"] == "O" and player_info.get('buttons')[row][1]["text"] == "O"
                    and player_info.get('buttons')[row][2]["text"] == ""):
                next_turn(row,2)
            elif (player_info.get('buttons')[row][0]["text"] == "O" and player_info.get('buttons')[row][1]["text"] == ""
                    and player_info.get('buttons')[row][2]["text"] == "O"):
                next_turn(row,1)
            elif (player_info.get('buttons')[row][0]["text"] == "" and player_info.get('buttons')[row][1]["text"] == "O"
                    and player_info.get('buttons')[row][2]["text"] == "O"):
                next_turn(row,0)

        for column in range(3):
            if (player_info.get('buttons')[0][column]["text"] == "O" and player_info.get('buttons')[1][column]["text"] == "O"
                    and player_info.get('buttons')[2][column]["text"] == ""):
                next_turn(2, column)
            elif (player_info.get('buttons')[0][column]["text"] == "O" and player_info.get('buttons')[1][column]["text"] == ""
                    and player_info.get('buttons')[2][column]["text"] == "O"):
                next_turn(1, column)
            elif (player_info.get('buttons')[0][column]["text"] == "" and player_info.get('buttons')[1][column]["text"] == "O"
                    and player_info.get('buttons')[2][column]["text"] == "O"):
                next_turn(0, column)

        if (player_info.get('buttons')[0][0]["text"] == "O" and player_info.get('buttons')[1][1]["text"] == "O"
                    and player_info.get('buttons')[2][2]["text"] == ""):
            next_turn(2, 2)

        elif (player_info.get('buttons')[0][0]["text"] == "O" and player_info.get('buttons')[1][1]["text"] == ""
                    and player_info.get('buttons')[2][2]["text"] == "O"):
            next_turn(1, 1)

        elif (player_info.get('buttons')[0][0]["text"] == "" and player_info.get('buttons')[1][1]["text"] == "O"
                    and player_info.get('buttons')[2][2]["text"] == "O"):
            next_turn(0, 0)

        if (player_info.get('buttons')[2][0]["text"] == "O" and player_info.get('buttons')[1][1]["text"] == "O"
                    and player_info.get('buttons')[0][2]["text"] == ""):
            next_turn(0, 2)

        elif (player_info.get('buttons')[2][0]["text"] == "O" and player_info.get('buttons')[1][1]["text"] == ""
                    and player_info.get('buttons')[0][2]["text"] == "O"):
            next_turn(1, 1)

        elif (player_info.get('buttons')[2][0]["text"] == "" and player_info.get('buttons')[1][1]["text"] == "O"
                    and player_info.get('buttons')[0][2]["text"] == "O"):
            next_turn(2, 0)

        while True:
            row = random.choice(value)
            column = random.choice(value)
            if player_info.get("buttons")[row][column]["text"] == "":
                next_turn(row, column)
                break

    def new_game():
        global player

        player = random.choice(players)

        label.config(text=player + "'s turn")

        for row in range(3):
            for column in range(3):
                player_info.get('buttons')[row][column].config(text="", bg="#F0F0F0")

        if player == "O":
            ai_turn()

    frame1.destroy()
    label_title.destroy()
    window = Frame(root, bg="light blue")
    window.pack()

    menubar = Menu(root)
    root.config(menu=menubar)
    file_menu = Menu(root)
    file_menu.add_command(label="Main Menu", command=lambda: main_menu(window))
    file_menu.add_command(label="Exit", command=end_game)
    menubar.add_cascade(label="File", menu=file_menu, underline=0)

    player_info = dict(players=["X", "O"],
                       player=random.choice(players),
                       buttons=[["", "", ""],
                                ["", "", ""],
                                ["", "", ""]])

    label = Label(window, text=player_info.get('player') + "'s Turn", font=('consolas', 40), bg="light blue")
    label.pack(side="top")

    reset_button = Button(window, text="restart", font=('consolas', 20), command=new_game, bg="blue")
    reset_button.pack(side="bottom")

    x_win = 0
    label_x = Label(window, text="X's Wins " + str(x_win), font=('consolas', 40), bg="light blue")
    label_x.pack(side="bottom")

    o_win = 0
    label_o = Label(window, text="O's Wins " + str(o_win), font=('consolas', 40), bg="light blue")
    label_o.pack(side="bottom")

    tie_win = 0
    label_tie = Label(window, text="Tie's Wins " + str(tie_win), font=('consolas', 40), bg="light blue")
    label_tie.pack(side="bottom")

    value = [0, 1, 2]

    frame = Frame(window, padx=20, pady=100, bg="light blue")
    frame.pack()

    for row in range(3):
        for column in range(3):
            player_info.get('buttons')[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                                             command=lambda row=row, column=column:
                                                             next_turn(row, column))
            player_info.get('buttons')[row][column].grid(row=row, column=column)

    if player_info.get("player") == "O":
        ai_turn()

def ai_hard():
    def next_turn(row, column):
        global player
        global x_win
        global o_win
        global tie_win

        if player_info.get("buttons")[row][column]["text"] == "" and check_winner() is False:

            if player == player_info.get("players")[0]:

                player_info.get("buttons")[row][column]["text"] = player

                if check_winner() is True:
                    label.config(text=(player_info.get("players")[0] + " Wins"))
                    x_win += 1
                    label_x.config(text="X's Wins " + str(x_win))

                elif check_winner() == "Tie":
                    label.config(text="Tie")
                    tie_win += 1
                    label_tie.config(text="Tie Win " + str(tie_win))

                elif check_winner() is False:
                    player = player_info.get("players")[1]
                    label.config(text=(player + "'s Turn"))
                    ai_turn()

            else:
                player_info.get("buttons")[row][column]["text"] = player

                if check_winner() is True:
                    label.config(text=(player_info.get("players")[1] + " Wins"))
                    o_win += 1
                    label_o.config(text="O's Wins " + str(o_win))

                elif check_winner() == "Tie":
                    label.config(text="Tie")
                    tie_win += 1
                    label_tie.config(text="Tie Win " + str(tie_win))

                elif check_winner() is False:
                    player = player_info.get("players")[0]
                    label.config(text=(player + "'s Turn"))

    def check_winner():

        for row in range(3):
            if (player_info.get("buttons")[row][0]["text"] == player_info.get("buttons")[row][1]["text"] ==
                    player_info.get("buttons")[row][2]["text"] != ""):
                player_info.get("buttons")[row][0].config(bg="green")
                player_info.get("buttons")[row][1].config(bg="green")
                player_info.get("buttons")[row][2].config(bg="green")
                return True

        for column in range(3):
            if (player_info.get("buttons")[0][column]["text"] == player_info.get("buttons")[1][column]["text"] ==
                    player_info.get("buttons")[2][column]["text"] != ""):
                player_info.get("buttons")[0][column].config(bg="green")
                player_info.get("buttons")[1][column].config(bg="green")
                player_info.get("buttons")[2][column].config(bg="green")
                return True

        if (player_info.get("buttons")[0][0]["text"] == player_info.get("buttons")[1][1]["text"] ==
                player_info.get("buttons")[2][2]["text"] != ""):
            player_info.get("buttons")[0][0].config(bg="green")
            player_info.get("buttons")[1][1].config(bg="green")
            player_info.get("buttons")[2][2].config(bg="green")
            return True

        elif (player_info.get("buttons")[0][2]["text"] == player_info.get("buttons")[1][1]["text"] ==
              player_info.get("buttons")[2][0]["text"] != ""):
            player_info.get("buttons")[0][2].config(bg="green")
            player_info.get("buttons")[1][1].config(bg="green")
            player_info.get("buttons")[2][0].config(bg="green")
            return True

        elif empty_spaces() is False:

            for row in range(3):

                for column in range(3):
                    player_info.get('buttons')[row][column].config(bg="yellow")

            return "Tie"

        return False

    def empty_spaces():
        spaces = 9

        for row in range(3):
            for column in range(3):
                if player_info.get("buttons")[row][column]["text"] != "":
                    spaces -= 1

        if spaces == 0:
            return False
        else:
            return True

    def ai_turn():
        for row in range(3):
            if (player_info.get('buttons')[row][0]["text"] == "O" and player_info.get('buttons')[row][1]["text"] == "O"
                    and player_info.get('buttons')[row][2]["text"] == ""):
                next_turn(row, 2)
            elif (player_info.get('buttons')[row][0]["text"] == "O" and player_info.get('buttons')[row][1]["text"] == ""
                  and player_info.get('buttons')[row][2]["text"] == "O"):
                next_turn(row, 1)
            elif (player_info.get('buttons')[row][0]["text"] == "" and player_info.get('buttons')[row][1]["text"] == "O"
                  and player_info.get('buttons')[row][2]["text"] == "O"):
                next_turn(row, 0)

        for column in range(3):
            if (player_info.get('buttons')[0][column]["text"] == "O" and player_info.get('buttons')[1][column][
                "text"] == "O"
                    and player_info.get('buttons')[2][column]["text"] == ""):
                next_turn(2, column)
            elif (player_info.get('buttons')[0][column]["text"] == "O" and player_info.get('buttons')[1][column][
                "text"] == ""
                  and player_info.get('buttons')[2][column]["text"] == "O"):
                next_turn(1, column)
            elif (player_info.get('buttons')[0][column]["text"] == "" and player_info.get('buttons')[1][column][
                "text"] == "O"
                  and player_info.get('buttons')[2][column]["text"] == "O"):
                next_turn(0, column)

        if (player_info.get('buttons')[0][0]["text"] == "O" and player_info.get('buttons')[1][1]["text"] == "O"
                and player_info.get('buttons')[2][2]["text"] == ""):
            next_turn(2, 2)

        elif (player_info.get('buttons')[0][0]["text"] == "O" and player_info.get('buttons')[1][1]["text"] == ""
              and player_info.get('buttons')[2][2]["text"] == "O"):
            next_turn(1, 1)

        elif (player_info.get('buttons')[0][0]["text"] == "" and player_info.get('buttons')[1][1]["text"] == "O"
              and player_info.get('buttons')[2][2]["text"] == "O"):
            next_turn(0, 0)

        if (player_info.get('buttons')[2][0]["text"] == "O" and player_info.get('buttons')[1][1]["text"] == "O"
                and player_info.get('buttons')[0][2]["text"] == ""):
            next_turn(0, 2)

        elif (player_info.get('buttons')[2][0]["text"] == "O" and player_info.get('buttons')[1][1]["text"] == ""
              and player_info.get('buttons')[0][2]["text"] == "O"):
            next_turn(1, 1)

        elif (player_info.get('buttons')[2][0]["text"] == "" and player_info.get('buttons')[1][1]["text"] == "O"
              and player_info.get('buttons')[0][2]["text"] == "O"):
            next_turn(2, 0)

        move_made = False  # Track if a move has been made

        # Check rows
        for row in range(3):
            if move_made:
                break
            if (player_info.get('buttons')[row][0]["text"] == "X" and
                    player_info.get('buttons')[row][1]["text"] == "X" and
                    player_info.get('buttons')[row][2]["text"] == ""):
                next_turn(row, 2)
                move_made = True
                break
            elif (player_info.get('buttons')[row][0]["text"] == "X" and
                  player_info.get('buttons')[row][1]["text"] == "" and
                  player_info.get('buttons')[row][2]["text"] == "X"):
                next_turn(row, 1)
                move_made = True
                break
            elif (player_info.get('buttons')[row][0]["text"] == "" and
                  player_info.get('buttons')[row][1]["text"] == "X" and
                  player_info.get('buttons')[row][2]["text"] == "X"):
                next_turn(row, 0)
                move_made = True
                break

        if move_made:
            return

        # Check columns
        for column in range(3):
            if move_made:
                break
            if (player_info.get('buttons')[0][column]["text"] == "X" and
                    player_info.get('buttons')[1][column]["text"] == "X" and
                    player_info.get('buttons')[2][column]["text"] == ""):
                next_turn(2, column)
                move_made = True
                break
            elif (player_info.get('buttons')[0][column]["text"] == "X" and
                  player_info.get('buttons')[1][column]["text"] == "" and
                    player_info.get('buttons')[2][column]["text"] == "X"):
                next_turn(1, column)
                move_made = True
                break
            elif (player_info.get('buttons')[0][column]["text"] == "" and
                  player_info.get('buttons')[1][column]["text"] == "X" and
                  player_info.get('buttons')[2][column]["text"] == "X"):
                next_turn(0, column)
                move_made = True
                break

        if move_made:
            return

        # Check diagonals
        if (player_info.get('buttons')[0][0]["text"] == "X" and
                player_info.get('buttons')[1][1]["text"] == "X" and
                player_info.get('buttons')[2][2]["text"] == ""):
            next_turn(2, 2)
            return
        elif (player_info.get('buttons')[0][0]["text"] == "X" and
              player_info.get('buttons')[1][1]["text"] == "" and
              player_info.get('buttons')[2][2]["text"] == "X"):
            next_turn(1, 1)
            return

        while True:
            row = random.choice(value)
            column = random.choice(value)
            if player_info.get("buttons")[row][column]["text"] == "":
                next_turn(row, column)
                break

    def new_game():
        global player

        player = random.choice(players)

        label.config(text=player + "'s turn")

        for row in range(3):
            for column in range(3):
                player_info.get('buttons')[row][column].config(text="", bg="#F0F0F0")

        if player == "O":
            ai_turn()

    frame1.destroy()
    label_title.destroy()
    window = Frame(root, bg="light blue")
    window.pack()

    menubar = Menu(root)
    root.config(menu=menubar)
    file_menu = Menu(root)
    file_menu.add_command(label="Main Menu", command=lambda: main_menu(window))
    file_menu.add_command(label="Exit", command=end_game)
    menubar.add_cascade(label="File", menu=file_menu, underline=0)

    player_info = dict(players=["X", "O"],
                       player=random.choice(players),
                       buttons=[["", "", ""],
                                ["", "", ""],
                                ["", "", ""]])

    label = Label(window, text=player_info.get('player') + "'s Turn", font=('consolas', 40), bg="light blue")
    label.pack(side="top")

    reset_button = Button(window, text="restart", font=('consolas', 20), command=new_game, bg="blue")
    reset_button.pack(side="bottom")

    x_win = 0
    label_x = Label(window, text="X's Wins " + str(x_win), font=('consolas', 40), bg="light blue")
    label_x.pack(side="bottom")

    o_win = 0
    label_o = Label(window, text="O's Wins " + str(o_win), font=('consolas', 40), bg="light blue")
    label_o.pack(side="bottom")

    tie_win = 0
    label_tie = Label(window, text="Tie's Wins " + str(tie_win), font=('consolas', 40), bg="light blue")
    label_tie.pack(side="bottom")

    value = [0, 1, 2]

    frame = Frame(window, padx=20, pady=100, bg="light blue")
    frame.pack()

    for row in range(3):
        for column in range(3):
            player_info.get('buttons')[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                                             command=lambda row=row, column=column:
                                                             next_turn(row, column))
            player_info.get('buttons')[row][column].grid(row=row, column=column)

    if player_info.get("player") == "O":
        ai_turn()

def multi_player():
    def next_turn(row, column):

        global player
        global x_win
        global o_win
        global tie_win

        if player_info.get('buttons')[row][column]['text'] == "" and check_winner() is False:

            if player == player_info.get('players')[0]:

                player_info.get('buttons')[row][column]['text'] = player

                if check_winner() is False:
                    player = player_info.get('players')[1]
                    label.config(text=(player + "'s Turn"))

                elif check_winner() is True:
                    label.config(text=(player_info.get('players')[0] + " Wins"))
                    x_win += 1
                    label_x.config(text="X's Wins " + str(x_win))

                elif check_winner() == "Tie":
                    label.config(text=("Tie"))
                    tie_win += 1
                    label_tie.config(text="Tie Win " + str(tie_win))

            else:
                player_info.get('buttons')[row][column]['text'] = player
                if check_winner() is False:
                    player = player_info.get('players')[0]
                    label.config(text=(player + "'s Turn"))

                elif check_winner() is True:
                    label.config(text=(player_info.get('players')[1] + " Wins"))
                    o_win += 1
                    label_o.config(text="O's Wins " + str(o_win))

                elif check_winner() == "Tie":
                    label.config(text=("Tie"))
                    tie_win += 1
                    label_tie.config(text="Tie Win " + str(tie_win))

    def check_winner():

        for row in range(3):
            if (player_info.get('buttons')[row][0]['text'] == player_info.get('buttons')[row][1]['text'] ==
                player_info.get('buttons')[row][2]['text'] != ""):
                player_info.get('buttons')[row][0].config(bg="green")
                player_info.get('buttons')[row][1].config(bg="green")
                player_info.get('buttons')[row][2].config(bg="green")
                return True

        for column in range(3):
            if (player_info.get('buttons')[0][column]['text'] == player_info.get('buttons')[1][column]['text'] ==
                player_info.get('buttons')[2][column]['text'] != ""):
                player_info.get('buttons')[0][column].config(bg="green")
                player_info.get('buttons')[1][column].config(bg="green")
                player_info.get('buttons')[2][column].config(bg="green")
                return True

        if (player_info.get('buttons')[0][0]['text'] == player_info.get('buttons')[1][1]['text'] ==
            player_info.get('buttons')[2][2]['text'] != ""):
            player_info.get('buttons')[0][0].config(bg="green")
            player_info.get('buttons')[1][1].config(bg="green")
            player_info.get('buttons')[2][2].config(bg="green")
            return True

        elif (player_info.get('buttons')[2][0]['text'] == player_info.get('buttons')[1][1]['text'] ==
              player_info.get('buttons')[0][2]['text'] != ""):
            player_info.get('buttons')[2][0].config(bg="green")
            player_info.get('buttons')[1][1].config(bg="green")
            player_info.get('buttons')[0][2].config(bg="green")
            return True

        elif empty_spaces() is False:
            for row in range(3):
                for column in range(3):
                    player_info.get('buttons')[row][column].config(bg="yellow")
            return "Tie"

        else:
            return False

    def empty_spaces():

        spaces = 9

        for row in range(3):
            for column in range(3):
                if player_info.get('buttons')[row][column]['text'] != "":
                    spaces -= 1

        if spaces == 0:
            return False
        else:
            return True

    def new_game():

        global player

        player = random.choice(players)

        label.config(text=player + "'s turn")

        for row in range(3):
            for column in range(3):
                player_info.get('buttons')[row][column].config(text="", bg="#F0F0F0")

    frame1.destroy()
    label_title.destroy()
    window = Frame(root, bg="light blue")
    window.pack()

    menubar = Menu(root)
    root.config(menu= menubar)

    file_menu = Menu(root)
    file_menu.add_command(label="Main Menu", command=lambda: main_menu(window))
    file_menu.add_command(label="Exit", command=end_game)

    menubar.add_cascade(label="File", menu=file_menu, underline=0)

    player_info = dict(players=["X", "O"],
                       player=random.choice(players),
                       buttons=[[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]])

    label = Label(window, text=player_info.get('player') + "'s Turn", font=('consolas', 40), bg="light blue")
    label.pack(side="top")

    reset_button = Button(window, text="restart", font=('consolas', 20), command=new_game, bg="blue")
    reset_button.pack(side="bottom")

    x_win = 0
    label_x = Label(window, text="X's Wins " + str(x_win), font=('consolas', 40), bg="light blue")
    label_x.pack(side="bottom")

    o_win = 0
    label_o = Label(window, text="O's Wins " + str(o_win), font=('consolas', 40), bg="light blue")
    label_o.pack(side="bottom")

    tie_win = 0
    label_tie = Label(window, text="Tie's Wins " + str(tie_win), font=('consolas', 40), bg="light blue")
    label_tie.pack(side="bottom")

    frame = Frame(window, padx=20, pady=100, bg="light blue")
    frame.pack()

    for row in range(3):
        for column in range(3):
            player_info.get('buttons')[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                          command=lambda row=row, column=column: next_turn(row, column))
            player_info.get('buttons')[row][column].grid(row=row, column=column)

def credit_screen():
    frame1.destroy()
    label_title.destroy()
    window_credits = Frame(root, bg="light blue")
    window_credits.pack(padx=20, pady=250)

    menubar = Menu(root)
    root.config(menu=menubar)

    file_menu = Menu(root)
    file_menu.add_command(label="Main Menu", command=lambda: main_menu(window_credits))
    file_menu.add_command(label="Exit", command=end_game)

    menubar.add_cascade(label="File", menu=file_menu, underline=0)

    label = Label(window_credits, text="Credits", bg="light blue", font=('consolas', 50))
    label.grid(row=0, column=0)

    label = Label(window_credits, text="Page", bg="light blue", font=('consolas', 50))
    label.grid(row=0, column=1)

    label = Label(window_credits, text="Title", bg="light blue", font=('consolas', 50))
    label.grid(row=1, column=0)

    label = Label(window_credits, text="Name", bg="light blue", font=('consolas', 50))
    label.grid(row=1, column=1)

    label = Label(window_credits, text="", bg="light blue", font=('consolas', 50))
    label.grid(row=2, column=0)

    label = Label(window_credits, text="", bg="light blue", font=('consolas', 50))
    label.grid(row=2, column=1)

    label = Label(window_credits, text="Programmer", bg="light blue", font=('consolas', 50))
    label.grid(row=3, column=0)

    label = Label(window_credits, text="Treeisme", bg="light blue", font=('consolas', 50))
    label.grid(row=3, column=1)

    label = Label(window_credits, text="Music", bg="light blue", font=('consolas', 50))
    label.grid(row=4, column=0)

    label = Label(window_credits, text="Bergie", bg="light blue", font=('consolas', 50))
    label.grid(row=4, column=1)

def main_menu(frame):
    global frame1, label_title, easy_button, medium_button, hard_button, mp_button, credits_button, exit_button
    frame.destroy()
    label_title = Label(text="Tic-Tac-Toe Menu", font=('Times New Roman', 50))
    label_title.pack(side="top")

    frame1 = Frame(root)
    frame1.pack()

    easy_button = Button(frame1, text="AI Easy", font=('consolas', 20), command=ai_easy, height=2, width=12)
    easy_button.pack()

    medium_button = Button(frame1, text="AI Medium", font=('consolas', 20), command=ai_medium, height=2, width=12)
    medium_button.pack()

    hard_button = Button(frame1, text="AI Hard", font=('consolas', 20), command=ai_hard, height=2, width=12)
    hard_button.pack()

    mp_button = Button(frame1, text="Multiplayer", font=('consolas', 20), command=multi_player, height=2, width=12)
    mp_button.pack()

    credits_button = Button(frame1, text="Credits", font=('consolas', 20), command=credit_screen, height=2, width=12)
    credits_button.pack()

    exit_button = Button(frame1, text="Exit", font=('consolas', 20), command=end_game, height=2, width=12)
    exit_button.pack()

def end_game():
    window_end_game = Toplevel()
    window_end_game.title("Confirm")
    window_end_game.config(bg="#2697B6")
    window_end_game.geometry("1000x500")
    window_end_game.overrideredirect(1)

    label = Label(window_end_game, bg="#2697B6", text="Are you sure you want to exit", font=('Times New Roman', 50))
    label.pack(side="top")

    button_yes = Button(window_end_game, bg="#8bd3e1", text="Yes", font=('Times New Roman', 50), command=lambda: root.destroy(), height=2, width=12)
    button_yes.pack(side="left")

    button_no = Button(window_end_game, bg="#8bd3e1", text="No", font=('Times New Roman', 50), command=lambda: window_end_game.destroy(), height=2, width=12)
    button_no.pack(side="right")

    center_window(window_end_game)

    window_end_game.mainloop()

def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

# where is the music that you want played
    # the r turns it into a string literal because it doesnt like \
music_filename = "Tic-Tac-ToeInstra2.mp3"
SOUND_FILE = os.path.join(os.path.dirname(__file__), music_filename)

# even tho we imported pygame we still need to include pygame into the event call
# init = initialize pygame mixer
pygame.mixer.init()
# load the sound
pygame.mixer.music.load(SOUND_FILE)
# change the volume of the music.
pygame.mixer.music.set_volume(0.05)
# set how many times the music loops and when it starts
pygame.mixer.music.play(loops=-1, start=0)

root = Tk()
root.title("Tic-Tac-Toe")
root.geometry("1000x1000")
root.config(bg="Light Blue")

x_win = 0
o_win = 0
tie_win = 0
players = ["X", "O"]
player = random.choice(players)
label_title = Label(text="Tic-Tac-Toe Menu", font=('Times New Roman', 50))
label_title.pack(side="top")

frame1=Frame(root)
frame1.pack()

easy_button = Button(frame1, text="AI Easy", font=('consolas', 20), command=ai_easy, height=2, width=12)
easy_button.pack()

medium_button = Button(frame1, text="AI Medium", font=('consolas', 20), command=ai_medium, height=2, width=12)
medium_button.pack()

hard_button = Button(frame1, text="AI Hard", font=('consolas', 20), command=ai_hard, height=2, width=12)
hard_button.pack()

mp_button = Button(frame1, text="Multiplayer", font=('consolas', 20), command=multi_player, height=2, width=12)
mp_button.pack()

credits_button = Button(frame1, text="Credits", font=('consolas', 20), command=credit_screen, height=2, width=12)
credits_button.pack()

exit_button = Button(frame1, text="Exit", font=('consolas', 20), command=end_game, height=2, width=12)
exit_button.pack()

center_window(root)

root.mainloop()
