#! /usr/bin/python
import os
import pygame, sys, time

from pygame.locals import *
import pygame.camera

width = 640
height = 480

basedir = "/home/rock/pics"

def initCamera():
	pygame.init()
	pygame.camera.init()
	cam = pygame.camera.Camera("/dev/video0", (width, height))
	cam.start()
	return cam

def getDirName():
	theDate = getDateTimeString("%Y%m%d")
	directory = basedir + "/" + theDate
	if not os.path.exists(directory):
		os.makedirs(directory)
	return directory

def getTime():
	theTime = getDateTimeString("%H%M%S")
	return theTime

def getDateTimeString(formatString):
	return time.strftime(formatString)

cam = initCamera()

i = 0
while True:
	image = cam.get_image()
	cam.stop
	filename = getDirName() + "/" + getTime() + str(i) + ".jpg"
	print 'SNAP (' + filename + ').'
	pygame.image.save(image, filename)
	time.sleep(3)
	i += 1

