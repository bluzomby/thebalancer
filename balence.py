#!/usr/bin/env python
import math
import os
import sys
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1200, 800)) # set the screen to be a 480p windowed screen
# set up some time stuff 
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 60 # pcmr
deltat = clock.tick(FRAMES_PER_SECOND) 