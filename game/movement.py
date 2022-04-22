import turtle as t
from config import aimermovedef
global aimer 
aimer = t.Turtle()
wn = t.Screen()
aimer.color('white')
aimer.left(90)
aimer.up()
def u():
    aimer.sety(aimer.ycor()+aimermovedef)
def d():
    aimer.sety(aimer.ycor()-aimermovedef)
def l():
    aimer.setx(aimer.xcor()-aimermovedef)
def r():
    aimer.setx(aimer.xcor()+aimermovedef)