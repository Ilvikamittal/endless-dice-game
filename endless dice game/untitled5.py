from tkinter import*
from PIL import ImageTk,Image
root=Tk()

root.title("Endless dice game")
root.geometry("500x500")
root.configure(background="green")

img=ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

p1_label=Label(root,text="Player 1",bg="purple",fg="white")
p1_label.place(relx=0.2,rely=0.3,anchor=CENTER)

p2_label=Label(root,text="Player 2",bg="purple",fg="white")
p2_label.place(relx=0.8,rely=0.3,anchor=CENTER)

s1_label=Label(root,bg="orange")
s1_label.place(relx=0.2,rely=0.4,anchor=CENTER)

s2_label=Label(root,bg="orange")
s2_label.place(relx=0.8,rely=0.4,anchor=CENTER)

show_label=Label(root,bg="red")
show_label.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()

