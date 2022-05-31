from tkinter import*
import random
from PIL import Image,ImageTk
root=Tk()
root.title("poka")
root.geometry("600x400")
root.configure(background="black")

img = ImageTk.PhotoImage(Image.open("Dice.jpg"))
pica = ImageTk.PhotoImage(Image.open("pica (1).jpg"))
pica1 = ImageTk.PhotoImage(Image.open("pica (2).jpg"))
pica2 = ImageTk.PhotoImage(Image.open("pica (3).jpg"))
pica3 = ImageTk.PhotoImage(Image.open("pica (4).jpg"))
pica4 = ImageTk.PhotoImage(Image.open("pica (5).jpg"))
pica5 = ImageTk.PhotoImage(Image.open("pica (6).jpg"))
pica6 = ImageTk.PhotoImage(Image.open("pica (7).jpg"))
pica7 = ImageTk.PhotoImage(Image.open("pica (8).jpg"))
pica8 = ImageTk.PhotoImage(Image.open("pica (9).jpg"))
pica9 = ImageTk.PhotoImage(Image.open("pica (10).jpg"))
pica10= ImageTk.PhotoImage(Image.open("pica (11).jpg"))
pica11= ImageTk.PhotoImage(Image.open("pica (12).jpg"))
pica12= ImageTk.PhotoImage(Image.open("pica (13).jpg"))

list=[pica,pica1,pica2,pica3,pica4,pica5,pica6,pica7,pica8,pica9,pica10,pica11,pica12]
random_no=random.randint(0,12)
label1=Label(root,text="Player1",bg="#345beb",fg="white")
label1.place(relx = 0.1, rely =0.2, anchor = CENTER)
label3=Label(root,bg="#ff0000",fg="white")
label3.place(relx = 0.1, rely =0.3, anchor = CENTER)

label2=Label(root,text="Player2",bg="#345beb",fg="white")
label2.place(relx = 0.9, rely =0.2, anchor = CENTER)
label4=Label(root,bg="#ff0000",fg="white")
label4.place(relx = 0.9, rely =0.3, anchor = CENTER)

player1_score=0
player2_score=0

def player1():
    random_no=random.randint(1,6)
    global player1_score
    label3["text"]="player1 dice score= "+str(random_no)
    player1_score=player1_score+random_no
    label5=Label(root,image=list[random_no],bg="#ff7300",fg="white")
    label5.place(relx = 0.5, rely =0.5, anchor = CENTER)
def player2():
     random_no=random.randint(1,6)
     global player2_score
     label4["text"]="player2 dice score= "+str(random_no)
     player2_score=player2_score+random_no
     label5=Label(root,image=list[random_no],bg="#ff7300",fg="white")
     label5.place(relx = 0.5, rely =0.5, anchor = CENTER)
button1=Button(root,image=img,command=player1,anchor = CENTER)
button1.place(relx = 0.1, rely =0.5, anchor = CENTER)

button2=Button(root,image=img,command=player2,anchor = CENTER)
button2.place(relx = 0.9, rely =0.5, anchor = CENTER)

root.mainloop()