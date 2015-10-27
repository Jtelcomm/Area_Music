#! /usr/bin/env python
# play mp3 from cron task
# Import moduals and functions


import os, sys

os.system('omxplayer -o local loop.mp3')



sys.exit()