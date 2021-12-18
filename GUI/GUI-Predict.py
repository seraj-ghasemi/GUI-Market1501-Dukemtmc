#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  11 12:55:49 2021
@authors: 
"""

from tkinter import *
import numpy as np
import os
from PIL import Image , ImageTk

master = Tk()

#main_path = 'C:/Users/ASUS/Desktop/dukemtmc/DukeMTMC-reID/DukeMTMC-reID/'
#names = os.listdir(main_path)
#names.sort()
img = Image.open('C:/Users/ASUS/Desktop/dukemtmc/GUI/info_for_label.jpg')
img = img.resize((120, 120), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

#path_attr = 'C:/Users/ASUS/Desktop/dukemtmc/DukeMTMC-reID/DukeMTMC-reID/Predict-label/final_attr_org.npy'
#path_start = 'C:/Users/ASUS/Desktop/dukemtmc/DukeMTMC-reID/DukeMTMC-reID/Predict-label/final_stop.npy'

h_color_var = IntVar(0)
h_attr_var = IntVar(0)
b_color_var = IntVar(0)
b_attr_var = IntVar(0)
bag_var = IntVar(0)
umb_var = IntVar(0)
face_var = IntVar(0)
l_color_var = IntVar(0)
l_attr_var = IntVar(0)
f_color_var = IntVar(0)
f_attr_var = IntVar(0)
c_color_var = IntVar(0)
c_attr_var = IntVar(0)
race_var = IntVar(0)

check = IntVar(0)

var = np.zeros((85),dtype=IntVar)

for v in range(len(var)):
    var[v] = IntVar()


def Predict():
    m = 0
    check.set(0)
    for j in range(len(var)):
        var[j].set(0)
    h_color_var.set(0)
    h_attr_var.set(0)
    b_color_var.set(0)
    b_attr_var.set(0)
    bag_var.set(0)
    umb_var.set(0)
    face_var.set(0)
    l_color_var.set(0)
    l_attr_var.set(0)
    f_color_var.set(0)
    f_attr_var.set(0)
    c_color_var.set(0)
    c_attr_var.set(0)
    race_var.set(0)
"""
"""    
def error_check():
    if h_attr_var.get() == 0:
        error1.config(text = 'head attr' , bg='red')
        pass
    elif h_color_var.get() == 0 and h_attr_var.get() != 5:
        error1.config(text = 'head color' , bg='red')
        pass
    elif b_attr_var.get() == 0:
        error1.config(text = 'body attr' , bg='red')
        pass
    elif b_color_var.get() == 0:
        error1.config(text = 'body color' , bg='red')
        pass
    elif l_attr_var.get() == 0:
        error1.config(text = 'leg attr' , bg='red')
        pass
    elif l_color_var.get() == 0 and l_attr_var.get() != 51:
        error1.config(text = 'leg color' , bg='red')
        pass
    elif f_attr_var.get() == 0:
        error1.config(text = 'foot attr' , bg='red')
        pass
    elif f_color_var.get() == 0 and f_attr_var.get() != 65:
        error1.config(text = 'foot color' , bg='red')
        pass

    elif c_attr_var.get() == 0:
        error1.config(text = 'cap attr' , bg='red')
        pass
    elif c_color_var.get() == 0 and c_attr_var.get() != 14 and c_attr_var.get() != 13:
        error1.config(text = 'cap color' , bg='red')
        pass

    elif bag_var.get() == 0:
        error1.config(text = 'backpack' , bg='red')
        pass
    else:
        if f_attr_var.get() == 65:
            f_color_var.set(0)
        if l_attr_var.get() == 51:
            l_color_var.set(0)
        if c_attr_var.get() == 14:
            c_color_var.set(0)
            h_attr_var.set(5)
            face_var.set(47)
            race_var.set(84)
        if c_attr_var.get() == 13:
            c_color_var.set(0)
        if h_attr_var.get() == 5:
            h_color_var.set(0)

        #if var[81].get() == 1:
        #    face_var.set(47)
        #    race_var.set(84)
        
        for j in range(1,76):
            var[j].set(0)
        for j in range(82,85):
            var[j].set(0)
        
        if h_color_var.get() != 0:
            var[h_color_var.get()].set(1)
        if h_attr_var.get() != 0:
            var[h_attr_var.get()].set(1)
        if b_color_var.get() != 0:
            var[b_color_var.get()].set(1)
        if b_attr_var.get() != 0:
            var[b_attr_var.get()].set(1)
        if bag_var.get() != 0:
            var[bag_var.get()].set(1)
        if umb_var.get() != 0:
            var[umb_var.get()].set(1)
        if face_var.get() != 0:
            var[face_var.get()].set(1)
        if l_color_var.get() != 0:
            var[l_color_var.get()].set(1)
        if l_attr_var.get() != 0:
            var[l_attr_var.get()].set(1)
        if f_color_var.get() != 0:
            var[f_color_var.get()].set(1)
        if f_attr_var.get() != 0:
            var[f_attr_var.get()].set(1)
        if race_var.get() != 0:
            var[race_var.get()].set(1)
    
        if c_color_var.get() != 0:
            var[c_color_var.get()].set(1)
        if c_attr_var.get() != 0:
            var[c_attr_var.get()].set(1)

        error1.config(text = 'all set' , bg='green')
        check.set(1)

        
# we need three button to go next image or come back to previous image or quit 
picture = Label(master , image = img)
picture.grid(row=9 ,column=7)
Quit = Button(master, text='Quit', command=master.quit).grid(row=24,column=17, pady=4)
Check = Button(master, text='Check', command=error_check).grid(row=24,column=6, pady=4)
Next_butt = Button(master, text='Predict', command=Predict).grid(row=24 , column=8)
err1 = Entry(master, width=10)
err1.grid(column=7, row=24)

# now we need 58 checkbutton in five main categories: gender, head, body, leg, foot
# IntVar() is a holder of chechbutton number

attr_colour = [
    "male/female",

    "hairless","short hair","longhair(straight)","knot","unvisible(hair)",
    "burnette","blonde","gray/white","black",

    'cap',"snowcap","hoodiecap","no cap", "unvisible(cap)",
    "c_white","c_purple","c_pink","c_blue","c_green","c_red","c_brown","c_yellow","c_gray","c_black",  

    "T-shirt/shirt","jacket/sweatshirt","overcoat","hoodie",
    "b_white","b_purple","b_pink","b_blue","b_green","b_red","b_brown","b_yellow","b_gray","b_black",  

    "backpack","bag/handbag",'no bags',
    "umbrella(open)","umbrella(closed)","no umbrella",
    "beard","shaved","hidden",

    "pants","shorts","skirt","unvisible",
    "l_white","l_purple","l_pink","l_blue","l_green","l_red","l_brown","l_yellow","l_gray","l_black",

    'formal shoes',"sneakers","high boots",'hidden',
    "f_white","f_purple","f_pink","f_blue","f_green","f_red","f_brown","f_yellow","f_gray","f_black",

    "sunglasses","headphone","gloves","scarf","tie",

    "front/back",

    "white", "black", "unkown"
    ]

for i,attr in enumerate(attr_colour):
    if i == 0:
        Radiobutton(master, text='male', variable=var[i], value=0).grid(column=10,row=21)
        Radiobutton(master, text='female', variable=var[i], value=1).grid(column=11,row=21)
    elif  0 < i < 10:
        if attr[-8:] == 'burnette':
            Radiobutton(master, text=attr, variable=h_color_var, value=i, bg = 'brown4').grid(column=i+5,row=1, sticky=W)
        elif attr[-6:] == 'blonde':
            Radiobutton(master, text=attr, variable=h_color_var, value=i, bg = 'yellow').grid(column=i+5,row=1, sticky=W)
        elif attr[-10:] == 'gray/white':
            Radiobutton(master, text=attr, variable=h_color_var, value=i, bg = 'gray').grid(column=i+5,row=1, sticky=W)
        elif attr[-5:] == 'black':
            Radiobutton(master, text=attr, variable=h_color_var, value=i, fg = 'gray', bg = 'black').grid(column=i+5,row=1, sticky=W)
        else:
            Radiobutton(master, text=attr, variable=h_attr_var, value=i).grid(column=i-1,row=1, sticky=W)
    elif 9 < i < 25:
        if attr[-5:] == 'white':
            Radiobutton(master, text=attr, variable=c_color_var , value=i, bg = 'white').grid(column=i-10,row=2, sticky=W)   
        elif attr[-6:] == 'purple':
            Radiobutton(master, text=attr, variable=c_color_var , value=i, bg = 'purple').grid(column=i-10,row=2, sticky=W)
        elif attr[-4:] == 'pink':
            Radiobutton(master, text=attr, variable=c_color_var , value=i, bg = 'hot pink').grid(column=i-10,row=2, sticky=W)
        elif attr[-4:] == 'blue':
            Radiobutton(master, text=attr, variable=c_color_var , value=i, bg = 'blue').grid(column=i-10,row=2, sticky=W)
        elif attr[-5:] == 'green':
            Radiobutton(master, text=attr, variable=c_color_var , value=i, bg = 'green').grid(column=i-10,row=2, sticky=W)
        elif attr[-3:] == 'red':
            Radiobutton(master, text=attr, variable=c_color_var , value=i, bg = 'red').grid(column=i-10,row=2, sticky=W)
        elif attr[-5:] == 'brown':
            Radiobutton(master, text=attr, variable=c_color_var , value=i, bg = 'brown4').grid(column=i-10,row=2, sticky=W)
        elif attr[-6:] == 'yellow':
            Radiobutton(master, text=attr, variable=c_color_var , value=i, bg = 'yellow').grid(column=i-10,row=2, sticky=W)
        elif attr[-4:] == 'gray':
            Radiobutton(master, text=attr, variable=c_color_var , value=i, bg = 'gray').grid(column=i-10,row=2, sticky=W)
        elif attr[-5:] == 'black':
            Radiobutton(master, text=attr, variable=c_color_var , value=i, fg = 'gray', bg = 'black').grid(column=i-10,row=2, sticky=W)
        else:
            Radiobutton(master, text=attr, variable=c_attr_var, value=i).grid(column=i-10,row=2, sticky=W)

    elif 24 < i < 39:
        if attr[-5:] == 'white':
            Radiobutton(master, text=attr, variable=b_color_var , value=i, bg = 'white').grid(column=i-24,row=3, sticky=W)   
        elif attr[-6:] == 'purple':
            Radiobutton(master, text=attr, variable=b_color_var , value=i, bg = 'purple').grid(column=i-24,row=3, sticky=W)
        elif attr[-4:] == 'pink':
            Radiobutton(master, text=attr, variable=b_color_var , value=i, bg = 'hot pink').grid(column=i-24,row=3, sticky=W)
        elif attr[-4:] == 'blue':
            Radiobutton(master, text=attr, variable=b_color_var , value=i, bg = 'blue').grid(column=i-24,row=3, sticky=W)
        elif attr[-5:] == 'green':
            Radiobutton(master, text=attr, variable=b_color_var , value=i, bg = 'green').grid(column=i-24,row=3, sticky=W)
        elif attr[-3:] == 'red':
            Radiobutton(master, text=attr, variable=b_color_var , value=i, bg = 'red').grid(column=i-24,row=3, sticky=W)
        elif attr[-5:] == 'brown':
            Radiobutton(master, text=attr, variable=b_color_var , value=i, bg = 'brown4').grid(column=i-24,row=3, sticky=W)
        elif attr[-6:] == 'yellow':
            Radiobutton(master, text=attr, variable=b_color_var , value=i, bg = 'yellow').grid(column=i-24,row=3, sticky=W)
        elif attr[-4:] == 'gray':
            Radiobutton(master, text=attr, variable=b_color_var , value=i, bg = 'gray').grid(column=i-24,row=3, sticky=W)
        elif attr[-5:] == 'black':
            Radiobutton(master, text=attr, variable=b_color_var , value=i, fg = 'gray', bg = 'black').grid(column=i-24,row=3, sticky=W)
        else:
            Radiobutton(master, text=attr, variable=b_attr_var, value=i).grid(column=i-24,row=3, sticky=W)
    
    elif 38 < i < 42:
        if i == 39:
            Radiobutton(master, text=attr, variable=bag_var, value=i).grid(column=2,row=21, sticky=W)
        if i == 40:
            Radiobutton(master, text=attr, variable=bag_var, value=i).grid(column=3,row=21, sticky=W)
        if i == 41:
            Radiobutton(master, text=attr, variable=bag_var, value=i).grid(column=4,row=21, sticky=W)
    elif 41 < i < 45:
        if i == 42:
            Radiobutton(master, text=attr, variable=umb_var, value=i).grid(column=2,row=22, sticky=W)
        if i == 43:
            Radiobutton(master, text=attr, variable=umb_var, value=i).grid(column=3,row=22, sticky=W)
        if i == 44:
            Radiobutton(master, text=attr, variable=umb_var, value=i).grid(column=4,row=22, sticky=W)
    elif 44 < i < 48:
        if i == 45:
            Radiobutton(master, text=attr, variable=face_var, value=i).grid(column=2,row=23, sticky=W)
        if i == 46:
            Radiobutton(master, text=attr, variable=face_var, value=i).grid(column=3,row=23, sticky=W)
        if i == 47:
            Radiobutton(master, text=attr, variable=face_var, value=i).grid(column=4,row=23, sticky=W)
    elif 47 < i < 62:
        if attr[-5:] == 'white':
            Radiobutton(master, text=attr, variable=l_color_var , value=i, bg = 'white').grid(column=i-47,row=4, sticky=W)   
        elif attr[-6:] == 'purple':
            Radiobutton(master, text=attr, variable=l_color_var , value=i, bg = 'purple').grid(column=i-47,row=4, sticky=W)
        elif attr[-4:] == 'pink':
            Radiobutton(master, text=attr, variable=l_color_var , value=i, bg = 'hot pink').grid(column=i-47,row=4, sticky=W)
        elif attr[-4:] == 'blue':
            Radiobutton(master, text=attr, variable=l_color_var , value=i, bg = 'blue').grid(column=i-47,row=4, sticky=W)
        elif attr[-5:] == 'green':
            Radiobutton(master, text=attr, variable=l_color_var , value=i, bg = 'green').grid(column=i-47,row=4, sticky=W)
        elif attr[-3:] == 'red':
            Radiobutton(master, text=attr, variable=l_color_var , value=i, bg = 'red').grid(column=i-47,row=4, sticky=W)
        elif attr[-5:] == 'brown':
            Radiobutton(master, text=attr, variable=l_color_var , value=i, bg = 'brown4').grid(column=i-47,row=4, sticky=W)
        elif attr[-6:] == 'yellow':
            Radiobutton(master, text=attr, variable=l_color_var , value=i, bg = 'yellow').grid(column=i-47,row=4, sticky=W)
        elif attr[-4:] == 'gray':
            Radiobutton(master, text=attr, variable=l_color_var , value=i, bg = 'gray').grid(column=i-47,row=4, sticky=W)
        elif attr[-5:] == 'black':
            Radiobutton(master, text=attr, variable=l_color_var , value=i, fg = 'gray', bg = 'black').grid(column=i-47,row=4, sticky=W)
        else:
            Radiobutton(master, text=attr, variable=l_attr_var, value=i).grid(column=i-47,row=4, sticky=W)
    elif 61 < i < 76:
        if attr[-5:] == 'white':
            Radiobutton(master, text=attr, variable=f_color_var , value=i, bg = 'white').grid(column=i-61,row=5, sticky=W)   
        elif attr[-6:] == 'purple':
            Radiobutton(master, text=attr, variable=f_color_var , value=i, bg = 'purple').grid(column=i-61,row=5, sticky=W)
        elif attr[-4:] == 'pink':
            Radiobutton(master, text=attr, variable=f_color_var , value=i, bg = 'hot pink').grid(column=i-61,row=5, sticky=W)
        elif attr[-4:] == 'blue':
            Radiobutton(master, text=attr, variable=f_color_var , value=i, bg = 'blue').grid(column=i-61,row=5, sticky=W)
        elif attr[-5:] == 'green':
            Radiobutton(master, text=attr, variable=f_color_var , value=i, bg = 'green').grid(column=i-61,row=5, sticky=W)
        elif attr[-3:] == 'red':
            Radiobutton(master, text=attr, variable=f_color_var , value=i, bg = 'red').grid(column=i-61,row=5, sticky=W)
        elif attr[-5:] == 'brown':
            Radiobutton(master, text=attr, variable=f_color_var , value=i, bg = 'brown4').grid(column=i-61,row=5, sticky=W)
        elif attr[-6:] == 'yellow':
            Radiobutton(master, text=attr, variable=f_color_var , value=i, bg = 'yellow').grid(column=i-61,row=5, sticky=W)
        elif attr[-4:] == 'gray':
            Radiobutton(master, text=attr, variable=f_color_var , value=i, bg = 'gray').grid(column=i-61,row=5, sticky=W)
        elif attr[-5:] == 'black':
            Radiobutton(master, text=attr, variable=f_color_var , value=i, fg = 'gray', bg = 'black').grid(column=i-61,row=5, sticky=W)
        else:
            Radiobutton(master, text=attr, variable=f_attr_var, value=i).grid(column=i-61,row=5, sticky=W)
    elif 75 < i < 81:
        Checkbutton(master, text=attr, variable=var[i]).grid(column=i-74,row=20, sticky=W)
    elif 80 < i < 82:
            Radiobutton(master, text='front', variable=var[i], value=0).grid(column=10,row=20, sticky=W)
            Radiobutton(master, text='back', variable=var[i], value=1).grid(column=11,row=20, sticky=W)
    elif 81 < i < len(attr_colour):
        if i == 82:
            Radiobutton(master, text=attr, variable=race_var, value=i).grid(column=2,row=24, sticky=W)
        if i == 83:
            Radiobutton(master, text=attr, variable=race_var, value=i).grid(column=3,row=24, sticky=W)
        if i == 84:    
            Radiobutton(master, text=attr, variable=race_var, value=i).grid(column=4,row=24, sticky=W)


accessories = Label(master, text = 'Accessories:')
accessories.grid(column=1,row=20)
body = Label(master, text = 'Body:')
body.grid(column=9,row=20)
gender = Label(master, text = 'Gender:')
gender.grid(column=9,row=21)
backpack = Label(master, text = 'Backpack:')
backpack.grid(column=1,row=21)
umbrella = Label(master, text = 'Umbrella:')
umbrella.grid(column=1,row=22)
face = Label(master, text = 'Face:')
face.grid(column=1,row=23)
race = Label(master, text = 'Race:')
race.grid(column=1,row=24)

Network = Label(master, text = 'Network:')
Network.grid(column=9,row=22)

error1 = Label(master, text = 'do the check' , bg='yellow')
error1.grid(column=7,row=23)

label = Label(master)
label.grid(row=23, pady=4)
master.mainloop()