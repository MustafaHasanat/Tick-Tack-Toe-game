from tkinter import *
from random import *


def Reset():
    vicWind.state('withdrawn')
    wind.deiconify()
    Clear()


def Exit():
    vicWind.destroy()
    wind.destroy()


def checkOrder(Xstate, Ostate, TxtList):
    global order, X_state, O_state, txtList, mode
    if (order == "p1") & (X_state[Xstate] == 0) & (O_state[Ostate] == 0) & (mode == "pvp"):
        txtList[TxtList].set("X")
        order = "p2"
        X_state[Xstate] = 1
        Check()
    elif (order == "p2") & (O_state[Ostate] == 0) & (X_state[Xstate] == 0) & (mode == "pvp"):
        txtList[TxtList].set("O")
        order = "p1"
        O_state[Ostate] = 1
        Check()
    elif (order == "p1") & (X_state[Xstate] == 0) & (O_state[Ostate] == 0) & (mode == "dump"):
        txtList[TxtList].set("X")
        order = "p2"
        X_state[Xstate] = 1
        Check()
        # --------------------------
        available = unPlayedBtns()
        chosen = choice(available)
        txtList[chosen].set("O")
        order = "p1"
        O_state[chosen] = 1
        Check()
    elif (order == "p1") & (X_state[Xstate] == 0) & (O_state[Ostate] == 0) & (mode == "undefeatable"):
        txtList[TxtList].set("X")
        order = "p2"
        X_state[Xstate] = 1
        Check()
        # --------------------------
        chosen = study()
        txtList[chosen].set("O")
        order = "p1"
        O_state[chosen] = 1
        Check()


def Check():
    global X_state, O_state, winningCase
    c = 1
    for i in ["X", "O"]:
        if c == 1:
            myList = X_state
            c += 1
        else:
            myList = O_state
#       ----------------------
        if (myList[0] == 1) & (myList[1] == 1) & (myList[2] == 1):
            Victory(i)
            winningCase = 1
        elif (myList[3] == 1) & (myList[4] == 1) & (myList[5] == 1):
            Victory(i)
            winningCase = 2
        elif (myList[6] == 1) & (myList[7] == 1) & (myList[8] == 1):
            Victory(i)
            winningCase = 3
        elif (myList[0] == 1) & (myList[3] == 1) & (myList[6] == 1):
            Victory(i)
            winningCase = 4
        elif (myList[1] == 1) & (myList[4] == 1) & (myList[7] == 1):
            Victory(i)
            winningCase = 5
        elif (myList[2] == 1) & (myList[5] == 1) & (myList[8] == 1):
            Victory(i)
            winningCase = 6
        elif (myList[0] == 1) & (myList[4] == 1) & (myList[8] == 1):
            Victory(i)
            winningCase = 7
        elif (myList[2] == 1) & (myList[4] == 1) & (myList[6] == 1):
            Victory(i)
            winningCase = 8


def Victory(vector):
    global order, labelTxt1
    Clear()
    if vector == "X":
        vicWind.state('normal')
        vicWind.deiconify()
        wind.withdraw()
        labelTxt1.set("Player 1 (X) is the WINNER !!!")
    elif vector == "O":
        vicWind.state('normal')
        vicWind.deiconify()
        wind.withdraw()
        labelTxt1.set("Player 2 (O) is the WINNER !!!")


def Clear():
    global X_state, O_state, txtList, winningCase, order
    X_state, O_state = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        txtList[i].set("")
    winningCase, order = 10, "p1"


def modeChange(MODE):
    global mode
    Reset()
    if MODE == "pvp":
        mode = "pvp"
    elif MODE == "dump":
        mode = "dump"
    elif MODE == "undefeatable":
        mode = "undefeatable"


def unPlayedBtns():
    global mode, winningCase, order, X_state, O_state, AVAILABLE
    AVAILABLE, availableXBtns, availableOBtns, start, end = [], [], [], 0, 9
    for j in range(9):
        try:
            elementX = X_state.index(0, start, end)
            availableXBtns.append(elementX)
            start = elementX + 1
        except:
            pass
    start, end = 0, 9
    for ii in range(9):
        try:
            elementO = O_state.index(0, start, end)
            availableOBtns.append(elementO)
            start = elementO + 1
        except:
            pass
    for jj in availableXBtns:
        try:
            available = availableOBtns.index(jj)
            AVAILABLE.append(availableOBtns[available])
        except:
            pass

    return AVAILABLE


def study():
    available = unPlayedBtns()


    return 0


wind = Tk()
wind.title("Tick Tack Toe")
wind.geometry("486x502+400+80")
wind.resizable(0, 0)

vicWind = Toplevel()
vicWind.title("The Victory !!!")
vicWind.geometry("400x150+450+200")
vicWind.resizable(0, 0)
vicWind.config(bg="#ffc400")
vicWind.state('withdrawn')

