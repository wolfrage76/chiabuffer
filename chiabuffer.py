import time

import shutil

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

dest_drive = "/mnt/tmpusb2/" #where do you want the .plot files moved to?
monitor_path = "/mnt/buffer/" #What folder do you want monitored?

if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = True
    case_sensitive = False
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):
    #print(f"hey, {event.src_path} has been created!"
    return

def on_moved(event):
    evt = event
    #print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")
    get_ext = evt.dest_path[-5:]
    if get_ext == ".plot":
        shutil.move(evt.dest_path, dest_drive)

#my_event_handler.on_created = on_created
#my_event_handler.on_deleted = on_deleted
#my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved


go_recursively = False
my_observer = Observer()
my_observer.schedule(my_event_handler, monitor_path, recursive=go_recursively)

my_observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
