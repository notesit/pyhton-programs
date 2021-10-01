# importing the Packages
import cv2
import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
root = tk.Tk()
root.title("Color to blackNwhite Convertor")
root.config(bg='#FFFAFA')
def selectimage():
   global panelA,panelB #used two global variables to create two panels
   global gray_image # for saving reference to the gray image
   location = fd.askopenfilename()
if len(location) > 0:
    image = cv2.imread(location)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #convert the images to PIL format...
    image = Image.fromarray(image)
    gray_image = Image.fromarray(gray) # save the gray image
    # ...and then to ImageTk format
    image = ImageTk.PhotoImage(image)
    gray = ImageTk.PhotoImage(gray_image) # use 'gray_image' instead of 'gray'
if panelA is None or panelB is None:
    panelA = tk.Label(image=image)
    panelA.image = image
    panelA.pack(side="left", padx=10, pady=10)
    panelB = tk.Label(image=gray)
    panelB.image = gray
    panelB.pack(side="right", padx=10, pady=10)
else:
    panelA.configure(image=image)
    panelB.configure(image=gray)
    panelA.image = image
    panelB.image = gray
    panelA = None
    panelB = None
    gray_image = None
    bframe = tk.Frame(root)
    bframe.pack(side="bottom", fill="both", expand="yes")
    btn = tk.Button(bframe, text="Select an image",font=('arial',10,'bold'),bg="cyan",
    command=selectimage)
    btn.config(height=5,width=15)
    btn.pack(side="left", fill="x", expand=1)
### function to save the gray image
def save_image():
  if gray_image:
   # ask the filename to be used as the output
    filename = fd.asksaveasfilename()
  if filename:
    gray_image.save(filename) # save the gray image
tk.Button(bframe, text="Save image", font="arial 10 bold", bg="gold", width=15,
height=5, command=save_image).pack(side="left", fill="x", expand=1)

# kick off the GUI
root.mainloop()
