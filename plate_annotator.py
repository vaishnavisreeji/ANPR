import shutil
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk


folder_selected =''
value =''

def submit():
    global value
    name=name_var.get()
    os.rename(os.path.join(folder_selected, value), os.path.join(folder_selected, name))
    show_file_list(window)
    print("The name is : " + name)

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    global value
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))
    #img = PhotoImage(file=os.path.join(folder_selected, value))  
    #img = Image.open(os.path.join(folder_selected, value))
    print(folder_selected+'/' +value)
    name_var.set(value)
    img = ImageTk.PhotoImage(Image.open(folder_selected+'/' +value))
    window.img = img
    canvas.create_image(10, 20, anchor=NW, image=window.img) 

def show_image():
    #img = ImageTk.PhotoImage(Image.open(os.path.join(folder_selected, os.listdir(folder_selected)[0])))
    img = ImageTk.PhotoImage(Image.open("/home/aswin/Downloads/ANPR/positive/Honda-Civic-527740d.jpg_0352_0097_0183_0109_0049.png"))
    window.img = img
    canvas.create_image(0,0, anchor=NW, image=window.img) 
    canvas.pack()

def show_folder_select_dialog():
    global folder_selected
    window.withdraw()
    folder_selected = filedialog.askdirectory()
    window.deiconify()

    show_file_list(window)


def show_file_list(window):
    listbox.delete(0, END)
    listbox.pack(side = LEFT, fill = BOTH)
    
    # Creating a Scrollbar and 
    # attaching it to root window
    
    
    # Adding Scrollbar to the right
    # side of root window
    scrollbar.pack(side = RIGHT, fill = BOTH)
    
    # Insert elements into the listbox
    print(folder_selected)
    if folder_selected != '':
        files = os.listdir(folder_selected)
        files.sort()
        for file in files:
            print(file)
            if os.path.isfile(os.path.join(folder_selected,file)):
                print(file)
                listbox.insert(END, file)
        
    # Attaching Listbox to Scrollbar
    # Since we need to have a vertical 
    # scroll we use yscrollcommand
    listbox.config(yscrollcommand = scrollbar.set)
    
    # setting scrollbar command parameter 
    # to listbox.yview method its yview because
    # we need to have a vertical view
    scrollbar.config(command = listbox.yview)

window = Tk()
window.geometry("750x400")
name_var=StringVar()

greeting = Label(text="Plate Annotator")
greeting.pack()
button = Button(
    text="Select Folder",
    width=10,
    height=1,
    bg="blue",
    fg="yellow",
    command= show_folder_select_dialog
)

button.pack()
listbox = Listbox(window)
listbox.bind('<<ListboxSelect>>', onselect)
scrollbar = Scrollbar(window)

canvas = Canvas(window,width = 300, height = 100)      
canvas.pack() 
name_entry = Entry(window,textvariable = name_var, font=('calibre',10,'normal'), width=50)
sub_btn=Button(window,text = 'Rename', command = submit)
#show_file_list(window)
name_entry.pack()
sub_btn.pack()
window.mainloop()

