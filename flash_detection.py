from SimpleCV import *
from SimpleCV.Display import Display 
import xaut

mouse = xaut.mouse()
mouse.move_delay(0)

disp = Display(resolution=(640,480))
cam = Camera()

while not disp.isDone():
	original_img = cam.getImage().flipHorizontal()
	img = original_img.colorDistance(color=Color.BLACK)
	bin = img.threshold(253).invert()
	bin.save(disp)
	if disp.mouseLeft:
		disp.done = True
		xaut.cleanup()