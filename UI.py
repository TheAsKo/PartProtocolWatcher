import MainLib as Lib
import logging
import ConfigHandler as Config
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Protocol Watcher")

def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="DM1",).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="DM2",).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="EM",).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="AutoDetect",).grid(column=2, row=4, sticky=W)


ttk.Label(mainframe, text="13376_400").grid(column=1, row=2, sticky=N)
ttk.Label(mainframe, text="13376_401").grid(column=2, row=2, sticky=N)
ttk.Label(mainframe, text="13114_402").grid(column=3, row=2, sticky=N)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

center(root)


if __name__ == '__main__':
    logging.debug("root Start")
    Lib.FileWatcher.WatchDirectory = Config.ConfigRead('FileWatcher','WatchedDirectory','str')
    Lib.FileWatcher().run()
    root.mainloop()