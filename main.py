from tkinter import *
from tkinter import messagebox


# Tic Tac Toe game
def restart():

    global count, turn, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, text, b_restart, b_quit

    btn1.grid(row=0, column=1)  # white
    btn2.grid(row=0, column=2)  # black
    btn3.grid(row=0, column=3)  # white

    btn4.grid(row=1, column=1)  # black
    btn5.grid(row=1, column=2)  # white
    btn6.grid(row=1, column=3)  # black

    btn7.grid(row=2, column=1)  # white
    btn8.grid(row=2, column=2)  # black
    btn9.grid(row=2, column=3)  # white

    btn1["text"] = " "
    btn2["text"] = " "
    btn3["text"] = " "
    btn4["text"] = " "
    btn5["text"] = " "
    btn6["text"] = " "
    btn7["text"] = " "
    btn8["text"] = " "
    btn9["text"] = " "
    count = 0
    turn = True


winner = " "


def check_win():
    global winner
    print("Checking win")
    if (btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X") \
            or (btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X") \
            or (btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X") \
            or (btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X") \
            or (btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X") \
            or (btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X") \
            or (btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X") \
            or (btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X"):
        winner = "X"
        messagebox.showinfo(title="Notification", message=f"The winner is{winner}!\n Restarting...")
        restart()
    elif (btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O") \
            or (btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O") \
            or (btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O") \
            or (btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O") \
            or (btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O") \
            or (btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O") \
            or (btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O") \
            or (btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O"):
        winner = "O"
        messagebox.showinfo(title="Notification", message=f"The winner is{winner}!\n Restarting...")
        restart()


def on_clicks(btn):
    global turn, count
    print(f"turn = {turn} count = {count}")
    if btn["text"] == " ":
        if turn:
            btn["text"] = 'X'
            turn = False
        else:
            btn["text"] = 'O'
            turn = True

        count += 1
        check_win()
        if count >= 9:
            restart()
            messagebox.showinfo(title="Notification", message="No more possible moves. Game has restarted.")


window = Tk()
window.configure(bg="white")
window.title("Tic Tac Toe")
window.geometry('576x536+520+100')

turn = True  # if turn = True it's the X turn else if turn = False its O turn.
count = 0  # count of moves (max is 9)

btn1 = Button(master=window, command=lambda: on_clicks(btn1), font=("Impact", 40), fg="black", bg="white", height=2,
              width=7, text=" ")
btn2 = Button(master=window, command=lambda: on_clicks(btn2), font=("Impact", 40), fg="black", bg="white", height=2,
              width=7, text=" ")
btn3 = Button(master=window, command=lambda: on_clicks(btn3), font=("Impact", 40), fg="black", bg="white", height=2,
              width=7, text=" ")

btn4 = Button(master=window, command=lambda: on_clicks(btn4), font=("Impact", 40), fg="black", bg="white", height=2,
              width=7, text=" ")
btn5 = Button(master=window, command=lambda: on_clicks(btn5), font=("Impact", 40), fg="black", bg="white", height=2,
              width=7, text=" ")
btn6 = Button(master=window, command=lambda: on_clicks(btn6), font=("Impact", 40), fg="black", bg="white", height=2,
              width=7, text=" ")

btn7 = Button(master=window, command=lambda: on_clicks(btn7), font=("Impact", 40), fg="black", bg="white", height=2,
              width=7, text=" ")
btn8 = Button(master=window, command=lambda: on_clicks(btn8), font=("Impact", 40), fg="black", bg="white", height=2,
              width=7, text=" ")
btn9 = Button(master=window, command=lambda: on_clicks(btn9), font=("Impact", 40), fg="black", bg="white", height=2,
              width=7, text=" ")

btn1.grid(row=0, column=1)  # white
btn2.grid(row=0, column=2)  # black
btn3.grid(row=0, column=3)  # white

btn4.grid(row=1, column=1)  # black
btn5.grid(row=1, column=2)  # white
btn6.grid(row=1, column=3)  # black

btn7.grid(row=2, column=1)  # white
btn8.grid(row=2, column=2)  # black
btn9.grid(row=2, column=3)  # white

window.mainloop()
