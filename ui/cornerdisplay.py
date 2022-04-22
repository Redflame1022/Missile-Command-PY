import turtle as t
import math
from config import level, baseline, debug
from game.enemy_msl_bhv import levelappend
ui = t.Turtle()
ui.color('white')
ui.up()
ui.hideturtle()
ui.speed(0)
def updcornerdisplay():
    from game.amsl import score
    from game.boundries import hp
    ui.clear()
    ui.goto(-250,200)
    ui.write('P  '+str(score))
    ui.sety(190)
    ui.write('L  '+str(level))
    ui.sety(180)
    ui.write("H  "+str(hp))
    ui.goto(-60,180)
    ui.write("Next level at "+str(baseline)+" points.")
def levelup():
    from game.amsl import score
    from config import baselineformula
    global baseline
    if(score>=baseline):
        global level
        level+=1
        baseline*=baselineformula
        baseline=math.ceil(baseline)
        levelappend()
        if debug == True:
            print('Level / Baseline per levelup '+str(level)+' ' +str(baseline))