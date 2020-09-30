# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:07:34 2020

@author: datha
"""
from cv import cv2
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
from tkinter import messagebox

#---

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():

    root.label = Label(root,bg = "darkslategray", fg = "white",
                       text = "WEBCAM FEED", font = ('Comic Sans MS',20))
    root.label.pack(padx = 10, pady = 10)

    root.videoLabel = Label(root, bg = "darkslategray")
    root.videoLabel.pack(padx = 10, pady = 10)

    root.captureButton = Button(root, text = "CAPTURE", command = Capture,
                                bg = "LIGHTBLUE", font = ('Comic Sans MS', 10))
    root.captureButton.pack(padx = 10, pady = 10, fill = BOTH)

    # Creating object of class VideoCapture with webcam index
    root.cap = cv2.VideoCapture(0)

    width, height = 640, 480

    # Setting width and height
    root.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)

    root.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    # Calling ShowFeed() function
    ShowFeed()

#---

# Defining ShowFeed() function to display webcam feed
def ShowFeed():

    #Capturing frame by frame
    _, frame = root.cap.read()

    # Flipping the frame vertically
    frame = cv2.flip(frame, 1)

    # Displaying date and time on the feed
    cv2.putText(frame,datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                (20, 30), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

    # Changing the frame color from BGR to RGB
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    # Creating an image memory from the above frame exporting
    # array interface
    videoImg = Image.fromarray(cv2image)

    # Creating object of PhotoImage() class to display the frame
    imgtk = ImageTk.PhotoImage(image = videoImg)

    # Configuring the label to display the frame
    root.videoLabel.configure(image=imgtk)

    # Keeping a reference
    root.videoLabel.imgtk = imgtk

    # Calling the function after 10 milliseconds
    root.videoLabel.after(10, ShowFeed)

#---

# Capture() to capture and save the image
def Capture():

    # Storing the date in the mentioned format in the name variable
    name = datetime.now().strftime('%d-%m-%Y %H-%M-%S')

    # Storing the path to save the image
    # Define your own path
    path = "C:/Python/PyCAM/"

    # Creating an image with the name in the path with extension .jpg
    imgName = path + name + ".jpg"

    # Capturing the frame
    ret, frame = root.cap.read()

    # Displaying date and time on the frame
    cv2.putText(frame, datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                (430, 460), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

    # Writing the image with the captured frame. This function returns
    # a Boolean Value which is stored in success variable
    success = cv2.imwrite(imgName, frame)

    # Displaying messagebox
    if success :
        messagebox.showinfo("SUCCESS", "IMAGE CAPTURED")

#---

# Creating object of tk class
root = tk.Tk()

# Setting the title and background color
# disabling the resizing property
root.title("PyCAM")
root.configure(background = "darkslategray")
root.resizable(False,False)

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()