from tkinter import *
from PIL import Image, ImageTk

G_WIDTH=800
G_HEIGHT=1600

root = Tk()
root.title("Set Time code")
root.geometry(f'{G_WIDTH}x{G_HEIGHT}')

img = Image.open('1.png')
new_size = (int(img.size[0]*G_WIDTH/img.size[1]),G_WIDTH)
img = img.resize(new_size, Image.ANTIALIAS)
ph = ImageTk.PhotoImage(img)

fr = Frame(root, height=G_HEIGHT, width=G_WIDTH)
cv = Canvas(fr, height=G_HEIGHT, width=G_WIDTH, highlightthickness=0)
cv.create_image(0,0, image=ph, anchor="nw")

fr.pack()
cv.pack(expand="Yes", side="top", fill="both", ipadx=0, ipady=0, padx=0, pady=0)

root.mainloop()
