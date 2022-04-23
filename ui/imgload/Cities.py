from images.Cities import *
import turtle as t
from config import hp, debug
starthealth = hp
wn = t.Screen()
City_L1T=t.Turtle()
City_L2T=t.Turtle()
City_L3T=t.Turtle()
City_R1T=t.Turtle()
City_R2T=t.Turtle()
City_R3T=t.Turtle()
Citygroupsdic = {'City_L1','City_L2','City_L3','City_R1','City_R2','City_R3'}
Citygroupslis = [City_L1T,City_L2T,City_L3T,City_R1T,City_R2T,City_R3T]
def regcity():
    for i in Citygroupsdic:
        wn.addshape('images/Cities/'+str(i)+'_1.gif')
        wn.addshape('images/Cities/'+str(i)+'_2.gif')
        wn.addshape('images/Cities/'+str(i)+'_3.gif')
        for x in Citygroupslis:
            x.up()
            x.clear()
            x.speed(0)
def position(t, x, y, n):
    t.shape('images/Cities/'+n+'_3.gif')
    t.goto(x,y)
def positioncities():
    position(City_L1T,-212,-190,'City_L1')
    position(City_L2T,-144,-187,'City_L2')
    position(City_L3T,-82, -193,'City_L3')
    position(City_R1T,50,-187,'City_R1')
    position(City_R2T,130,-185,'City_R2')
    position(City_R3T,205,-195,'City_R3')
    for x in Citygroupslis:
        x.clear()
        x.showturtle()
def cityupd(healtharg):
    def cupdfun(h, nm, c):
        if(healtharg==h):
            c.shape('images/Cities/City_'+nm+'.gif')
            if(debug == True):
                print(str(c)+' updated to images/Cities/City_'+nm+'.gif')
    cupdfun(11, 'L1_2',City_L1T)
    cupdfun(10, 'L1_1',City_L1T)
    cupdfun(9, 'L2_2',City_L2T)
    cupdfun(8, 'L2_1',City_L2T)
    cupdfun(7, 'L3_2',City_L3T)
    cupdfun(6, 'L3_1',City_L3T)
    cupdfun(5, 'R1_2',City_R1T)
    cupdfun(4, 'R1_1',City_R1T)
    cupdfun(3, 'R2_2',City_R2T)
    cupdfun(2, 'R2_1',City_R2T)
    cupdfun(1, 'R3_2',City_R3T)
    cupdfun(0, 'R3_1',City_R3T)