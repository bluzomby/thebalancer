#!/usr/bin/env python
import math, os, sys, pygame
from pygame.locals import *
# General window intializing stuff
pygame.init()
# set the background color
background_color = (255,255,255) # white
screen = pygame.display.set_mode((1280, 720)) # set the screen to be a 720p windowed screen
pygame.display.set_caption('The Balancer') 
screen.fill(background_color)
# set up some time stuff 
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 60 # pcmr
deltat = clock.tick(FRAMES_PER_SECOND)
# load images here
pygame.display.flip()
# make sure the window doesn't close immediately by creating an infine loop
running = True
while running:
	for event in pygame.event.get(): # make it so the window closes if the "X" is pressed
		if event.type == pygame.QUIT:
			running = False