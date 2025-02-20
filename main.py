import tkinter
from tkinter import *
from PIL import ImageTk
import platform

from pc import pc_info, python_info

width = 750
height = 400

version_os = None

root = tkinter.Tk()
root.title("System")
root.geometry(f"{width}x{height}+700+250")
root.minsize(width, height)
root.maxsize(width, height)

label = Label(text=pc_info, justify=LEFT)
label.place(relx=.0, rely=.0)

label2 = Label(text=python_info, justify=LEFT)
label2.place(relx=.0, rely=.7)

img = ImageTk.PhotoImage(file="python.png")
panel = Label(root, image = img)
panel.place(relx=.8, rely=.7)

if platform.system() == "Windows":
    version_os = "windows.png"
elif platform.system() == "Linux":
    version_os = "linux.png"
elif platform.system() == "Darwin":
    version_os = "mac.png"

os_img = ImageTk.PhotoImage(file=version_os)
panel_os = Label(root, image = os_img)
panel_os.place(relx=.8, y=20)

root.mainloop()