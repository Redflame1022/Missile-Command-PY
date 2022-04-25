#This is a script created by Redflame1022 to clone Missile Command. Please head over to the INFO.md file for more information.

#Imports
import turtle as t
from misc.PIP_install_check import instcheck
from ui.imgload.Cities import regcity, positioncities
from ui.startscreen import startscreen, cleartxt
from ui.imgload.land import landimg
from game.movement import u, d, l, r
from game.enemy_msl_bhv import bhv, emsllst, godown
from game.amsl import amsl_hit
from game.boundries import boundries
from ui.cornerdisplay import updcornerdisplay, level
from ui.gameover import gameover
from ui.leaderboard import checkscore, currenths
from config import defaultgodownrate, tracerdef, grun
global wn
wn = t.Screen()
#Functions and main loop
wn.title('Loading...')
instcheck()
checkscore()
currenths()
import keyboard
startscreen()
keyboard.wait('Space')
wn.title('Missile Command')
cleartxt()
landimg()
regcity()
positioncities()
wn.onkeypress(u, 'Up')
wn.onkeypress(d, 'Down')
wn.onkeypress(l, 'Left')
wn.onkeypress(r, 'Right')
wn.onkeypress(amsl_hit, 'space')
updcornerdisplay()
for i in emsllst:
    bhv(i)
amsl_hit()
while(grun == True):
    from game.boundries import hp
    t.tracer(int(tracerdef),0)
    for i in emsllst:
        godown(i, defaultgodownrate*level+.15)
        boundries(i)
    if(hp<=0):
        gameover()
    wn.listen()
    t.update()