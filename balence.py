#!/usr/bin/env python
import math, os, sys, pygame, eztext
from pygame.locals import *
#ask the user their name before launching into the main program
myname = raw_input('What is your name? ')
# define some colors
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
# Set score/game related variables 
myscore = 0
mylives = 0
# Load images
background = pygame.image.load('background.bmp')
instruction_image = pygame.image.load('instructions.bmp')
# General window intializing stuff
pygame.init()
screen = pygame.display.set_mode((1280, 720)) # set the screen to be a 720p windowed screen
# set up some time stuff 
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 60 # pcmr
deltat = clock.tick(FRAMES_PER_SECOND)
# load images here
pygame.display.flip()
# Start screen, code used is here: http://stackoverflow.com/questions/20356307/how-would-i-add-a-start-screen-to-this-pygame-python-code
end_it = False 
while (end_it==False):
	screen.blit(background, [0, 0])
	myfont = pygame.font.SysFont('Seravek Light', 40) # Placeholder font, will find a better one once I get the whole color scheme of my game going
	nlabel = myfont.render('Welcome '+myname+', Click to start', 1, (white))
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN:
			end_it = True
			instructions = True
			screen.fill(white)
	screen.blit(nlabel,(450, 360))
	pygame.display.flip()
while (instructions == True):
	screen.blit(instruction_image, [0, 0])
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN:
			instructions = False
			screen.fill(white)
	pygame.display.flip()
running = True
while running:
	for event in pygame.event.get(): # make it so the window closes if the "X" is pressed
		if event.type == pygame.QUIT:
			running = False