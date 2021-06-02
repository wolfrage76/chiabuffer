import shutil
import glob
import keyboard
from datetime import datetime

ext = "plot" # extension we are looking for (you can test usuing .txt files, etc)
minSize = 800 # Size in GB - if a dest drive has less free space remaining, it's removed from list

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print('Started : ' + current_time)
print('To exit, press:  q')
sources = ["/media/chaos/WD Blue/Chia Relocate"] # Comma separated list of dirs to monitor

destinations = ["/media/chaos/Seagate Expansion Drive1/Farm"] # comma separated list of dirs to move plots into

#######################
#         begin       #
#######################

jobs = []

def main():
    file_count = -1
    for dest in destinations:
        total, used, free = shutil.disk_usage(dest)
        if (free // (2 ** 30)) > minSize:
                jobs.append(dest)
    for source in sources:
        for file in glob.glob(source + "*." + ext):
            print("File found for moving: " + file)
            file_count += 1
            try:
               shutil.move(file, jobs[file_count % len(jobs)])
               print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + ' ' + file + ':  copied successfully')

            # If source and destination are same
            except shutil.SameFileError:
                print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + ' ' + file + ': Source and destination '
                                                                                   'represents the same file in '
                      + (jobs[file_count % len(jobs)]))

            # If there is any permission issue
            except PermissionError:
                print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + ' ' + file + ": Permission denied.")

            # For other errors
            except:
                print("Error occurred while copying file.")


while True:
    main()
    if keyboard.is_pressed("q"):
        print("q pressed, ending loop")
        break
