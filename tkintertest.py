from tkinter import Tk, Frame, BOTH, Button,messagebox


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent

        self.parent.title("Test title")
        self.fullscreen()



    def fullscreen(self):
        w, h = self.parent.winfo_screenwidth(), self.parent.winfo_screenheight()
        self.parent.geometry("%dx%d+0+0" % (w , h))


def showMsg():
    messagebox.showinfo("Hello", "Hello world")

def main():
    root = Tk()
    app = Example(root)

    b = Button(root, text="OK", command=showMsg)

    b.pack()
    root.mainloop()


if __name__ == '__main__':
    main()