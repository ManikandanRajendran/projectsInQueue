import json
from tkinter import *

root = Tk()
root.geometry("800x800")
root.title("Quize")

with open('data.json') as file:
    input = json.load(file)


class Quiz:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)

    def question(self,qn):
        qstn_lbl = Label(root, text=(input['data'][qn]['q']), font=("times", 20, "bold"))
        qstn_lbl.place(x=70, y=100)
        return qn

    def read_question(self, i):
        with open('data.json') as file:
            input = json.load(file)
            q = (input['data'][i]['q'])
            o = (input['data'][0]['o'])
            a = (input['data'][0]['a'])
            print(q)
            print(o)
            print(a)

    def read_options(self):
        pass

    def read_ans(self):
        pass

    def exit1(self):
        exit()


quiz = Quiz()
heading = Label(root, text="Quiz in python program", bg='blue', width=65, font=("times", 20, "bold"))
heading.place(x=0, y=0)

submit = Button(root, text="Submit", bg="green", width=15)
submit.place(x=220, y=600)

next1 = Button(root, text="Next Question", bg="green", width=15)
next1.place(x=450, y=600)

close = Button(root, text="close", bg="green", width=15, command=quiz.exit1)
close.place(x=330, y=700)


root.mainloop()
