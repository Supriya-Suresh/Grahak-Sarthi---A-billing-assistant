
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tkinter as tk
from gtts import gTTS
from pygame import mixer

import argparse
import sys
import time
import cv2
import os

import numpy as np
import tensorflow as tf
from PIL import Image, ImageTk
import math
import graphics

list_price = []
list_name = []
list_weight = []
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
        for F in (FrontPage, PageOne, PageTwo):
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

        label1 = tk.Label(self, text="VESIT ", font="Times 50 underline", bg="navy", fg="white")
        label1.place(x=-40, y=73, width=1420, height=50)

        label2 = tk.Label(self, text="Department of Electronics and Telecommunication", font="Times 40 ", bg="navy",
                          fg="white")
        label2.place(x=-18, y=160, width=1420, height=90)

        label3 = tk.Label(self, text="Grahak Sarthi-A Billing assistant", font="Times 44 bold", bg="navy", fg="gold")
        label3.place(x=0, y=370, width=1420, height=50)

        label4 = tk.Label(self, text="Welcome to!", font="Times 26 bold italic", bg="navy", fg="white")
        label4.place(x=-10, y=270, width=1420, height=50)



        #load = Image.open('veslogo.png')
        #render = ImageTk.PhotoImage(load)
        #img1 = tk.Label(self, image=render, bg="black")
        #img1.image = render
        #img1.place(x=970, y=280)

        #self.photo62 = Image.open('veslogo.png')
        #self.photo63 = ImageTk.PhotoImage(self.photo62)
        #self.img64 = tk.Label(self, image=self.photo63)
        #self.img64.image = self.photo63
        #self.img64.place(x=380, y=37)

        button1 = tk.Button(self, text="Proceed to bill", fg="navy", font="Times 40", bg="gold",
                            activebackground="dark goldenrod",
                            command=lambda: controller.show_frame(PageOne))
        button1.place(x=520, y=500)

        label5 = tk.Label(self, text="Mentored by : Dr. R.K Kulkarni", font="Times 26 italic bold", bg="navy", fg="gold")
        label5.place(x=470, y=700)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="navy")

        label6 = tk.Label(self, text="Developed by: Pragati Tripathi . Rohit Sreedhar . Supriya Suresh",
                          font="Times 20 italic bold", bg="navy", fg="white")
        label6.place(x=280, y=700)
        label7 = tk.Label(self, text="Billing desk", font="Times 30 bold", bg="gold")
        label7.place(x=-35, y=90, width=1420, height=50)

        label8 = tk.Label(self, text="Grahak Sarthi-A billing Assistant", font="Times 30 bold ", bg="navy", fg="gold")
        label8.place(x=-5, y=25, width=1370, height=50)

        label9 = tk.Label(self, text="Hello user!", font="Times 30 italic ", bg="navy", fg="white")
        label9.place(x=-390, y=240, width=1370, height=50)

        def mainprogram():
            ##Main program
            import argparse
            import sys
            import time
            import cv2
            # from camera import camera_image
            import weighing
            #ext_weight = weighing.weighing_machine_output()
            #list_weight.append(ext_weight)
            import camera

            import numpy as np
            import tensorflow as tf

            # from Veg_billing import veg_amount
            im = camera.camera_image()

            def load_graph(model_file):
                graph = tf.Graph()
                graph_def = tf.GraphDef()

                with open(model_file, "rb") as f:
                    graph_def.ParseFromString(f.read())
                with graph.as_default():
                    tf.import_graph_def(graph_def)

                return graph

            def read_tensor_from_image_file(file_name, input_height=299, input_width=299,
                                            input_mean=0, input_std=255):
                input_name = "file_reader"
                output_name = "normalized"
                file_reader = tf.read_file(file_name, input_name)
                image_reader = tf.image.decode_jpeg(file_reader, channels=3,
                                                    name='jpeg_reader')
                float_caster = tf.cast(image_reader, tf.float32)
                dims_expander = tf.expand_dims(float_caster, 0);
                resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
                normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
                sess = tf.Session()
                result = sess.run(normalized)

                return result

            def load_labels(label_file):
                label = []
                proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
                for l in proto_as_ascii_lines:
                    label.append(l.rstrip())
                return label

            if __name__ == "__main__":
                # file_name = "tf_files/bit.jpg"
                # file_name = r"C:\Users\sathish\Desktop\Camera/Veg.jpg"
                file_name = r"C:\Users\sathish\Desktop\Veggie\tensorflow-for-poets-2\Images/Veg.jpg"
                model_file = r"C:\Users\sathish\Desktop\Veggie\tensorflow-for-poets-2\tf_files/rounded_graph.pb"
                label_file = r"C:\Users\sathish\Desktop\Veggie\tensorflow-for-poets-2\tf_files/retrained_labels.txt"
                input_height = 299
                input_width = 299
                input_mean = 128
                input_std = 128
                input_layer = "Mul"
                output_layer = "final_result"

                parser = argparse.ArgumentParser()
                parser.add_argument("--image", help="image to be processed")
                parser.add_argument("--graph", help="graph/model to be executed")
                parser.add_argument("--labels", help="name of file containing labels")
                parser.add_argument("--input_height", type=int, help="input height")
                parser.add_argument("--input_width", type=int, help="input width")
                parser.add_argument("--input_mean", type=int, help="input mean")
                parser.add_argument("--input_std", type=int, help="input std")
                parser.add_argument("--input_layer", help="name of input layer")
                parser.add_argument("--output_layer", help="name of output layer")
                args = parser.parse_args()

                if args.graph:
                    model_file = args.graph
                if args.image:
                    file_name = args.image
                if args.labels:
                    label_file = args.labels
                if args.input_height:
                    input_height = args.input_height
                if args.input_width:
                    input_width = args.input_width
                if args.input_mean:
                    input_mean = args.input_mean
                if args.input_std:
                    input_std = args.input_std
                if args.input_layer:
                    input_layer = args.input_layer
                if args.output_layer:
                    output_layer = args.output_layer

                graph = load_graph(model_file)
                t = read_tensor_from_image_file(file_name,
                                                input_height=input_height,
                                                input_width=input_width,
                                                input_mean=input_mean,
                                                input_std=input_std)

                input_name = "import/" + input_layer
                output_name = "import/" + output_layer
                input_operation = graph.get_operation_by_name(input_name);
                output_operation = graph.get_operation_by_name(output_name);

                with tf.Session(graph=graph) as sess:
                    start = time.time()
                    results = sess.run(output_operation.outputs[0],
                                       {input_operation.outputs[0]: t})
                    end = time.time()
                results = np.squeeze(results)

                top_k = results.argsort()[-5:][::-1]
                labels = load_labels(label_file)

                print('\nEvaluation time (1-image): {:.3f}s\n'.format(end - start))
                top_var = (top_k[0])
                # final_name = top_var[-5:]

                result_final = results[top_var] * 100
                final_name = labels[top_var]
                list_name.append(final_name)
                print(labels[top_var], "Confidence: %s %%\n" % result_final)
                # return result_final,labels,top_var,final_name

                if result_final > 20:
                    # print(labels[top_var], "Confidence: %s %%\n" %result_final)
                    final_name = labels[top_var]
                    print("Predicted Vegetable: %s" % final_name)
                    ext_weight = 0.5
                    list_weight.append(ext_weight)

                    try:
                        self.canvas1.destroy()
                    except (NameError, AttributeError):
                        pass
                    try:
                        self.label10.destroy()
                    except (NameError, AttributeError):
                        pass
                    try:
                        self.label11.destroy()
                    except (NameError, AttributeError):
                        pass
                    try:
                        self.label12.destroy()
                    except (NameError, AttributeError):
                        pass
                    try:
                        self.label13.destroy()
                    except (NameError, AttributeError):
                        pass
                    try:
                        self.label14.destroy()
                    except (NameError, AttributeError):
                        pass
                    try:
                        self.label15.destroy()
                    except (NameError, AttributeError):
                        pass
                    try:
                        self.label16.destroy()
                    except (NameError, AttributeError):
                        pass
                    try:
                        self.label17.destroy()
                    except (NameError, AttributeError):
                        pass
                    try:
                        self.button5.destroy()
                    except (NameError, AttributeError):
                        pass

                    #    ######Calculation
                    if final_name == "tomato":
                        price = int((float(ext_weight) * 40) / 1)  # Considering cost of Tomato 1Kg = Rs.40
                        list_price.append(price)
                        tot_bill = int(sum(list_price))
                        # print("cost: Rs %s \n" % price)
                        print("Total cost: Rs %s \n" % price)
                        # return final_name, result_final, ext_weight, price
                    elif final_name == "ladyfinger":
                        price = int((float(ext_weight) * 45) / 1)  # Considering cost of Okra 1Kg = Rs.45
                        list_price.append(price)
                        tot_bill = int(sum(list_price))
                        print("Total cost: Rs %s \n" % price)
                        # return final_name, result_final, ext_weight, price
                    elif final_name == "cucumber":
                        price = int((float(ext_weight) * 30) / 1)  # Considering cost of Cucumber 1Kg = Rs.30
                        list_price.append(price)
                        tot_bill = int(sum(list_price))
                        print("Total cost: Rs %s \n" % price)
                        # return final_name, result_final, ext_weight, price
                    elif final_name == "bitter gourd":
                        price = int((float(ext_weight) * 55) / 1)  # Considering cost of bitter gourd 1Kg = Rs.55
                        list_price.append(price)
                        tot_bill = int(sum(list_price))
                        print("Total cost: Rs %s \n" % price)
                        # return final_name, result_final, ext_weight, price

                    self.canvas1 = tk.Canvas(self, width=650, height=350, bg="silver",
                                             scrollregion=(0, 0, 500, 500))
                    self.canvas1.place(x=570, y=220)

                    self.label10 = tk.Label(self,
                                            text=" Items                 Quantity           Amount ",
                                            fg="red", bg="silver", font="Times 24 bold")
                    self.label10.place(x=610, y=250)

                    self.label11 = tk.Label(self, text=final_name, bg="silver", fg="black", font="Times 22")
                    self.label11.place(x=610, y=290, height=80)

                    self.label12 = tk.Label(self, text="%s Kg\n" % ext_weight, bg="silver", fg="black",
                                            font="Times 22")
                    self.label12.place(x=850, y=306, height=80)

                    self.label13 = tk.Label(self, text="Rs.%s" % price, bg="silver", fg="black", font="Times 22")
                    self.label13.place(x=1055, y=290, height=80)

                    self.label17 = tk.Label(self, text="Cost of %s : Rs %s \n" % (final_name, price), bg="silver",
                                            fg="black", font="Times 24")
                    self.label17.place(x=610, y=400)

                    self.label14 = tk.Label(self, text="                Total cost: Rs %s \n" % tot_bill, bg="silver", fg="blue",
                                            font="Times 26 bold")
                    self.label14.place(x=610, y=450)

                    button5 = tk.Button(self, text="Proceed to bill ➪", bg="white", fg="black", activebackground="green",
                                        activeforeground="Yellow", bd="10",
                                        font="Times 20 bold", padx="0", pady="0", wraplength=0,
                                        command = lambda: controller.show_frame(PageTwo))
                    button5.place(x=790, y=600)

                    # tts = gTTS(text="Total cost: Rs %s" % price, lang="en")  # Text to Speech
                    # thanks = gTTS(text="Thank you for shopping with us", lang="en")
                    # tts.save(r"C:\Users\sathish\Desktop\Veggie\tensorflow-for-poets-2\sound\sound.mp3")
                    # thanks.save(r"C:\Users\sathish\Desktop\Veggie\tensorflow-for-poets-2\sound\thankyou.mp3")
                    # mixer.init()
                    # mixer.music.load(r"C:\Users\sathish\Desktop\Veggie\tensorflow-for-poets-2\sound\sound.mp3")
                    # mixer.music.load((r"C:\Users\sathish\Desktop\Veggie\tensorflow-for-poets-2\sound\thankyou.mp3"))
                    # mixer.music.play()



                else:
                    print("Object not identified")
                    self.label16 = tk.Label(self, text="Object not identified", bg="silver", fg="red",
                                            font="Times 33")
                    self.label16.place(x=640, y=380, height=80)

        button2 = tk.Button(self, text="Click to begin", bg="white", fg="black", activebackground="green",
                            activeforeground="Yellow", bd="10",
                            font="Times 26 bold", height=0, width=18, padx="0", pady="0", wraplength=0,
                            command=mainprogram)
        button2.place(x=90, y=340)

        button3 = tk.Button(self, text="Home", bg="white", fg="black", activebackground="green",
                            activeforeground="white", bd="10",
                            font="Times 16 bold", height=0, width=10, padx="0", pady="0", wraplength=0,
                            command=lambda: controller.show_frame(FrontPage))
        button3.place(x=1100, y=25)

        def spec():
            list_price[:] = []
            list_name[:] = []
            list_weight[:] = []
            try:
                self.canvas1.destroy()
            except (NameError, AttributeError):
                pass
            try:
                self.canvas2.destroy()
            except (NameError, AttributeError):
                pass
            try:
                self.label10.destroy()
            except (NameError, AttributeError):
                pass
            try:
                self.label11.destroy()
            except (NameError, AttributeError):
                pass
            try:
                self.label12.destroy()
            except (NameError, AttributeError):
                pass
            try:
                self.label13.destroy()
            except (NameError, AttributeError):
                pass
            try:
                self.label14.destroy()
            except (NameError, AttributeError):
                pass
            try:
                self.label15.destroy()
            except (NameError, AttributeError):
                pass
            try:
                self.label16.destroy()
            except (NameError, AttributeError):
                pass
            try:
                self.label17.destroy()
            except (NameError, AttributeError):
                pass
            try:
                self.button5.destroy()
            except (NameError, AttributeError):
                pass
            controller.show_frame(PageOne)
            #if os.path.exists(r'C:\Users\sathish\Desktop\Veggie\tensorflow-for-poets-2\Images\Veg.jpg'):
            #    os.remove(r'C:\Users\sathish\Desktop\Veggie\tensorflow-for-poets-2\Images\Veg.jpg')


        button4 = tk.Button(self, text="Reset", bg="white", fg="black", activebackground="green",
                            activeforeground="Yellow", bd="10",
                            font="Times 16 bold", height=0, width=5, padx="0", pady="0", wraplength=0,
                            command=spec)
        button4.place(x=10, y=25)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="navy")

        label23 = tk.Label(self, text="Developed by: Pragati Tripathi . Rohit Sreedhar . Supriya Suresh",
                          font="Times 20 italic bold", bg="navy", fg="white")
        label23.place(x=280, y=700)

        button3 = tk.Button(self, text="Back", bg="white", fg="black", activebackground="green",
                            activeforeground="white", bd="10",
                            font="Times 16 bold", height=0, width=10, padx="0", pady="0", wraplength=0,
                            command=lambda: controller.show_frame(PageOne))
        button3.place(x=1100, y=25)

        def payments():
            self.button8 = tk.Button(self, text="PayTM", bg="white", fg="black", activebackground="green",
                                activeforeground="Yellow", bd="10",
                                font="Times 20 bold", height=0, width=15, padx="0", pady="0", wraplength=0)
            self.button8.place(x=130, y=320)
            self.button9 = tk.Button(self, text="Mobikwik", bg="white", fg="black", activebackground="green",
                                activeforeground="Yellow", bd="10",
                                font="Times 20 bold", height=0, width=15, padx="0", pady="0", wraplength=0)
            self.button9.place(x=130, y=410)
            self.button10 = tk.Button(self, text="PayUMoney", bg="white", fg="black", activebackground="green",
                                activeforeground="Yellow", bd="10",
                                font="Times 20 bold", height=0, width=15, padx="0", pady="0", wraplength=0)
            self.button10.place(x=130, y=500)

            self.button11 = tk.Button(self, text="State Bank Buddy", bg="white", fg="black", activebackground="green",
                                activeforeground="Yellow", bd="10",
                                font="Times 20 bold", height=0, width=15, padx="0", pady="0", wraplength=0)
            self.button11.place(x=130, y=590)

            try:
                self.label15.destroy()
            except (NameError, AttributeError):
                pass


        button6 = tk.Button(self, text="e-Payment", bg="dark orange", fg="white", activebackground="green",
                            activeforeground="Yellow", bd="10",
                            font="Times 30 bold", height=0, width=15, padx="0", pady="0", wraplength=0,
                            command=payments)
        button6.place(x=130, y=190)

        def thanks():
            self.label15 = tk.Label(self, text="Thank you for shopping with us :)", fg="yellow",bg = "navy",
                                    font="Times 48 italic ")
            self.label15.place(x=310, y=500)

            try:
                self.button8.destroy()
            except (NameError, AttributeError):
                pass
            try:
                self.button9.destroy()
            except (NameError, AttributeError):
                pass
            try:
                self.button10.destroy()
            except (NameError, AttributeError):
                pass
            try:
                self.button11.destroy()
            except (NameError, AttributeError):
                pass

        button7 = tk.Button(self, text="Cash-Payment", bg="dark orange", fg="white", activebackground="green",
                            activeforeground="white", bd="10",
                            font="Times 30 bold", height=0, width=15, padx="0", pady="0", wraplength=0, command = thanks)
        button7.place(x= 770, y=190)




app = gui()
app.mainloop()
