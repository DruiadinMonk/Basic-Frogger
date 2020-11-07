# Log class to create a Log object.



# MODULES
import pygame



# LOG CLASS
class Log:


	# INITIALIZE
	def __init__(self, window, color, x, y, w, h, vel):
		self.window = window
		self.color = color
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.vel = vel 		# Logs move either left or right 'velocity' speed.


	# DRAW FROG
	def drawLog(self):
		pygame.draw.rect(self.window, self.color, (self.x, self.y, self.w, self.h))

	# MOVE LOG
	def moveLog(self):
		# Move log
		self.x += self.vel

		# If log hits wall...
		if self.x <= 0 or self.x >= 300:

			# Shift direction.
			self.vel *= -1
