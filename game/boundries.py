from operator import ge
from game.movement import aimer
from game.enemy_msl_bhv import bhv
from ui.cornerdisplay import updcornerdisplay
from ui.imgload.Cities import cityupd
from config import hp
import turtle as t
import time
wn = t.Screen()
wn.addshape('images/Explosion/Boom_1.gif')
wn.addshape('images/Explosion/Boom_2.gif')
wn.addshape('images/Explosion/Boom_3.gif')
wn.addshape('images/Explosion/Boom_4.gif')
def boundries(target):
    def gexplosion(ex):
        t.tracer(1,0)
        gexpl = t.Turtle()
        gexpl.up()
        gexpl.goto(ex.xcor(),ex.ycor())
        gexpl.showturtle()
        gexpl.shape('images/Explosion/Boom_1.gif')
        time.sleep(.2)
        gexpl.shape('images/Explosion/Boom_2.gif')
        time.sleep(.2)
        gexpl.shape('images/Explosion/Boom_3.gif')
        time.sleep(.2)
        gexpl.shape('images/Explosion/Boom_4.gif')
        time.sleep(.2)
        gexpl.hideturtle()
        t.tracer(0,0)
    if(target.xcor()>= 320 or target.xcor()<= -320):
        bhv(target)
    elif(aimer.ycor()<=-170):
        aimer.sety(aimer.ycor()+10)
    elif(aimer.ycor()>=230):
        aimer.sety(aimer.ycor()-10)
    elif(aimer.xcor()>=320):
        aimer.setx(aimer.xcor()-10)
    elif(aimer.xcor()<=-320):
        aimer.setx(aimer.xcor()+10)
    elif(target.xcor()>= 320 or target.xcor()<= -320):
        bhv(target)
    elif(target.ycor()<=-170):
        global hp
        gexplosion(target)
        bhv(target)
        hp = hp-1
        updcornerdisplay()
        cityupd(hp)

        