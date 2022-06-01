from tkinter import *
import pyttsx3
import datetime
import time
import webbrowser
import os
from tkinter import ttk
from playsound import playsound

rt=Tk()
j=pyttsx3.init()
rt.geometry('700x700')
 
o=j.getProperty('voices')
j.setProperty('voice',o[1].id)
h=int(time.strftime('%H'))
m=int(time.strftime('%M'))
if h>=5 and h<=12:
    j.say('good morning boss')
    j.runAndWait()
elif h>=12 and h<=17:
    j.say('good afternoon boss')
    j.runAndWait()
elif h>=17 and h<=20:
    j.say('good eveing boss')
    j.runAndWait()
elif h>=20 and h<=0:
    j.say('good night boss')
    j.runAndWait()    

rt.configure(background='blue')
rt.title('Jarvis')
l=Label(rt,text='Jarvis',font='Arial 18 bold')
l.place(x=0,y=0)
mc=Entry(rt,width=167,font='Arial 18 bold')
kl=['red','blue','green','yellow','brown','pink','orange','purple']
mc.place(x=0,y=100)
v=StringVar()
bc=ttk.Combobox(rt,width=21,value=kl)
bc.place(x=200,y=350)
bl=Label(rt,text='BackgroundColor',bg='purple',font='Arial 16 bold',fg='white')
bl.place(x=200,y=320)
bc.set('blue')
v=['Male','Female']
c=ttk.Combobox(rt,textvariable=v,value=v)
c.place(x=0,y=350)
c.set('Female')
lv=Label(rt,text='Voices',font='Arial 16 bold',fg='white',bg='black')
lv.place(x=0,y=320)
def vp():
    if c.get()=='Male':
        j.setProperty('voice',o[0].id)
    elif c.get()=='Female':
        j.setProperty('voice',o[1].id)
    j.setProperty('volumn',vs.get())

    if vs.get()>=50 and vs.get()<=100:
        vs.configure(troughcolor='yellow')
    if bc.get()=='red':
        rt.configure(background=kl[0])
        btn.configure(bg='yellow')
    elif bc.get()=='blue':
        rt.configure(bg=kl[1])
    elif bc.get()=='green':
        rt.configure(bg=kl[2])
    elif bc.get()=='yellow':
         rt.configure(bg=kl[3])
         vb.configure(bg='blue')
    elif bc.get()=='brown':
        rt.configure(bg=kl[4])
    elif bc.get()=='pink':
        rt.configure(bg=kl[5])
    elif bc.get()=='orange':
        rt.configure(bg=kl[6])
    elif bc.get()=='purple':
        rt.configure(bg=kl[7])
    
cn=IntVar()
vs=Scale(rt,length=320,troughcolor='red',variable=cn)
vs.place(x=580,y=356)
def cul():
    t=Toplevel()
    t.geometry('600x600')
    t.title('Calculator')  
    t.configure(bg='yellow')
    ol=Label(t,text='Calculator',bg='blue',fg='white',font='Arial 24 bold')
    ol.place(x=0,y=0)
    l=Label(t,text='Enter the first number',bg='white',fg='blue',font='Arial 16 bold')
    l.place(x=160,y=70)
    ni=IntVar()
    et=Entry(t,width=23,textvariable=ni)
    et.place(x=130,y=120)
    gyu=Label(t,text='Enter the second number',bg='blue',fg='white',font='Arial 16 bold')
    gyu.place(x=130,y=190)
    b=IntVar()
    rg=Entry(t,width=23,textvariable=b)
    rg.place(x=130,y=223)
    ool=Label(t,text='Enter the operator',bg='white',fg='blue',font='Arial 16 bold')
    ool.place(x=130,y=250)
    tool=Entry(t,width=23)
    tool.place(x=130,y=300)
    root=Label(t,text='Result',bg='blue',fg='white',font='Arial 16 bold')
    root.place(x=120,y=420)
    def opi():
        if tool.get()=='+':
            root.configure(text=f'{et.get()} + {rg.get()} = {ni.get()+b.get()}')
        elif tool.get()=='-':
            root.configure(text=f'{et.get()} - {rg.get()} = {ni.get()-b.get()}')
        elif tool.get()=='*' or tool.get()=='x':
            root.configure(text=f'{et.get()} X {rg.get()} = {ni.get()*b.get()}')
        elif tool.get()=='/':
            root.configure(text=f'{et.get()} / {rg.get()} = {ni.get()/b.get()}')


    bu=Button(t,text='Calculate',bg='purple',fg='white',width=20,command=opi)
    bu.place(x=100,y=350)


    t.mainloop()
def july():
    
    if mc.get()=='google':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://google.com')
    elif mc.get()=='my song':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://www.youtube.com/watch?v=sAzlWScHTc4')
    elif mc.get()=='github':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://www.github.com')
    elif mc.get()=='gmail':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
    elif mc.get()=='youtube':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://www.youtube.com')
    elif mc.get()=='twitter':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://www.twitter.com')
    elif mc.get()=='':
        j.say('please enter something')
        j.runAndWait()
    elif mc.get()=='song':
        os.startfile('C:\\Users\\adity\\Desktop\\turtle\\j.mp3')
    elif mc.get()=='day':
        j.say('today is'+ time.strftime('%A'))
        j.runAndWait()
    elif mc.get()=='month':
        j.say('month is'+time.strftime('%B'))
        j.runAndWait()
    elif mc.get()=='microsoft word':
        j.say('here found boss')
        j.runAndWait()
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
    elif mc.get()=='microsoft powerpoint':
        j.say('here found boss')
        j.runAndWait()
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
    elif mc.get()=='microsoft excel':
        j.say('here found boss')
        j.runAndWait()
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
    elif mc.get()=='hotstar':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://www.hotstar.com')
    elif mc.get()=='netflix':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://www.netflix.com')
    elif mc.get()=='prime video':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://www.primevideo.com')
    elif mc.get()=='freelancer':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://www.freelancer.com')
    elif mc.get()=='udemy':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://www.udemy.com')
    elif mc.get()=='great learning':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://www.greatlearning.com')
    elif mc.get()=='geeksforgeeks':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://www.geeksforgeeks.com')
    elif mc.get()=='time':
        j.say('time is'+time.strftime('%H:%M'))
        j.runAndWait()
    elif mc.get()=='python idle':
        j.say('here found boss')
        j.runAndWait()
        os.startfile("C:\\Users\\adity\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\idlelib\\idle.pyw")
    

    else:
        j.say('sorry i cannot get it boss')
        j.runAndWait()
btn=Button(rt,text='Speak',bg='red',fg='white',width=21,font='Arial 20 bold',command=july)
btn.place(x=111,y=200)
vb=Button(rt,text='Select',width=21,bg='yellow',fg='purple',command=vp)
vb.place(x=0,y=420)
sn=Button(rt,text='Calculator',bg='pink',fg='blue',width=18,command=cul)
sn.place(x=160,y=420)
rt.mainloop()
