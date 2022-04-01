"""This is what the program does:
1. Gets a street address from the command line arguments or clipboard
2. Opens the web browser to the Google Maps page for the address

This means the code will need to do the following:

1. Read the command line arguments from the sys.argv.
2. Read the clipboard contents 
3. Call the webbrowser.open() function to open the web browser.
"""
#mapIt.py - Launches a map in the browser using an address 
#from the command line or clipboard 

#STEP 1: Figure Out the URL
"""Enter the following into the command line:
C:\> mapit 870 Valencia St, San Francisco, CA 94110
"""

#STEP 2: Handle the command line arguments
import webbrowser, sys, pyperclip  
if len(sys.argv) > 1:
    # Get address from the command line.
    address = ' '.join(sys.argv[1:]) 
    
    
    
# STEP 3: Handle the clipboard Content and Launch the Browser
else:
    #TODO: Get address from the clipboard
    address = pyperclip.paste() 

webbrowser.open('https://www.google.com/maps/place/' + address)
    