from tkinter import *
from tkvideo import tkvideo
from tkinter.messagebox import showinfo
import os, sys
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
root = Tk()
root.title('Rick Roll')
showinfo("💩💩💩", "Bạn đã sẵn sàng để lên đỉnh chưa ???")
video_label = Label(root)
video_label.pack()
player = tkvideo(os.path.join(resource_path("assets") ,"nothing.mp4"), video_label,
                 loop = 1, size = (700, 500))
player.play()
trollwindow = Toplevel(root)
trollwindow.title("You've been trolled!!!")
trollwindow.geometry("250x250")
img = PhotoImage(file=os.path.join(resource_path("assets"), "nothing.png"))
Label(
    trollwindow,
    image=img
).pack()
root.mainloop()