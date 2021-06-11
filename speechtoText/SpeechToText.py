import speech_recognition as sr

#
# filename = '/home/manikandan/Downloads/download.mp4'
#
r = sr.Recognizer()
# with sr.AudioFile(filename) as source:
#     audio_data= r.record(source)
#     text = r.recognize_google(audio_data)
#     print(text)

# from tkinter import *
# import tkSnack
#
# root = Tk()
# tkSnack.initializeSnack(root)
# c = tkSnack.Sound(file='test.wav')
# c.record()
# root.after(5000, c.stop)
# root.mainloop()


with sr.Microphone(device_index=1) as source:
    print("Speak:")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry, speak again")
