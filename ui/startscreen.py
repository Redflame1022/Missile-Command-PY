import turtle as t
from config import version
wn = t.Screen()
def newinfo(y, txt):
    text.sety(text.ycor()-y)
    text.stamp()
    text.setx(text.xcor()+8)
    text.sety(text.ycor()+8)
    text.write(txt)
    text.setx(text.xcor()-8)
    text.sety(text.ycor()-8)

def startscreen():
    from ui.leaderboard import hscr
    wn.title('Start screen')
    global text
    text = t.Turtle()
    text.speed(0)
    text.up()
    text.goto(-60,200)
    text.write('Missile Command', font=('SpaceMission',30,'normal'))
    text.sety(180)
    text.write('By Redflame1022')
    text.sety(120)
    text.write('Previous High Score: '+str(hscr), font=('SpaceMission',18,'normal'))
    text.goto(-325,100)
    newinfo(0, 'General Information:')
    newinfo(15, 'Missile Command is a game where you fire at missiles rained down on you.')
    newinfo(15, 'Your cities have a total of 2 health each, with 6 cities that is 12 health in total.')
    newinfo(15, 'Any time a missile reaches the ground that will count as a hit, and a city will take 1 point of damage.')
    newinfo(15, 'You move your aimer with the arrow keys, currently only up, down, left, right is supported.')
    newinfo(15, 'Each missile shot down is worth 100 points.')
    newinfo(15, 'Each time an enemy missile hits you it is -100 points.')
    newinfo(15, 'Each city destroyed is -350 points')
    newinfo(15, 'Each level increase is x2 of the previous requirement.')
    newinfo(15, 'Every two levels you will get +1 missiles until there are 10 missiles, each level will have the missiles slightly increase in speed.')
    newinfo(15, 'As more missiles appear, when the missiles get closer to the bottom the game will slow down slightly to let you catch up.')
    text.goto(-325,-150)
    newinfo(0, 'Controls:')
    newinfo(15, 'Use your arrow keys to control the aimer')
    newinfo(15, 'Strafing is currently not supported.')
    newinfo(15, 'Press Space to fire.')
    text.goto(-60,-250)
    text.write(version)
    text.goto(-60,-200)
    text.write('Space to continue', font=('SpaceMission',18,'normal'))

def cleartxt():
    text.clear()
    text.hideturtle()
    text.goto(1000,1000)
