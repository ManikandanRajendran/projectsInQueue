from tkinter import *

window = Tk()


def send():
    send = "YOU =>" + e.get()
    text.insert(END, "\n" + send)
    if e.get() == "Hello":
        text.insert(END, "\n" + "BOT => Hi")
    elif e.get() == "Hi":
        text.insert(END, "\n" + "BOT => Hi")
    elif e.get() == "How are you":
        text.insert(END, "\n" + "BOT => fine")

    e.delete(0, END)


window.title("CHAT BOT")
text = Text(window)
text.grid(row=0, column=0, columnspan=2)

e = Entry(window, width=100)
send = Button(window, text='send', command=send).grid(row=1, column=1)
e.grid(row=1, column=0)

window.mainloop()
