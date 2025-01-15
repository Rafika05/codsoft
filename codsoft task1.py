from tkinter import *
top = Tk()
top.title("To-Do List")
top.geometry("1350x720")
label = Label(top, text="To-Do List", fg="red", font=("Arial", 20, "bold"))
label.place(x=600, y=20)

tasks={}
y_position = 280

def add_list():
    global y_position
    text1 = t1.get().strip()
    if text1:
        if text1 not in tasks:  
            ch = Checkbutton(top, text=text1, fg="black",height=2,width=20)
            ch.place(x=580, y=y_position)
            y_position += 30
            tasks[text1]=ch
            lb.insert(END, text1)
            t1.delete(0, END)
            error_label.config(text="")  
        else:
            error_label.config(text="Task already exists!")
    else:
        error_label.config(text="Please enter a task....")

def delete():
    global y_position
    listindex = lb.curselection()
    if listindex:
        task = lb.get(listindex)
        lb.delete(listindex)
        tasks[task].destroy()
        del tasks[task]
        error_label.config(text="")
    else:
        error_label.config(text="Select a task to delete....")

t1 = Entry(top, bg="light blue", bd=20,width=40, fg="black")
t1.place(x=480, y=100)

btn = Button(top, text="ADD", bg="green", fg="white", width=6, height=2,font=("Arial",20,"bold"), command=add_list)
btn.place(x=910, y=100)

btn1 = Button(top, text="Remove Task", bg="red", fg="white",font=("Arial",20,"bold"), command=delete)
btn1.place(x=910, y=500)

lb = Listbox(top, height=15, width=30)
lb.place(x=910, y=250)

error_label = Label(top, text="", fg="red",font=("Comic Sans Mc",20,"bold"))
error_label.place(x=560, y=500)

top.mainloop()
