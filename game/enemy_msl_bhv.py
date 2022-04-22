from operator import le
import turtle as t
import random as rd
global levelappendupd
from config import tracerdef, newmslincrrate, levelappendupd, debug
global emsllst
t.tracer(tracerdef,0)
emsl0 = t.Turtle()
emsl1 = t.Turtle()
emsl2 = t.Turtle()
emsl3 = t.Turtle()
emsl4 = t.Turtle()
emsl5 = t.Turtle()
emsl6 = t.Turtle()
emsl7 = t.Turtle()
emsl8 = t.Turtle()
emsl9 = t.Turtle()
emsllst = [emsl0]

def bhv(emsl):
    emsl.reset()
    t.tracer(tracerdef,0)
    emsl.speed(0)
    emsl.color('red')
    emsl.up()
    enemystartposx = rd.randint(-300,300)
    enemystartposy = 250
    emsl.goto(enemystartposx,enemystartposy)
    enemydir = rd.randint(-45,45)
    emsl.setheading(-90)
    emsl._rotate(enemydir)
    emsl.down()
    emsl.clear()
    emsl.speed(.1)
def levelappendfunct(lnum, msl, lupreq):
    global levelappendupd
    from ui.cornerdisplay import level
    if level==lnum*newmslincrrate and levelappendupd == lupreq:
        emsllst.append(msl)
        levelappendupd+=1
        bhv(msl)
        if debug == True:
            print(emsllst, levelappendupd)
    else:
        if debug == True:
            print(emsllst, levelappendupd)
        pass
def levelappend():
    levelappendfunct(1, emsl1, 0)
    levelappendfunct(2, emsl2, 1)
    levelappendfunct(3, emsl3, 2)
    levelappendfunct(4, emsl4, 3)
    levelappendfunct(5, emsl5, 4)
    levelappendfunct(6, emsl6, 5)
    levelappendfunct(7, emsl7, 6)
    levelappendfunct(8, emsl8, 7)
    levelappendfunct(9, emsl9, 8)
def godown(emsl, downspeed):
    t.tracer(tracerdef,0)
    emsl.forward(downspeed)

def stop(emsl):
    emsl.up()
    emsl.clear()
    emsl.shape('circle')
    emsl.turtlesize(5)