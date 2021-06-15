import shutil
import glob
import keyboard
from datetime import datetime

ext = "plot"
minSize = 800

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print('Started : ' + current_time)
sources = ["/mnt/tmp1/", "/mnt/tmp2/"]

jobs = []

def main():
    file_count = -1
    for dest in destinations:
        total, used, free = shutil.disk_usage(dest)
        if (free // (2 ** 30)) > minSize:
                jobs.append(dest)
    for source in sources:
        for file in glob.glob(source + "*." + ext):
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
