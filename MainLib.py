# Main Lib
##############################################################################################
# Imports
import os
import ConfigHandler as Config
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
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
    @staticmethod

    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            Handler.log.info("Created file - "+event.src_path)
        elif event.event_type == 'modified':
            Handler.log.info("Modified file - "+event.src_path)
##############################################################################################

if __name__ == '__main__':
    logging.debug("root Start")
    FileWatcher.WatchDirectory = Config.ConfigRead('FileWatcher','WatchedDirectory','str')
    FileWatcher().run()