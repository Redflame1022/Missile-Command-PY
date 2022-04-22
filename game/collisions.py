from game.movement import aimer
from config import collisiondistance
def collision(target):
    return abs(target.xcor() - aimer.xcor()) < collisiondistance and abs(target.ycor() - aimer.ycor()) < collisiondistance