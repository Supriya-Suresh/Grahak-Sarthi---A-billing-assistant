import tkinter as tk
from PIL import Image,ImageTk
from gtts import gTTS
import math
import graphics

class gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self,"Grahak Sarthi")
        tk.Tk.wm_attributes(self,"-fullscreen", True)
        tk.Tk.configure(self,background="red")
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
        tk.Frame.__init__(self, parent, bg="black")

        label1 = tk.Label(self, text="VESIT", font="Times 50 ", bg="black",fg="white")
        label1.place(x=-40, y=73, width=1420, height=50)

        label2 = tk.Label(self, text="Department of Electronics and Telecommunication", font="Times 40 ", bg="black", fg="white")
        label2.place(x=-18, y=160, width=1420, height=50)

        label3 = tk.Label(self, text="- A BILLING ASSISTANT", font="Times 26 bold italic", bg="black", fg="white")
        label3.place(x=-27, y=519, width=1420, height=50)

        #load = Image.open('veslogo.png')
        #render = ImageTk.PhotoImage(load)
        #img1 = tk.Label(image=render)
        #img1.image = render
        #img1.place(x=380, y=337)

        load = Image.open('veslogo.png')  # Image of Vivekanand College  Logo
        photo = ImageTk.PhotoImage(load)
        img4 = tk.Label(self,image=photo)
        img4.image = photo
        #img4.pack()
        img4.place(x=390, y=37)



        #self.image = tk.PhotoImage(file='veslogo.png')
        #self.gmail = tk.Label(self, image=self.image)
        #self.gmail.place(x=380, y=337)



        #load = Image.open('veslogo.png')
        #render = ImageTk.PhotoImage(load)
        #img50 = tk.Label(self, image=render, bg="black")
        #img50.image = render
        #img50.place(x=970, y=280)

        #self.photo62 = Image.open('veslogo.png')
        #self.photo63 = ImageTk.PhotoImage(self.photo62)
        #self.img64 = tk.Label(self, image=self.photo63)
        #self.img64.image = self.photo63
        #self.img64.place(x=380, y=37)



        button1 = tk.Button(self, text="Grahak Sarthi",fg="blue",font="Times 90",bg="yellow",activebackground="orange",
                            command=lambda: controller.show_frame(PageOne))
        button1.place(x=310, y=270)

        label4 = tk.Label(self, text="Mentor: Dr. R.K Kulkarni",font="Times 40 italic bold",bg="black",fg="yellow")
        label4.place(x=410, y=700)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="blue")
        label5 = tk.Label(self, text="Mentor: Dr. R.K Kulkarni, Electronics and Telecommunication", font="Times 30 italic bold", bg="blue", fg="white")
        label5.place(x=140, y=700)
        label6 = tk.Label(self, text="Billing Assistant", font="Times 30 bold", bg="White")
        label6.place(x=-35, y=90, width=1420, height=50)

        label7 = tk.Label(self, text="Welcome!", font="Times 30 bold ", bg="blue", fg="white")
        label7.place(x=-5, y=25, width=1370, height=50)

        #load = Image.open('veslogo.png')  # Image of Vivekanand College  Logo
        #render = ImageTk.PhotoImage(load)
        #img4 = tk.Label(self, image=render, bg="black")
        #img4.image = render
        #img4.place(x=390, y=37)

        button2 = tk.Button(self, text="New", bg="white", fg="black", activebackground="green",
                         activeforeground="Yellow", bd="10",
                         font="none 16 bold", height=0, width=10, padx="0", pady="0", wraplength=0,
                            command=lambda: controller.show_frame(FrontPage))
        button2.place(x=130, y=340)
        
        button3 = tk.Button(self, text="Back", bg="white", fg="black", activebackground="green",
                         activeforeground="white", bd="10",
                         font="none 16 bold", height=0, width=10, padx="0", pady="0", wraplength=0,
                            command=lambda: controller.show_frame(FrontPage))
        button3.place(x=1100, y=25)
        
app = gui()
app.mainloop()
