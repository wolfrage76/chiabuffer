# chiabuffer
Python script to monitor a Buffer drive and move plots to a dest drive. Will not include destination drives with less than `minSize` amount.
Usage:

`sudo python3 buffer.py`

Yes, you need sudo because the shutil module requires it.  

Settings to edit:

ext = "plot" # extension we are looking for (you can test usuing .txt files, etc)

minSize = 800 # Size in GB - if a dest drive has less free space remaining, it's removed from list

sources = ["/mnt/from"] # Comma separated list of dirs to monitor

destinations = ["/mnt/to"] # comma separated list of dirs to move plots into


