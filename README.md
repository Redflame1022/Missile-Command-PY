Missile Command for Python
==========================
By Redflame1022

This is a Missile Command (ish) clone, this file will basically say my process in designing it and where to find certain stuff.

Check the config.py for some basic configurable settings and debug stuff.

*I am fairly new to Python so dont expect it to be the most efficient thing ever.*

--------------------------------------------------------------------------------------------------------------------------

**IMPORTANT:**

In the files for this please go to misc/fonts/ and double click SpaceMission and click install. Run the code once and when it gets to the info screen close VScode and re open it, this is to make sure that keyboard installs correctly aswell as the font.

--------------------------------------------------------------------------------------------------------------------------

The game itself:

So basically the game has gone through a lot of revisions and rewrites entirely. Simply because of Python's limitations when it comes to Turtle Graphics.
However it has also allowed me to make it a lot more organized.

The game is seperated into 4 main folders being game, images, misc, ui.

The game folder contains most of the actual in game functionality. Including the collisions and main stack of stuff.  
The images folder contains all of the graphics loaded into the game.  
The misc folder contains stuff that doesn't really fit into any category, like fonts. 
The ui folder contains everything to do with ui, including the start screen and most of the stuff to do with layered visuals. 
Anything not in these folders is labeled 'outside'  


If you get any errors related to PIP or Keyboard you can install them manually. 
If you get an error about keyboard, run "PIP install Keyboard" in console.  


General descripton of each file:


game/:

amsl.py - Checks collision with enemy missiles, keeps track of score and levels. Also updates corner display.   
boundries.py - Checks if aimer or enemymsl goes out of bounds, resets the enemy missile if true and pushes the aimer if true. Also detects if the enemymsl's have gone below y-170, in which case it updates HP and corner display. 

collisions.py - Function for checking weather the enemymsl is within range of the amsl explosion. 
enemy_msl_bhv.py - Dictates the behavior for the msl's with the bhv() function. Also is responsible for adding new turtles based on level. Contains the function to move turtles down and a stop function.  

movement.py - Deals with the movement of the aimer. 


images/:  

land.gif - Land image   
Sphider'ly.gif - AAAAAAAAAAAAAAAAAAAAAAAA 


images/Cities/: 

Contains the 6 cities and their 3 states each.  


images/Explosion/:  

Contains animation frames for the explosion animation.  


misc/:  

PIP_install_check.py - Attempts to install the Keyboard module onto a users device, and gives instructions if something goes wrong. Also clears console.  


misc/fonts/:

SpaceMission-rgyw9.otf - File containing the special font for the startscreen and gameover screen.


ui/:

cornerdisplay.py - Is responsible for the information on the top left of the screen, contains info for HP, level, and points. Also contains information for baseline. Is responsible for keeping track of levelups.

gameover.py - Responsible for stopping everything and displaying the game over message. 
HS.txt - Score container for leaderboard  
leaderboard.py - Responsible for loading and updating leaderboad  
startscreen.py - Responsible for displaying the startscreen information and graphics. 


ui/imgload/:

Cities.py - Functions for loading and placing the cities. 
DeathSphider.py - Function for loading the endscreen death sphider. 
land.py - Function for loading in the background image. 


outside:

config.py - Responsible for basic configuration of code aswell as debug vrs.  
run.py - Compiles and runs all functions, contains main game loop.  
