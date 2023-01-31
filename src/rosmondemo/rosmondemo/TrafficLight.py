#! /usr/bin/env python3

#from https://stackoverflow.com/questions/24588406/creating-a-traffic-light-using-python

from tkinter import *

class TrafficLights:

    def __init__(self,name):

        window = Tk()
        window.title("Monitor "+name)

        frame = Frame(window)
        frame.pack()

        self.canvas = Canvas(window, width=120, height=340, bg="white")
        self.canvas.pack()

        self.oval_red = self.canvas.create_oval(10, 10, 110, 110, fill="white")
        self.oval_yellow = self.canvas.create_oval(10, 120, 110, 220, fill="white")
        self.oval_green = self.canvas.create_oval(10, 230, 110, 330, fill="white")

        # self.color.set('R')
        self.canvas.itemconfig(self.oval_red, fill="red")

        window.mainloop()

    def monitorCallback(self,data):
        colors = {"true":'G',"unknown":'Y',"false":'R'}
        truestr = "true"
        falsestr = "false"
        unknownstr = "unknown"
        if truestr in data.data:
            self.changeColor(colors[truestr])
        elif falsestr in data.data:
            self.changeColor(colors[falsestr])
        elif unknownstr in data.data:
            self.changeColor(colors[unknownstr])


    def changeColor(self,color):
        # color = 'R'#self.color.get()

        if color == 'R':
            self.canvas.itemconfig(self.oval_red, fill="red")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="white")
        elif color == 'Y':
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="yellow")
            self.canvas.itemconfig(self.oval_green, fill="white")
        elif color == 'G':
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="green")
