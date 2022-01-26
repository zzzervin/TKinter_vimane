from tkinter import *
k=0
def klikker(event):
    global k
    k+=1
    nupp.config(text=k)

def klikker_(event):
    global k
    k-=1
    nupp.config(text=k)

def txt_to_lbl(event):
    t=txt.get()
    lbl.configure(text=t)
    txt.delete(0,END)

def valimine():
    valik=var.get()
    lbl.configure(text=valik)
    txt.insert(0,valik)

akkan=Tk()# главное окно приложения
akkan.title("Akkan")
akkan.geometry("800x400") 

nupp=Button(akkan,text="Mina olen nupp",font="Arial 20",width=20,bg="#FF6347",fg="#000080",relief=RAISED)
nupp.pack()#place(x=400,y=200)#side=LEFT
nupp.bind("<Button-1>",klikker)
nupp.bind("<Button-3>",klikker_)

lbl=Label(akkan,text="...",height=3,width=20,font="Arial 20",bg="green",fg="lightblue",relief="solid")#.pack()
lbl.pack()
txt=Entry(akkan,width=20,font="Arial 20",bg="green",fg="lightblue",justify=CENTER)
txt.pack()
txt.bind("<Return>",txt_to_lbl)
akkan.mainloop()

i1=PhotoImage(file="1.jpg")
i2=PhotoImage(file="2.png")
i3=PhotoImage(file="3.png")

var=StringVar()
var.set("1")
r1=Radiobutton(akkan,image=i1,variable=var,value="1",command=valimine)
r2=Radiobutton(akkan,image=i2,variable=var,value="2",command=valimine)
r3=Radiobutton(akkan,image=i3,variable=var,value="3",command=valimine)

r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)