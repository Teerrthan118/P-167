from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root= Tk()
root.title("Working On Canvas Using Functions")
root.geometry("1000x590")

canvas=Canvas(root, width = 990, height=490, bg = "white", highlightbackground="gray")
canvas.pack()

label1 = Label(root, text="Choose Colour")
fillcolour=["green","yellow","red","blue"]
colour_dropdown = ttk.Combobox(root, state="readonly", values = fillcolour, width = 10)
startx = Label(root, text="startx")
coordinates_values = [10,50,100,200,300,400,500,600,700,800,900]
d1 = ttk.Combobox(root, state="readonly", values = coordinates_values, width = 10)
starty = Label(root, text="starty")
d2 = ttk.Combobox(root, state="readonly", values = coordinates_values, width = 10)
endx = Label(root, text="endx")
d3 = ttk.Combobox(root, state="readonly", values = coordinates_values, width = 10)
endy = Label(root, text="endy")
d4 = ttk.Combobox(root, state="readonly", values = coordinates_values, width = 10)

def circle(event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress = 'c'
    draw(keypress,oldx,oldy,newx,newy)
    
def rectangle(event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress = 'r'
    draw(keypress,oldx,oldy,newx,newy)
    
def line(event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress = 'l'
    draw(keypress,oldx,oldy,newx,newy)
    
def draw(keypress,oldx,oldy,newx,newy):
    color = colour_dropdown.get()
    if keypress=='c':
        draw_circle=canvas.create_oval(oldx,oldy,newx,newy, fill=color)
        
    if keypress=='r':
        draw_rectangle=canvas.create_rectangle(oldx,oldy,newx,newy, fill=color)
        
    if keypress=='l':
        draw_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=color)

root.bind("<c>",circle)
root.bind("<r>",rectangle)
root.bind("<l>",line)

label1.place(relx=0.6, rely=0.9)
colour_dropdown.place(relx=0.8, rely = 0.9)
startx.place(relx=0.1, rely=0.85)
d1.place(relx=0.2, rely = 0.85)
starty.place(relx=0.3, rely=0.85)
d2.place(relx=0.4, rely = 0.85)
endx.place(relx=0.5, rely=0.85)
d3.place(relx=0.6, rely = 0.85)
endy.place(relx=0.7, rely=0.85)
d4.place(relx=0.8, rely = 0.85)


root.mainloop()