# Ground class to create top and bottom Ground objects.



# MODULES
import pygame



# LOG CLASS
class Ground:


	# INITIALIZE
	def __init__(self, window, color, x, y, w, h):
		self.window = window
		self.color = color
		self.x = x
		self.y = y
		self.w = w
		self.h = h


	# DRAW FROG
	def drawGround(self):
		pygame.draw.rect(self.window, self.color, (self.x, self.y, self.w, self.h))
