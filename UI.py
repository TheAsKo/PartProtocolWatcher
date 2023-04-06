# UI
##############################################################################################
# Imports
import MainLib as Lib
import logging
import ConfigHandler as Config
from tkinter import *
from tkinter import ttk
##############################################################################################
# Declarations
logging.getLogger().setLevel(logging.DEBUG)
root = Tk()
root.title("Protocol Watcher")
##############################################################################################
# Classes and Definitions
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
##############################################################################################
def ButtonPress(arg):
    logging.debug("Assigning ID: "+str(arg))
    match arg:
        case 1 : Config.ConfigWrite('FileWatcher','watcheddirectory',Config.ConfigRead('FileWatcher','DM1Directory','str'),'str')
        case 2 : Config.ConfigWrite('FileWatcher','watcheddirectory',Config.ConfigRead('FileWatcher','DM2Directory','str'),'str')
        case 3 : Config.ConfigWrite('FileWatcher','watcheddirectory',Config.ConfigRead('FileWatcher','EMDirectory','str'),'str')
        case 4 : Config.ConfigWrite('FileWatcher','watcheddirectory',Config.ConfigRead('FileWatcher','TestDirectory','str'),'str')
        case 0 : pass #NEED TO FINISH AUTODETECT FUNC
        case _ : logging.critical("Failed passing command from UI")
    Lib.FileWatcher.WatchDirectory = Config.ConfigRead('FileWatcher','WatchedDirectory','str')
    root.lift()
    root.destroy()
    Lib.FileWatcher().run()
##############################################################################################    

    

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="DM1",command=lambda:ButtonPress(1)).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="DM2",command=lambda:ButtonPress(2)).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="EM",command=lambda:ButtonPress(3)).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="AutoDetect",command=lambda:ButtonPress(0),state=DISABLED).grid(column=2, row=4, sticky=W)
ttk.Button(mainframe, text="Test",command=lambda:ButtonPress(4)).grid(column=2, row=5, sticky=W)


ttk.Label(mainframe, text="13376_400").grid(column=1, row=2, sticky=N)
ttk.Label(mainframe, text="13376_401").grid(column=2, row=2, sticky=N)
ttk.Label(mainframe, text="13114_402").grid(column=3, row=2, sticky=N)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

center(root)


if __name__ == '__main__':
    logging.debug("Root Start")
    root.mainloop()