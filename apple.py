# Apple class to create Apple object for Frog to eat.



# MODULES
import pygame



# LOG CLASS
class Apple:


	# INITIALIZE
	def __init__(self, window, color, x, y, radius):
		self.window = window
		self.color = color
		self.x = x
		self.y = y
		self.radius = radius


	# DRAW FROG
	def drawApple(self):
		pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)
