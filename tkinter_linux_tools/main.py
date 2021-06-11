import tkinter as tk
import os


root = tk.Tk()
root.title('small tool')
root.geometry("300x200")

def power_off():
    os.system("shutdown now -h")


def restart():
    os.system('reboot now')

root.mainloop()