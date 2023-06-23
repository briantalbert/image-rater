from tkinter import *
from PIL import ImageTk, Image, ImageOps
from tkinter import filedialog
import os
from Picture import *
import random


def keydown(e):
    key = e.keysym
    leftidx = currentidx[0]
    rightidx = currentidx[1]
    if (key == 'Right'):
        picture_objects[rightidx].plus_one()
        picture_objects[leftidx].minus_one()
        
    elif (key == 'Left'):
        picture_objects[rightidx].minus_one()
        picture_objects[leftidx].plus_one()
        
    elif (key == 'Up'):
        picture_objects[rightidx].plus_one()
        picture_objects[leftidx].plus_one()
        
    elif (key == 'Down'):
        picture_objects[rightidx].minus_one()
        picture_objects[leftidx].plus_one()
    else:
        pass
        
    left_label.image = ''
    right_label.image = ''
    highscores()
    currentidx.pop()
    currentidx.pop()
    l, r = get_idx()
    show_images(l, r)
    
def highscores():
    sortedlist = sorted(picture_objects, key=lambda h: h.rating, reverse=True)
    clear_frame()
    for i in range(3):
        img = Image.open(sortedlist[i].path)
        img.thumbnail((250, 250))
        img = ImageTk.PhotoImage(img)
        newLabel = Label(master=frm_highscores)
        newLabel.image = img
        newLabel['image'] = newLabel.image
        newLabel.grid(row=0, column=i)


def clear_frame():
   for widgets in frm_highscores.winfo_children():
      widgets.destroy()
     
def opendir():
    left_label.image = ''
    right_label.image = ''
    if (currentidx):
        currentidx.pop()
        currentidx.pop()
    os.chdir(filedialog.askdirectory())
    get_file_list()

def get_file_list():
    files = os.listdir()
    picture_objects.clear()
    ctr = 0
    for file in files:
        if file.endswith(('.jpg', '.png', 'jpeg', '.gif')):
            if  (file.startswith('rsz')):
                pass
            else:
                new_picture = Picture(file, ctr)
                picture_objects.append(new_picture)
                ctr += 1
    l, r = get_idx()
    
    show_images(l, r)

def get_idx():
    l = random.randint(0, len(picture_objects) - 1)
    r = random.randint(0, len(picture_objects) - 1)
    while (l == r):
        r = random.randint(0, len(picture_objects) - 1)
    currentidx.append(l)
    currentidx.append(r)
    return l, r

def get_size(size):
    w = size[0]
    h = size[1]
    if (w > 300):
        w = 300
        ratio = size[0] / size[1]
        h = int(300/ratio)
    return w, h

def show_images(l, r):
    baseheight = 400
    
    leftimage = Image.open(picture_objects[l].path)
    hpercent = (baseheight/float(leftimage.size[1]))
    wsize = int((float(leftimage.size[0])*float(hpercent)))
    w, h = get_size(leftimage.size)
    leftimage = leftimage.resize((w, h), Image.Resampling.LANCZOS)
    leftimage = ImageTk.PhotoImage(leftimage)
    left_label.image = leftimage
    left_label['image'] = left_label.image

    
    rightimage = Image.open(picture_objects[r].path)
    hpercent = (baseheight/float(rightimage.size[1]))
    wsize = int((float(rightimage.size[0])*float(hpercent)))
    w, h = get_size(rightimage.size)
    rightimage = rightimage.resize((w, h), Image.Resampling.LANCZOS)
    rightimage = ImageTk.PhotoImage(rightimage)
    right_label.image = rightimage
    right_label['image'] = right_label.image

    left_label.grid(row=0)
    right_label.grid(row=0, column=1)

    

root = Tk()
root.geometry("700x800")
root.resizable(width=True, height=True)
root.title('Image Rater')
root.bind("<KeyPress>", keydown)
btn = Button(master=root, text='choose folder', command=opendir).pack()

frm_photos = Frame(master=root, width=650, height=500, padx=5, pady=5)
frm_photos.place(x=25, y=50)

frm_highscores = Frame(master=root, width=650, height= 300, padx=5, pady=5)
frm_highscores.place(x=75, y=455)

left_label = Label(master=frm_photos)
right_label = Label(master=frm_photos)

picture_objects = []
currentidx = []

root.mainloop()