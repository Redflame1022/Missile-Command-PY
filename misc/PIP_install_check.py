import os
import time
import turtle as t
text = t.Turtle()
text.hideturtle()
clear = lambda: os.system('cls')
kbinst = lambda: os.system('pip install keyboard')
checkkbvs = lambda: os.system('')
def instcheck():
    text.write('Loading...')
    clear()
    print('Attempting to use PIP to install module Keyboard, please restart your VSCode once after this just to be safe.')
    print('If the code will not run due to an error with keyboard please install it manually using pip install keyboard')
    print('Continuing in 2 seconds')
    time.sleep(2)
    kbinst()
    print('Keyboard module (hopefully) installed, startup continuing.')
    text.clear()