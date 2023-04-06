# Main Lib
##############################################################################################
# Imports
import os
import ConfigHandler as Config
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
from tkinter import *
from tkinter import messagebox
##############################################################################################
# Declarations
logging.getLogger().setLevel(logging.DEBUG)
##############################################################################################
# Classes and Definitions
class FileWatcher:  
    log = logging.getLogger('FileWatcher') 
    WatchDirectory = ""
    SleepTime = 5
 
    def __init__(self):
        self.observer = Observer()
        
    def run(self):
        self.observer.schedule(Handler(), self.WatchDirectory, recursive = True)
        self.log.debug("FileWatcher Started")
        self.observer.start()
        try:
            while True:
                time.sleep(self.SleepTime)
        except:
            self.observer.stop()
            self.log.debug("FileWatcher Stopped")
        self.observer.join()
##############################################################################################
class Handler(FileSystemEventHandler):
    log = logging.getLogger("Handler")
    WaitTime = 5
    @staticmethod

    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            Handler.log.info("Created file - "+event.src_path)
            time.sleep(Handler.WaitTime)
        elif event.event_type == 'modified':
            Handler.log.info("Modified file - "+event.src_path)
            #subprocess.Popen(r'explorer "'+event.src_path+'"')
            FileProgress(event.src_path)
##############################################################################################
#def FileOpen(filepath,alt=1):
#    filepath = filepath.replace('/','\\')
#    match alt:
#        case 0 : os.startfile(filepath)
#        case 1 : subprocess.Popen(r'explorer "'+filepath+'"')
##############################################################################################
def FileProgress(filepath,setting = 0):
    log = logging.getLogger("FileProgress")
    log.info("Started File Handling")
    try: 
        value = messagebox.askyesnocancel('ProtocolWatcher','Bol nájdeny nový prokotol: \n'+str(filepath)+'\n Chcete ho otvorit?')
    except: logging.warning("Failed to ask question")
    match setting:
        case 0 :
            match value:
                case True  : subprocess.Popen(r'explorer "'+filepath.replace('/','\\')+'"')
                case False : pass
                case None  : os._exit(0)
                case _ : logging.warning("Failed to choose value of messagebox")
        case _ : pass
    time.sleep(1)


