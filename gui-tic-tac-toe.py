from tkinter import Tk, Button, Label
from tkinter.messagebox import showinfo, askokcancel

def check(button):
    global turn, opp
    finished = won = False
    if button1["text"] == button2["text"] == button3["text"] != " " or  button4["text"] == button5["text"] == button6["text"] != " " or button7["text"] == button8["text"] == button9["text"] != " " or button1["text"] == button4["text"] == button7["text"] != " " or button2["text"] == button5["text"] == button8["text"] != " " or button3["text"] == button6["text"] == button9["text"] != " " or button1["text"] == button5["text"] == button9["text"] != " " or button3["text"] == button5["text"] == button7["text"] != " ": finished = won = True
    elif button1["text"] != " " and button2["text"] != " " and button3["text"] != " " and button4["text"] != " " and button5["text"] != " " and button6["text"] != " " and button7["text"] != " " and button8["text"] != " " and button9["text"] != " ": finished = True
    if finished:
        if won: showinfo(f"Dear {button['text']}", "You won the game!")
        else: showinfo("Tie", "The game is tie.")
        if askokcancel("Restart", "Restart the game?"):
            for widget in [button1, button2, button3, button4, button5, button6, button7, button8, button9]: widget.config(text = " ")
            turn, opp = "X", "O"
        else:
            root.destroy()    
            return
    turn_label.config(text = f"Turn:  {turn}")

def button1_func():
    global turn, opp
    if button1["text"] == " ":
        button1.config(text = turn)
        turn, opp = opp, turn
        check(button1)

def button2_func():
    global turn, opp
    if button2["text"] == " ":
        button2.config(text = turn)
        turn, opp = opp, turn
        check(button2)

def button3_func():
    global turn, opp
    if button3["text"] == " ":
        button3.config(text = turn)
        turn, opp = opp, turn
        check(button3)
        
def button4_func():
    global turn, opp
    if button4["text"] == " ":
        button4.config(text = turn)
        turn, opp = opp, turn
        check(button4)

def button5_func():
    global turn, opp
    if button5["text"] == " ":
        button5.config(text = turn)
        turn, opp = opp, turn
        check(button5)

def button6_func():
    global turn, opp
    if button6["text"] == " ":
        button6.config(text = turn)
        turn, opp = opp, turn
        check(button6)
        
def button7_func():
    global turn, opp
    if button7["text"] == " ":
        button7.config(text = turn)
        turn, opp = opp, turn
        check(button7)

def button8_func():
    global turn, opp
    if button8["text"] == " ":
        button8.config(text = turn)
        turn, opp = opp, turn
        check(button8)

def button9_func():
    global turn, opp
    if button9["text"] == " ":
        button9.config(text = turn)
        turn, opp = opp, turn
        check(button9)


root = Tk()
root.title("Tic Tac Toe")
root.geometry("544x626")
root.resizable(0, 0)
turn, opp = "X", "O"
turn_label = Label(root, text = f"Turn:  {turn}", font = ('Times 26 bold'))
turn_label.place(x = 275, y = 25, anchor = "center")
button1 = Button(root, text = " ", height = 4, width = 8, relief = "solid", bd = 5, font = ('Times 26 bold'), command = button1_func)
button1.place(x = 0, y = 50)
button2 = Button(root, text = " ", height = 4, width = 8, relief = "solid", bd = 5, font = ('Times 26 bold'), command = button2_func)
button2.place(x = 180, y = 50)
button3 = Button(root, text = " ", height = 4, width = 8, relief = "solid", bd = 5, font = ('Times 26 bold'), command = button3_func)
button3.place(x = 360, y = 50)
button4 = Button(root, text = " ", height = 4, width = 8, relief = "solid", bd = 5, font = ('Times 26 bold'), command = button4_func)
button4.place(x = 0, y = 240)
button5 = Button(root, text = " ", height = 4, width = 8, relief = "solid", bd = 5, font = ('Times 26 bold'), command = button5_func)
button5.place(x = 180, y = 240)
button6 = Button(root, text = " ", height = 4, width = 8, relief = "solid", bd = 5, font = ('Times 26 bold'), command = button6_func)
button6.place(x = 360, y = 240)
button7 = Button(root, text = " ", height = 4, width = 8, relief = "solid", bd = 5, font = ('Times 26 bold'), command = button7_func)
button7.place(x = 0, y = 430)
button8 = Button(root, text = " ", height = 4, width = 8, relief = "solid", bd = 5, font = ('Times 26 bold'), command = button8_func)
button8.place(x = 180, y = 430)
button9 = Button(root, text = " ", height = 4, width = 8, relief = "solid", bd = 5, font = ('Times 26 bold'), command = button9_func)
button9.place(x = 360, y = 430)
root.mainloop()
