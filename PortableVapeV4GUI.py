# Imports [DO NOT CHANGE]
import os
import json
import requests
import time
import tkinter
import itertools
import psutil
import subprocess
import pyautogui
import datetime
import tempfile
import random
import shutil
import re
import sys
from colorama import init, Fore, Back, Style
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from urllib.request import Request, urlopen

# Colour Setup
init(convert=True)

# Lists / Variables
PREFETCH = "[] " # [LEAVE AS IS] For the fake UI.
ABC = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] # [LEAVE AS IS] For generating random names.
FULL_PATH = "" # Gather file location of executed. [IMPORTANT] [LEAVE AS IS]

# Generate TEMP folder (Random name - Defined in FULL_PATH) and images for GUI
def generateFiles():
    global DOWNLOADED
    global FULL_PATH # Make global.
    # Generate Tempfolder name.
    temp = ""
    
    for i in range(0,20): # [CAN BE CHANGED FOR EXTRA RANDOM] Generate 20 char long folder in \AppData\Local\Temp.
        temp = temp + str(ABC[random.randint(0,len(ABC)-1)]) # Gen name.
        
    full_path = os.path.join(tempfile.gettempdir(), str(temp)) # Create Pathing.

    # Assign to FULL_PATH (Global).
    FULL_PATH = full_path

    # Create Path.
    os.mkdir(full_path)

    # MAIN background.
    image_url = "https://raw.githubusercontent.com/NightTabGit/FakeV4-GUI/main/V4Gui.PNG"
    filename = image_url.split("/")[-1]

    # Ico file.
    image_url2 = "https://gitcdn.link/cdn/NightTabGit/FakeV4-GUI/main/Default.ico"
    filename2 = image_url2.split("/")[-1]

    # Default file.
    image_url3 = "https://gitcdn.link/cdn/NightTabGit/FakeV4-GUI/main/Blank.png"
    filename3 = image_url3.split("/")[-1]

    # Download images to TEMP folder.

    flags = 0
    # Download background locally (NOT in Temp).
    r = requests.get(image_url, stream = True)
    if r.status_code == 200: # Check for success.
        r.raw.decode_content = True
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f) # Finish download.
    else:
        flags = flags + 1
        pass
    shutil.copy("V4Gui.png", full_path) # Send to TEMP folder.
    os.remove("V4Gui.png") # Remove local PNG.

    r = requests.get(image_url2, stream = True)
    if r.status_code == 200: # Check for success.
        r.raw.decode_content = True
        with open(filename2,'wb') as f:
            shutil.copyfileobj(r.raw, f) # Finish download.
    else:
        flags = flags + 1
        pass
    shutil.copy("Default.ico", full_path) # Send to TEMP folder.
    os.remove("Default.ico") # Remove local PNG.

    if flags == 0:
         DOWNLOADED = True
    else:
         DOWNLOADED = False # No Images = No GUI (CANCEL REQ).

# Vape GUI.
def vapeGUI():
    # Setup window.
    width = 630 # Width of window.
    height = 360 # Height of window.
    
    root = tkinter.Tk() # Name.
    
    w, h = int(width), int(height) # Heigher, Width.
    
    canvas = tkinter.Canvas(root, width=w, height=h, highlightthickness=0) # Start canvas (Hidden borders).
    
    filename = PhotoImage(file = os.path.join(FULL_PATH + "\V4Gui.png")) # Set background.
    image = canvas.create_image(int(width), 0, anchor=NE, image=filename,) # Set in middle.
    canvas.pack(fill='both') # Pack
    
    root.eval('tk::PlaceWindow . center') # Window in center of screen.
    if isinstance(root, Tk): # Determine when packed.
        master = root  # Root window.
    else:
        master = root.master
        
    # Drag window code [DO NOT CHANGE].

    x, y = 0, 0 # Set at 0.
    def mouseMotion(event): # Drag event.
        global x, y
        offset_x, offset_y = event.x - x, event.y - y  
        new_x = master.winfo_x() + offset_x
        new_y = master.winfo_y() + offset_y
        new_geometry = f"+{new_x}+{new_y}"
        master.geometry(new_geometry)

    def mousePress(event): # Detect mouse press.
        global x, y
        count = time.time()
        x, y = event.x, event.y

    root.bind("<B1-Motion>", mouseMotion) # Bind down + up.
    root.bind("<Button-1>", mousePress)

    def destroyWindow(): # Destroy window.
        fadeOut()
        root.destroy()

    def minimizeWindow(): # Hide (Temporary) window.
        fadeOut()
        root.state('withdrawn') # Hide.
        time.sleep(0.2) # Wait 2 seconds before showing again (Make it seem glitched).
        root.state('normal') # Show.
        fadeInFast()

    def fadeIn():
        Alpha = 0.0
        root.attributes("-alpha", Alpha) # Alpha (Window).
        while 1.0 > Alpha :
            Alpha = Alpha + 0.04 # Increment by 0.04 per 0.005s.
            root.attributes("-alpha", Alpha) # Update alpha value.
            time.sleep(0.005)

    def fadeInFast():
        Alpha = 0.0
        root.attributes("-alpha", Alpha) # Alpha (Window).
        while 1.0 > Alpha :
            Alpha = Alpha + 0.2 # Increment by 0.2 per 0.005s.
            root.attributes("-alpha", Alpha) # Update alpha value.
            time.sleep(0.005)
            
    def fadeOut():
        Alpha = 1.0
        root.attributes("-alpha", Alpha) # Alpha (Window).
        while Alpha > 0.1:
            Alpha = Alpha - 0.2 # Increment by -0.2 per 0.005s.
            root.attributes("-alpha", Alpha) # Update alpha value.
            time.sleep(0.005)
        
    ## Launch code.
    Alpha = 0
    root.resizable(False, False) # Stops resizing.
    root.title(' ')
    root.iconbitmap(os.path.join(FULL_PATH + "\Default.ico"))
    root.mainloop() # Start loop.

##
##
##
# Main GUI / Code.
##
##
##

# Generate files (TEMP).
try:
    generateFiles()
except:
    pass

# GUI / Spoof vape.
print()
print(Fore.WHITE + str(PREFETCH) + Fore.RED + "Vape V4 v4.3 Patcher v2.1")
print()
time.sleep(1)
print(Fore.WHITE + str(PREFETCH) + Fore.RED + "Minecraft not found...") # Spoof no MC.
print()

time.sleep(0.1) # Slight delay.
if DOWNLOADED == True:
     vapeGUI()
else:
     print(Fore.WHITE + str(PREFETCH) + Fore.RED + "ERROR | Firewall blocked essential files. #78ee") # Bogus error.
     print()
     time.sleep(2)

# Once GUI is closed delete TEMP folder, and all contents.
try:
     shutil.rmtree(FULL_PATH)
except:
     pass

# Exit program.
print(Fore.WHITE + str(PREFETCH) + Fore.RED + "Exiting...")
time.sleep(2)
