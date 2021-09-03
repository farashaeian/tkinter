from tkinter import *
from random import randint

win=Tk()
win.title('Rock Paper Scissors Game')
win.geometry('700x600')
win.resizable(0,0)

#Buttons for rock,paper,scissors
#commands will be inserted after difinition of the function
rock=Button(win, text='Rock', font=('arial 25 bold'), justify='center', fg='brown')
rock.place(relx=0.04, rely=0.65, width=200, height=180)
paper=Button(win, text='Paper', font=('arial 25 bold'), justify='center', fg='blue')
paper.place(x=256, rely=0.65, width=200, height=180)
scissors=Button(win, text='Scissors', font=('arial 25 bold'), justify='center', fg='black')
scissors.place(x=472, rely=0.65, width=200, height=180)

#rock functoin
def Rock():
    #your choice:show on label & disable your options
    Your_choice=Label(win, text='Rock', font=('arial 25 bold'), justify='center', fg='black', bg='white')
    Your_choice.place(relx=0.04, y=170, width=200 , height=50)
    paper.config(state= "disabled")
    scissors.config(state= "disabled")
    #computer choice:show on label & compare & show the winner
    d={0:'Rock', 1:'Paper', 2:'Scissors'}
    choice=randint(0,2)
    My_choice=Label(win, text=d[choice], font=('arial 25 bold'), justify='center', fg='black', bg='white')
    My_choice.place(x=472, y=170, width=200 , height=50)
    #compare
    if d[choice]=='Paper':
        w='Me'
    elif d[choice]=='Rock' :
        w='None'
    else :
        w='You'
    #show winner
    winner_final=Label(win, text=w, font=('arial 25 bold'), justify='center', fg='white', bg='black')
    winner_final.place(x=300, y=290, width=100 , height=50)
#insert command in buttons 
rock.config(command=Rock)

#Paper function
def Paper():
    #your choice:show on label & disable your options
    Your_choice=Label(win, text='Paper', font=('arial 25 bold'), justify='center', fg='black', bg='white')
    Your_choice.place(relx=0.04, y=170, width=200 , height=50)
    rock.config(state= "disabled")
    scissors.config(state= "disabled")
    #computer choice:show on label & compare & show the winner
    d={0:'Rock', 1:'Paper', 2:'Scissors'}
    choice=randint(0,2)
    My_choice=Label(win, text=d[choice], font=('arial 25 bold'), justify='center', fg='black', bg='white')
    My_choice.place(x=472, y=170, width=200 , height=50)
    #compare
    if d[choice]=='Scissors':
        w='Me'
    elif d[choice]=='Paper' :
        w='None'
    else :
        w='You'
    #show winner
    winner_final=Label(win, text=w, font=('arial 25 bold'), justify='center', fg='white', bg='black')
    winner_final.place(x=300, y=290, width=100 , height=50)
#insert command in buttons
paper.config(command=Paper)

#Scissors function
def Scissors():
    #your choice:show on label & disable your options
    Your_choice=Label(win, text='Scissors', font=('arial 25 bold'), justify='center', fg='black', bg='white')
    Your_choice.place(relx=0.04, y=170, width=200 , height=50)
    rock.config(state= "disabled")
    paper.config(state= "disabled")
    #computer choice:show on label & compare & show the winner
    d={0:'Rock', 1:'Paper', 2:'Scissors'}
    choice=randint(0,2)
    My_choice=Label(win, text=d[choice], font=('arial 25 bold'), justify='center', fg='black', bg='white')
    My_choice.place(x=472, y=170, width=200 , height=50)
    #compare
    if d[choice]=='Rock':
        w='Me'
    elif d[choice]=='Scissors' :
        w='None'
    else :
        w='You'
    #show winner
    winner_final=Label(win, text=w, font=('arial 25 bold'), justify='center', fg='white', bg='black')
    winner_final.place(x=300, y=290, width=100 , height=50)
#insert command in buttons
scissors.config(command=Scissors)

#start button
start_btn=Button(win, text='Start', font=('arial 25 bold'), justify='center', fg='white', bg='green')
start_btn.place(relx=0.36, y=30, width=200 , height=50)

#start function
def start():
   rock.config(state= "active")
   paper.config(state= "active")
   scissors.config(state= "active")
   winner=Label(win, text='?', font=('arial 25 bold'), justify='center', fg='white', bg='black').place(x=300, y=290, width=100 , height=50)
   Your_choice=Label(win, text='1st player', font=('arial 25 bold'), justify='center', fg='black', bg='white')
   Your_choice.place(relx=0.04, y=170, width=200 , height=50)
   My_choice=Label(win, text='2nd player', font=('arial 25 bold'), justify='center', fg='black', bg='white')
   My_choice.place(x=472, y=170, width=200 , height=50)

#insert command in start button
start_btn.config(command=start)

#labels
winneris=Label(win, text='winner is :', font=('arial 25 bold'), justify='center', fg='white', bg='red').place(relx=0.36, y=230, width=200 , height=50)
winner=Label(win, text='?', font=('arial 25 bold'), justify='center', fg='white', bg='black').place(x=300, y=290, width=100 , height=50)

Label(win, text='Your choice', font=('arial 25 bold'), justify='center', fg='white', bg='black').place(relx=0.04, y=110, width=200 , height=50)
Label(win, text='My choice', font=('arial 25 bold'), justify='center', fg='white', bg='black').place(x=472, y=110, width=200 , height=50)

Your_choice=Label(win, text='1st player', font=('arial 25 bold'), justify='center', fg='black', bg='white')
Your_choice.place(relx=0.04, y=170, width=200 , height=50)
My_choice=Label(win, text='2nd player', font=('arial 25 bold'), justify='center', fg='black', bg='white')
My_choice.place(x=472, y=170, width=200 , height=50)


