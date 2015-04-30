#!/usr/bin/env python
import math, os, sys, pygame, inputbox
# using the library pygame (http://pygame.org) to handle most things and inputbox (http://www.pygame.org/pcr/inputbox/) to handle text easily 
from pygame.locals import *

# define some colors
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)

# Set score/game related variables 
myscore = 0
mylives = 3
running = True
instructions = False
game = False
# set screen size
screen = pygame.display.set_mode((1280, 720)) # set the screen to be a 720p windowed screen
# ask the user their name before launching into the main program 
myname = int(inputbox.ask(screen, 'Type your name and then press enter: '))

# Load images
background = pygame.image.load('background.bmp')
instruction_image = pygame.image.load('instructions.bmp')
plate1 = pygame.image.load('plates.bmp')
back1 = pygame.image.load('mainback1.bmp')
# load textboxes // all using inputbox 
myname = int(inputbox.ask(screen, 'Type your name and then press enter: '))
inp1 = int(inputbox.ask(screen, ''))
inp2 = int(inputbox.ask(screen, ''))
inp3 = int(inputbox.ask(screen, ''))

# General window intializing stuff
pygame.init()

# set up some time stuff 
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 60 # pcmr // the game will run at 60fps
deltat = clock.tick(FRAMES_PER_SECOND)
pygame.display.flip() # idk why I have to do this but the code won't work without it, also needed after anytime an image loads 

###################################
###### Now the actual program #####
###################################

def main():
	screen.blit(myname, (0,0))
	pygame.display.flip()
	# Start screen, code used is here: http://stackoverflow.com/questions/20356307/how-would-i-add-a-start-screen-to-this-pygame-python-code
	screen.fill(black)
	end_it = False 
	while (end_it==False):
		screen.blit(background, [0, 0])
		myfont = pygame.font.SysFont('Seravek Light', 40) # Placeholder font, will find a better one once I get the whole color scheme of my game going
		nlabel = myfont.render('Welcome '+myname+', Click to start', 1, (white)) # The screen will print the user's name 
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN: # Program will move on to the next screen when the mouse is clicked
				screen.fill(black)
				instructions = True
				end_it = True
		screen.blit(nlabel,(450, 360))
		pygame.display.flip()
	
	# Instructions screen, using mostly the same code as the welcome screen 
	while (instructions == True):
		screen.fill(black)
		screen.blit(instruction_image, [0, 0])
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN: # Program will move on to the next screen when the mouse is clicked
				game = True
				instructions = False
				screen.fill(black)
		pygame.display.flip()
	
	while (game == True):
		screen.fill(white)
		screen.blit(inp1, (615, 320))
		str.inp1
		if inp1 == "1":
			correct1 = True 
		screen.blit(back1, (0,0))
		pygame.display.flip()
	
	while (running == True):
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT: # the window will close if the "x" on the window is pressed
					running = False # nothing can come after this in the code 

main()