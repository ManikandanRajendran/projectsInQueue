import pyttsx3

t2s = pyttsx3.init()

voiceRate = t2s.getProperty('rate')
print(voiceRate)
t2s.setProperty('rate', 145)

voices = t2s.getProperty('voices')
# print(voices)
print(len(voices))

t2s.setProperty('voice', 'english+f5')

t2s.say("podu thagida thagida")
t2s.runAndWait()
t2s.stop()

# try:
#     # t2s.save_to_file('')
#     t2s.save_to_file('podu thagida thagida podu thagida thagida podu thagida thagida podu thagida thagida', '/home/manikandan/Desktop/audio/test.mp3')
#     t2s.runAndWait()
# except:
#     print("audio not saved")