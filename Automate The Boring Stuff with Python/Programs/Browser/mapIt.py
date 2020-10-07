import pyperclip
import sys
import webbrowser

# Either provide the address to find in the command line while running, else copy the address to the clipboard and run the program.

sys.argv  # ['mapIt.py', '870', 'Valencia', 'St.']

if len(sys.argv) > 1:
    # ['mapIt.py', '870', 'Valencia', 'St.'] => '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.co.in/maps/place/<address>
webbrowser.open('https://www.google.co.in/maps/place/'+address)
