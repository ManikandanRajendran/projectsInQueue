from tkinter import *

root = Tk()

class definePage(root):
    def __init__(self, *args, **kwargs):
        root.__init__(self, *args, **kwargs)
        container = root.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (fisrtPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(fisrtPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.rootraise()


class fisrtPage(root.Frame):
    def __init__(self, parent, controller):
        root.Frame.__init__(self, parent)
        label = root.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = root.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = root.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(root.Frame):

    def __init__(self, parent, controller):
        root.Frame.__init__(self, parent)
        label = root.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = root.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = root.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(root.Frame):

    def __init__(self, parent, controller):
        root.Frame.__init__(self, parent)
        label = root.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = root.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = root.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = definePage()
app.mainloop()