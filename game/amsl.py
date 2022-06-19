import turtle as t
import time
from game.movement import aimer
from game.collisions import collision
from game.enemy_msl_bhv import emsllst
from game.enemy_msl_bhv import bhv
from ui.cornerdisplay import levelup, updcornerdisplay
from config import score, tracerdef, scoreperehit, debug
from ui.leaderboard import updleaderboard
wn = t.Screen()
wn.addshape('./Missile-Command-PY/images/Explosion/Boom_1.gif')
wn.addshape('./Missile-Command-PY/images/Explosion/Boom_2.gif')
wn.addshape('./Missile-Command-PY/images/Explosion/Boom_3.gif')
wn.addshape('./Missile-Command-PY/images/Explosion/Boom_4.gif')
def amsl_hit():
        amsl_hit = t.Turtle()
        def aexplosion():
                amsl_hit.color('white')
                aimer.hideturtle()
                amsl_hit.showturtle()
                amsl_hit.sety(amsl_hit.ycor()-25)
                amsl_hit.down()
                amsl_hit.circle(25)
                amsl_hit.up()
                amsl_hit.sety(amsl_hit.ycor()+25)
                amsl_hit.shape('./Missile-Command-PY/images/Explosion/Boom_1.gif')
                time.sleep(.2)
                amsl_hit.shape('./Missile-Command-PY/images/Explosion/Boom_3.gif')
                time.sleep(.2)
                amsl_hit.shape('./Missile-Command-PY/images/Explosion/Boom_4.gif')
                time.sleep(.2)
                amsl_hit.hideturtle()
                aimer.showturtle()
        t.tracer(tracerdef+1,0)
        t.colormode(255)
        fireline = t.Turtle()
        fireline.goto(-10,-170)
        fireline.hideturtle()
        fireline.speed(0)
        fireline.color('white')
        amsl_hit.speed(0)
        amsl_hit.up()
        amsl_hit.hideturtle()
        axcor = aimer.xcor()
        aycor = aimer.ycor()
        amsl_hit.goto(axcor,aycor)
        fireline.goto(axcor,(aycor-25))
        aexplosion()
        for i in emsllst:
                if collision(i):
                        wn.title('Hit!')
        for i in emsllst:
                if collision(i):
                        global score
                        bhv(i)
                        score+=scoreperehit
                        levelup()
                        updleaderboard(score)
                        if(debug==True):
                                print('Hit')
                        else:
                                pass
                else:
                        if(debug==True):
                                print('Miss')
                        else:
                                pass
        time.sleep(0.1)
        fireline.goto(-10,-170)
        fireline.clear()
        amsl_hit.clear()
        updcornerdisplay()
        t.tracer(tracerdef,0)
        wn.title('Missile Command')