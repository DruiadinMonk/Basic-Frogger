# Frog class to create a Frog object.



# MODULES
import pygame



# LOG CLASS
class Frog:


	# INITIALIZE
	def __init__(self, window, color, x, y, radius):
		self.window = window
		self.color = color
		self.x = x
		self.y = y
		self.radius = radius


	# DRAW FROG
	def drawFrog(self):
		pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)
