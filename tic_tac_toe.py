from tkinter import *

win=Tk()
win.title('tic tac toe')
win.geometry('500x500')
win.resizable(0,0)

e1=StringVar()
E1=Entry(win, textvariable=e1, font=('arial 40 bold'), justify='center').place(relx=0.2,rely=0.2,relwidth=0.2,relheight=0.2)
e2=StringVar()
E2=Entry(win, textvariable=e2, font=('arial 40 bold'), justify='center').place(relx=0.4,rely=0.2,relwidth=0.2,relheight=0.2)
e3=StringVar()
E3=Entry(win, textvariable=e3, font=('arial 40 bold'), justify='center').place(relx=0.6,rely=0.2,relwidth=0.2,relheight=0.2)
e4=StringVar()
E4=Entry(win, textvariable=e4, font=('arial 40 bold'), justify='center').place(relx=0.2,rely=0.4,relwidth=0.2,relheight=0.2)
e5=StringVar()
E5=Entry(win, textvariable=e5, font=('arial 40 bold'), justify='center').place(relx=0.4,rely=0.4,relwidth=0.2,relheight=0.2)
e6=StringVar()
E6=Entry(win, textvariable=e6, font=('arial 40 bold'), justify='center').place(relx=0.6,rely=0.4,relwidth=0.2,relheight=0.2)
e7=StringVar()
E7=Entry(win, textvariable=e7, font=('arial 40 bold'), justify='center').place(relx=0.2,rely=0.6,relwidth=0.2,relheight=0.2)
e8=StringVar()
E8=Entry(win, textvariable=e8, font=('arial 40 bold'), justify='center').place(relx=0.4,rely=0.6,relwidth=0.2,relheight=0.2)
e9=StringVar()
E9=Entry(win, textvariable=e9, font=('arial 40 bold'), justify='center').place(relx=0.6,rely=0.6,relwidth=0.2,relheight=0.2)

def win_msg(x):
    result=Label(win, text=f'{x.get()} wins',font=('arial 25 bold'),fg='red').place(relx=0.33,rely=0.015,relwidth=0.35,relheight=0.15)    

def finish():
    l=['x','X','o','O','']
    s=['x','X','o','O']
    
    if ((e1.get() not in l)or(e2.get() not in l)or(e3.get() not in l)or(e4.get() not in l)or(e5.get() not in l)or(e6.get() not in l)or(e7.get() not in l)or(e8.get() not in l)or(e9.get() not in l)):
        Label(win, text='Unvalid Item \n Start Again!!!',font=('arial 18 bold'), justify='center').place(relx=0.33,rely=0.015,relwidth=0.35,relheight=0.15)
        
    else:
        if ((e1.get()==e2.get()==e3.get())&(e1.get() in s)&(e2.get() in s)&(e3.get() in s)):
            win_msg(e1)
            
        elif ((e4.get()==e5.get()==e6.get())&(e4.get() in s)&(e5.get() in s)&(e6.get() in s)):
            win_msg(e4)

        elif ((e7.get()==e8.get()==e9.get())&(e7.get() in s)&(e8.get() in s)&(e9.get() in s)):
            win_msg(e7)
            
        elif ((e1.get()==e4.get()==e7.get())&(e1.get() in s)&(e4.get() in s)&(e7.get() in s)):
            win_msg(e1)
            
        elif ((e2.get()==e5.get()==e8.get())&(e2.get() in s)&(e5.get() in s)&(e8.get() in s)):
            win_msg(e2)
            
        elif ((e3.get()==e6.get()==e9.get())&(e3.get() in s)&(e6.get() in s)&(e9.get() in s)):
            win_msg(e3)
            
        elif ((e1.get()==e5.get()==e9.get())&(e1.get() in s)&(e5.get() in s)&(e9.get() in s)):
            win_msg(e1)
            
        elif ((e3.get()==e5.get()==e7.get())&(e3.get() in s)&(e5.get() in s)&(e7.get() in s)):
            win_msg(e3)
        else:
            Label(win, text='No Winner!!!',font=('arial 18 bold'), justify='center').place(relx=0.33,rely=0.015,relwidth=0.35,relheight=0.15)

    
        
def start():
    e1.set('')
    e2.set('')
    e3.set('')
    e4.set('')
    e5.set('')
    e6.set('')
    e7.set('')
    e8.set('')
    e9.set('')
    Label(win, text='Go for Win!!! ',font=('arial 18 bold'), justify='center').place(relx=0.33,rely=0.015,relwidth=0.35,relheight=0.15)
    
btn_start=Button(win,text=' start ',font=('arial 18 bold'), justify='center' ,bg='green', fg='yellow', command=start).place(relx=0.03,rely=0.03,relheight=0.1)

btn_finish=Button(win,text='finish',font=('arial 18 bold'), justify='center' ,bg='orange', command=finish).place(relx=0.8,rely=0.03,relheight=0.1)

Label(win, text=' Press Start ',font=('arial 18 bold'), justify='center').place(relx=0.33,rely=0.015,relwidth=0.35,relheight=0.15)


    


