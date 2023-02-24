"""
Fakime Nur Ozdemir
jan 2023
2048 version 1.0 """

import tkinter
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("2048 by Faki")
window.geometry("495x700+30+80")
window.config(background="#888888")

#variables
intervaley = 90
intervalex = 90


#frame1
frame1 = Frame(window, highlightbackground="black", highlightthickness=2)
frame1.place(x=320, y=80)

lbl_2048 = Label(frame1, text="2048", bg="#4F7942", height=2, width=17, fg="white")
lbl_2048.pack()

#frame2
frame2 = Frame(window, highlightbackground="#4F7942", highlightthickness=3)
frame2.place(x=300, y=130)

lbl_scr = Label(frame2, text="Score", background="#888888", height=3, width=9, fg="black")
lbl_scr.pack()

#frame3
frame3 = Frame(window, highlightbackground="#4F7942", highlightthickness=3)
frame3.place(x=400, y=130)

lbl_tpscr = Label(frame3, text="Top Score", background="#888888", height=3, width=9, fg="black")
lbl_tpscr.pack()



#list de couleurs
list_colors = {
    0: "grey",
    2: "#EA9999",
    4: "#F6B26B",
    8: "#B6D7A8",
    16: "#FFE599",
    32: "#C27BA0",
    64: "#A2C4C9",
    128: "#597EAA",
    256: "#B4A7D6",
    512: "#F9CB9C",
    1024: "#D5A6BD",
    2048: "#9FC5F8",
    4096: "#E69138",
    8192: "#8E7CC3",
}


numbers = [[8192, 0, 0, 0], [4, 512, 16, 4096], [256, 1024, 2, 32], [128, 2048, 64, 8]]
labels = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]

for line in range(len(numbers)):
    for col in range(len(numbers[line])):
         labels[line][col] = Label(text="", width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 22), highlightbackground="black", highlightthickness=1)
         labels[line][col].place(x=70 + intervalex * col, y=250 + intervaley * line)
#functions
#div icin daha cok yorum eklemelisin
def display ():
    for line in range(len(numbers)):
        for col in range(len(numbers[line])):
            if numbers[line][col] == 0 :
                labels[line][col].config(text="", bg=list_colors[numbers[line][col]])
            else:
                labels[line][col].config(text=numbers[line][col], bg=list_colors[numbers[line][col]])

def new_button():
    global numbers
    numbers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 4]]
    display()

#button (aide Carlos>aide Athos)
new_button = tkinter.Button(window,command=new_button, text="Nouveau", highlightbackground="#274E13", fg="#888888")
new_button.place(x=395, y=200)


display()
window.mainloop()
