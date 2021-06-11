import json
import requests
import pyttsx3
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

from PIL import ImageTk, Image

root = Tk()
root.geometry("600x800")
root.configure(bg='#ABEBC6')
root.title("Stress Buster")
imgPath = "/home/manikandan/Documents/API_Pytest/stressBuster/speaker3.png"
image = Image.open(imgPath)
img = image.resize((40, 40), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
text=''
# jokeUrl = 'https://icanhazdadjoke.com/', https://official-joke-api.appspot.com/jokes/programming/random


def textToVoice(self):
    global text
    t2s = pyttsx3.init()
    t2s.setProperty('rate', 115)
    # voices = t2s.getProperty('voices')
    t2s.setProperty('voice', 'english+f6')
    try:
        t2s.say(text)
        t2s.runAndWait()
    except:
        t2s.say("Nothing here to Read.. Sorry!")
        t2s.runAndWait()
    t2s.stop()


def getQuote():
    url = "https://api.quotable.io/random"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response = json.loads(response.text)
    quote = response['content'] + " - " + response["author"]
    return quote


def speakerLogo():
    global img
    speakerLabel = Label(root, image=img, bg="#ABEBC6", fg="gray21")
    speakerLabel.bind('<Button-1>', textToVoice)
    speakerLabel.place(x=520, y=400)


def getJoke():
    url = "https://icanhazdadjoke.com/"
    headers = {'Accept': 'application/json'}
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response = json.loads(response.text)
    return response['joke']


def fetchQuote():
    global text
    text = getQuote()
    result = Label(root, text=text, bg="#ABEBC6", fg="gray21", font=("arial", 14, "bold"), wraplength=500)
    result.place(x=10, y=450, width=590, height=150)
    speakerLogo()


def fetchJoke():
    global text
    text = getJoke()
    result = Label(root, text=text, bg="#ABEBC6", fg="gray21", font=("arial", 14, "bold"), wraplength=500)
    result.place(x=10, y=450, width=590, height=150)
    speakerLogo()


def exit1():
    exit()


welcomeLabel = Label(root, text="welcome dear, How can I help you ?", bg="#ABEBC6", fg="gray21",
                     font=("arial", 16, "bold"))
welcomeLabel.place(x=100, y=20)

jokeButton = Button(root, text="Tell me a Joke", bg="#ABEBC6", fg="gray21", font=("arial", 16, "bold"), borderwidth='4', width=15, command = fetchJoke)
jokeButton.place(x=200, y=150)

QuoteButton = Button(root, text="Tell me a quote", bg="#ABEBC6", fg="gray21", font=("arial", 16, "bold"), borderwidth='4', width=15, command=fetchQuote)
QuoteButton.place(x=200, y=250)

# speakerLogo()

exitButton = Button(root, text="Exit", fg="white", bg="brown", width=10, command=exit1)
exitButton.place(x=200, y=750)

root.mainloop()
