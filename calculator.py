from tkinter import *

win=Tk()
win.title('calculator')
win.geometry('300x300')
expression=''
#update expression
def update(btn):
    global expression
    expression+=str(btn)
    inputtxt.set(expression)
#pressequal
def pressequal():
    try:
        global expression
        total=str(eval(expression))
        inputtxt.set(total)
        expression=''
    except:
        inputtxt.set('error')
        expression=''
#clear
def clear():
    global expression
    expression=''
    inputtxt.set('')

inputtxt=StringVar()
screen=Entry(win,font=('arial',20),justify='right',textvariable=inputtxt)
screen.place(x=0,y=0,relwidth=1,relheight=0.2)

b1=Button(win,text='1',font=('arial',20), command=lambda: update(1)).place(x=0,rely=0.2,relwidth=0.25,relheight=0.2,)
b2=Button(win,text='2',font=('arial',20), command=lambda: update(2)).place(relx=0.25,rely=0.2,relwidth=0.25,relheight=0.2)
b3=Button(win,text='3',font=('arial',20), command=lambda: update(3)).place(relx=0.5,rely=0.2,relwidth=0.25,relheight=0.2)
bplus=Button(win,text='+',font=('arial',20), command=lambda: update('+')).place(relx=0.75,rely=0.2,relwidth=0.25,relheight=0.2)

b4=Button(win,text='4',font=('arial',20), command=lambda: update(4)).place(x=0,rely=0.36,relwidth=0.25,relheight=0.2)
b5=Button(win,text='5',font=('arial',20), command=lambda: update(5)).place(relx=0.25,rely=0.36,relwidth=0.25,relheight=0.2)
b6=Button(win,text='6',font=('arial',20), command=lambda: update(6)).place(relx=0.5,rely=0.36,relwidth=0.25,relheight=0.2)
bsub=Button(win,text='-',font=('arial',20), command=lambda: update('-')).place(relx=0.75,rely=0.36,relwidth=0.25,relheight=0.2)

b7=Button(win,text='7',font=('arial',20), command=lambda: update(7)).place(x=0,rely=0.52,relwidth=0.25,relheight=0.2)
b8=Button(win,text='8',font=('arial',20), command=lambda: update(8)).place(relx=0.25,rely=0.52,relwidth=0.25,relheight=0.2)
b9=Button(win,text='9',font=('arial',20), command=lambda: update(9)).place(relx=0.5,rely=0.52,relwidth=0.25,relheight=0.2)
bmul=Button(win,text='*',font=('arial',20), command=lambda: update('*')).place(relx=0.75,rely=0.52,relwidth=0.25,relheight=0.2)

bdecimal=Button(win,text='.',font=('arial',20), command=lambda: update('.')).place(x=0,rely=0.68,relwidth=0.25,relheight=0.2)
b0=Button(win,text='0',font=('arial',20), command=lambda: update(0)).place(relx=0.25,rely=0.68,relwidth=0.25,relheight=0.2)
bequal=Button(win,text='=',font=('arial',20), command=lambda: pressequal()).place(relx=0.5,rely=0.68,relwidth=0.25,relheight=0.2)
bdiv=Button(win,text='/',font=('arial',20), command=lambda: update('/')).place(relx=0.75,rely=0.68,relwidth=0.25,relheight=0.2)

bclear=Button(win,text='clear',font=('arial',20), command=lambda: clear()).place(x=0,rely=0.84,relwidth=1,relheight=0.2)
