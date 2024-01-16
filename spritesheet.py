"""
This is a seperate py file that is meant to take a sprite sheet and create a class for it that allows us to use it in other programs to create 
sprite sheets
"""

import pygame

class SpriteSheet():
	def __init__(self,image):
		self.sheet = image

	def get_image(self, frame, width,height,scale, color):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet,(0,0),((frame * width),0,width,height)) #this takes a part of the sprite sheet which is identified by the third argument of blit here and pastes it onto the image that we created which is just a black box
		image = pygame.transform.scale(image, (width * scale, height * scale)) #this takes the image and scales it up to a larger size 
		image.set_colorkey(color) #this sets whatever color we input to be transparent I think

		return image