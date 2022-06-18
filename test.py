from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()  
canvas = Canvas(root, width = 300, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("/home/aswin/Downloads/ANPR/positive/Honda-Civic-527740d.jpg_0352_0097_0183_0109_0049.png"))  
canvas.create_image(150, 200, anchor=NW, image=img) 
root.mainloop() 

