"""
Frogger Game
By: Druiadin Monk

Create a frog object
5 rows of logs
Each log in each row is differently spaced for each row.
	
	-   -   -
	-  -  -  -
      -    -  
    - - - - - 
	    -     

End log at the top
Start log at bottom.
Grab red 'apple' at top, before you can return.

Once complete: "YOU WIN!" message.

"""



# MODULES
import pygame
import random 			# For direction of logs
from frog import Frog
from log import Log
from apple import Apple
from ground import Ground


# INITIALIZE
pygame.init() 											# Initialize 'pygame'.
WIN_X, WIN_Y = 400, 600 								# Set window (x, y).
window = pygame.display.set_mode((WIN_X, WIN_Y)) 		# Create window.
pygame.display.set_caption("Frogger") 					# Title of window.
font = pygame.font.Font('freesansbold.ttf', 32) 		# Properties of Font.
clock = pygame.time.Clock()
run = True 			# Main loop
FPS = 60 			# Speed of game.



# COLORS
WHITE   = (255, 255, 255)
BLACK   = (  0,   0,   0)
RED     = (255,   0,   0)
GREEN_1 = (  0, 222,   0)
GREEN_2 = (  0, 126,   0)
BROWN   = (140,  64,   0)
BLUE    = (  0,  53, 159)



# INITIALIZE OBJECTS: From top to bottom.

"""
	7 lists, 7 rows.
	odd rows move right, even move left.

Two options:

	1st
			Enough logs on each row, spaced apart on screen.
			Once log object off screen, reset the 'x', to be off screen to the left and continues moving right.

	2nd
			Have logs on each row bounce off walls.

"""


logs = []
# LOGS
for i in range(7):
	r_x = random.randint(0, 300)
	if i % 2 == 0: 	# If odd row, b/c i = 0 first.
		r_vel = random.randint(1, 4)
	else: 
		r_vel = random.randint(-4, -1)
	log = Log(window, BROWN, r_x, (i+1) * 65, 100, 50, r_vel)
	logs.append(log)


top = Ground(window, GREEN_2, 0, 0, 400, 50)
apple = Apple(window, RED, 200, 25, 5)
frog = Frog(window, GREEN_1, 200, 550, 15)
bot = Ground(window, GREEN_2, 0, 525, 400, 600)



# log_row_1 = []
# log_row_2 = []
# log_row_3 = []
# log_row_4 = []
# log_row_5 = []



"""
Log list 1-5 will randomizein y position.
	speed (velocity)
	and starting position on each row.

OR randomize 

	_____

	---->
	<----
	---->
	<----
	---->
	_____


"""




# MAIN LOOP
while run:


	# INITIALIZE
	clock.tick(FPS) 					# Speed of game.
	window.fill(BLUE) 				# BACKGROUND: Blue (Water)
	keys = pygame.key.get_pressed() 	# Frog Movement


	# EACH EVENT
	for event in pygame.event.get():

		# IF QUIT...
		if event.type == pygame.QUIT:
			run = False


	# DRAW OBJECTS

	# Log Objects
	for i in range(len(logs)):
		logs[i].moveLog()
		logs[i].drawLog()


	# Other Objects
	top.drawGround()
	apple.drawApple()
	bot.drawGround()
	frog.drawFrog()



	# MOVE OBJECTS



	# What ever the closest 'Y' object is...
	# 	if in between the 'x' (left and right side of log),
	# 		then 'JUMP' moves Frog to valid log.

	# When jump to new log or ground,
	# 	place frog on log where it jumped to. ('x' +/- radius of frog on log.)
	# 	Do NOT place in middle of log or ground.



	# UPDATE
	pygame.display.update()

# END LOOP



# If Main Loop == False
pygame.quit()
