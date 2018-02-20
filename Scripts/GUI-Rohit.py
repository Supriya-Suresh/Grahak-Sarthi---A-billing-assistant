import tkinter as tk
from PIL import Image, ImageTk
#from gtts import gTTS
import math
import graphics


class gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Grahak Sarthi")
        tk.Tk.wm_attributes(self, "-fullscreen", True)
        tk.Tk.configure(self, background="red")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frame = {}
        for F in (FrontPage, PageOne):
            frame = F(container, self)
            self.frame[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(FrontPage)

    def show_frame(self, controller):
        frame = self.frame[controller]
        frame.tkraise()


# Screen Configuration Ends
class FrontPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="navy")

        label1 = tk.Label(self, text="VESIT", font="Times 50 underline", bg="navy", fg="white")
        label1.place(x=-40, y=73, width=1420, height=50)

        label2 = tk.Label(self, text="Department of Electronics and Telecommunication", font="Times 40 ", bg="navy",
                          fg="white")
        label2.place(x=-18, y=160, width=1420, height=50)

        label3 = tk.Label(self, text="Grahak Sarthi-A Billing assistant", font="Times 44 bold underline", bg="navy", fg="gold")
        label3.place(x=0, y=370, width=1420, height=50)

        label8 = tk.Label(self, text="Welcome to!", font="Times 26 bold italic", bg="navy", fg="white")
        label8.place(x=-10, y=270, width=1420, height=50)



        # load = Image.open('veslogo.png')
        # render = ImageTk.PhotoImage(load)
        # img50 = tk.Label(self, image=render, bg="black")
        # img50.image = render
        # img50.place(x=970, y=280)

        #self.photo62 = Image.open('ves-logo.png')
        #self.photo63 = ImageTk.PhotoImage(self.photo62)
        #self.img64 = tk.Label(self, image=self.photo63)
        #self.img64.image = self.photo63
        #self.img64.place(x=380, y=37)

        button1 = tk.Button(self, text="Proceed to bill", fg="navy", font="Times 40", bg="gold",
                            activebackground="dark goldenrod",
                            command=lambda: controller.show_frame(PageOne))
        button1.place(x=520, y=500)

        label4 = tk.Label(self, text="Mentored by : Dr. R.K Kulkarni", font="Times 26 italic bold", bg="navy", fg="gold")
        label4.place(x=470, y=700)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="navy")
        label5 = tk.Label(self, text="Developed by: Supriya Suresh . Pragati Tripathi . Rohit Sreedhar",
                          font="Times 20 italic bold", bg="navy", fg="white")
        label5.place(x=220, y=700)
        label6 = tk.Label(self, text="Billing desk", font="Times 30 bold", bg="gold")
        label6.place(x=-35, y=90, width=1420, height=50)

        label7 = tk.Label(self, text="Grahak Sarthi-A billing Assistant", font="Times 30 bold ", bg="navy", fg="gold")
        label7.place(x=-5, y=25, width=1370, height=50)

        label11 = tk.Label(self, text="Hello user!", font="Times 30 italic ", bg="navy", fg="white")
        label11.place(x=-320, y=240, width=1370, height=50)

        button2 = tk.Button(self, text="Click to begin", bg="white", fg="black", activebackground="green",
                            activeforeground="Yellow", bd="10",
                            font="none 20 bold", height=0, width=30, padx="0", pady="0", wraplength=0,
                            command=lambda: controller.show_frame(FrontPage))
        button2.place(x=130, y=340)

        button3 = tk.Button(self, text="Home", bg="white", fg="black", activebackground="green",
                            activeforeground="white", bd="10",
                            font="none 16 bold", height=0, width=10, padx="0", pady="0", wraplength=0,
                            command=lambda: controller.show_frame(FrontPage))
        button3.place(x=1100, y=25)

        button4 = tk.Button(self, text="Reset", bg="white", fg="black", activebackground="green",
                            activeforeground="Yellow", bd="10",
                            font="none 16 bold", height=0, width=10, padx="0", pady="0", wraplength=0,
                            command=lambda: controller.show_frame(FrontPage))
        button4.place(x=1000, y=340)

        button5 = tk.Button(self, text="Update", bg="white", fg="black", activebackground="green",
                            activeforeground="Yellow", bd="10",
                            font="none 16 bold", height=0, width=10, padx="0", pady="0", wraplength=0,
                            command=lambda: controller.show_frame(FrontPage))
        button5.place(x=1000, y=440)

app = gui()
app.mainloop()
