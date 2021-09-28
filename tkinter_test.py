import tkinter as tk

def test():
    print("cum")

def test2():
    print("penis")

LARGE_FONT= ("Verdana", 12)


class SYN(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="SYN", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Play Game",
                            command=lambda: [controller.show_frame(PageOne), test()])
        button.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="SYN", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Pass",
                            command=lambda: [controller.show_frame(PageOne),test()])
        button1.pack()

        button2 = tk.Button(self, text="Trade",
                            command=lambda: [controller.show_frame(PageOne),test2()])
        button2.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="SYN", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Pass",
                            command=lambda: [controller.show_frame(PageOne),test()])
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: [controller.show_frame(PageOne),test2()])
        button2.pack()

app = SYN()
app.mainloop()