import pytesseract as tess          # will convert the image to text string
from PIL import Image               # adds image processing capabilities
import pyttsx3                      # converts the text to speech

path = "/home/manikandan/Documents/API_Pytest/imageToText/4.png"
t2s = pyttsx3.init()
img = Image.open(path)
text = tess.image_to_string(img)
print(text)

t2s.setProperty('rate', 145)
t2s.setProperty('voice', 'english+f3')
t2s.say(text)
t2s.runAndWait()
