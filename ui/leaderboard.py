import os
from config import debug
global hscr
def checkscore():
    with open("ui/HS.txt", "r") as fl:
        global hscr
        hscr = fl.read().replace('\n','')
        int(hscr)
        fl.close()
        if(debug == True):
            print('HS.txt opened and read.')
def updleaderboard(score):
    global hscr
    checkscore()
    if(int(score)>int(hscr)):
        os.remove('ui/HS.txt')
        with open('ui/HS.txt', 'xt') as fl:
            fl.write(str(score))
            fl.close()
            if(debug == True):
                print('HS.txt deleted and regenerated.')
def currenths():
    global hscr
    print('Previous High Score:')
    print(hscr) 