labelTxt1 = StringVar()
labelTxt1.set("")
lab1 = Label(vicWind, textvariable=labelTxt1, width=30, height=3,
             bg="#ffc400", fg="#263238", font=("times", 15, 'bold'),).pack(side=TOP, fill=X)
btn1 = Button(vicWind, text="Reset", width=10, height=1, activebackground="#f50057", cursor="hand2",
              bg="#e65100", fg="#263238", command=Reset, font=("times", 15, 'bold'),).pack(side=LEFT)
btn2 = Button(vicWind, text="Exit", width=10, height=1, activebackground="#f50057", cursor="hand2",
              bg="#e65100", fg="#263238", command=Exit, font=("times", 15, 'bold'),).pack(side=RIGHT)

mainMenu = Menu(wind, bg="red")

game = Menu(wind, bg="#aed581")
mainMenu.add_cascade(label="Game", menu=game)

gameMode = Menu(wind, bg="#689f38")
cpu = Menu(wind, bg="#558b2f")

game.add_cascade(label="Game Mode", menu=gameMode)
gameMode.add_command(label="PvP", command=lambda: modeChange("pvp"))
gameMode.add_cascade(label="Player vs CPU", menu=cpu)
cpu.add_command(label="Dump", command=lambda: modeChange("dump"))
cpu.add_command(label="Undefeatable", command=lambda: modeChange("undefeatable"))
game.add_separator()
game.add_command(label="Reset", command=Clear)
game.add_command(label="Exit", command=wind.quit)

wind.config(bg="#607d8b", menu=mainMenu)

order = "p1"
mode = "pvp"
winningCase = 10  # No winner
X_state, O_state, txtList = [], [], []
w, h, fontSize, BG, FG, ABG = 3, 1, 60, "#ffc400", "#607d8b", "#f50057"
for i in range(9):
    X_state.append(0)
    O_state.append(0)
    txtList.append(StringVar())
xx, yy, xSep, ySep = 0, 0, 165, 170

btn0 = Button(wind, width=w, height=h, font=('italic', fontSize, 'bold'), bg=BG, fg=FG, textvariable=txtList[0],
              command=lambda: checkOrder(0, 0, 0), activebackground=ABG, cursor="hand2")
btn0.place(x=xx, y=yy)
yy += ySep
btn1 = Button(wind, width=w, height=h, font=('italic', fontSize, 'bold'), bg=BG, fg=FG, textvariable=txtList[1],
              command=lambda: checkOrder(1, 1, 1), activebackground=ABG, cursor="hand2")
btn1.place(x=xx, y=yy)
yy += ySep
btn2 = Button(wind, width=w, height=h, font=('italic', fontSize, 'bold'), bg=BG, fg=FG, textvariable=txtList[2],
              command=lambda: checkOrder(2, 2, 2), activebackground=ABG, cursor="hand2")
btn2.place(x=xx, y=yy)
yy = 0
xx += xSep
btn3 = Button(wind, width=w, height=h, font=('italic', fontSize, 'bold'), bg=BG, fg=FG, textvariable=txtList[3],
              command=lambda: checkOrder(3, 3, 3), activebackground=ABG, cursor="hand2")
btn3.place(x=xx, y=yy)
yy += ySep
btn4 = Button(wind, width=w, height=h, font=('italic', fontSize, 'bold'), bg=BG, fg=FG, textvariable=txtList[4],
              command=lambda: checkOrder(4, 4, 4), activebackground=ABG, cursor="hand2")
btn4.place(x=xx, y=yy)
yy += ySep
btn5 = Button(wind, width=w, height=h, font=('italic', fontSize, 'bold'), bg=BG, fg=FG, textvariable=txtList[5],
              command=lambda: checkOrder(5, 5, 5), activebackground=ABG, cursor="hand2")
btn5.place(x=xx, y=yy)
yy = 0
xx += xSep
btn6 = Button(wind, width=w, height=h, font=('italic', fontSize, 'bold'), bg=BG, fg=FG, textvariable=txtList[6],
              command=lambda: checkOrder(6, 6, 6), activebackground=ABG, cursor="hand2")
btn6.place(x=xx, y=yy)
yy += ySep
btn7 = Button(wind, width=w, height=h, font=('italic', fontSize, 'bold'), bg=BG, fg=FG, textvariable=txtList[7],
              command=lambda: checkOrder(7, 7, 7), activebackground=ABG, cursor="hand2")
btn7.place(x=xx, y=yy)
yy += ySep
btn8 = Button(wind, width=w, height=h, font=('italic', fontSize, 'bold'), bg=BG, fg=FG, textvariable=txtList[8],
              command=lambda: checkOrder(8, 8, 8), activebackground=ABG, cursor="hand2")
btn8.place(x=xx, y=yy)


wind.mainloop()
