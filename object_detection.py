from SimpleCV import *
from SimpleCV.Display import Display 
import xaut
mouse = xaut.mouse()
delay = mouse.move_delay(0)
custom_red = (121.0, 41.0, 37.0)
disp = Display(resolution=(640,480))
white_img = Image((640,480)).invert()
YELLOW=(179.0, 195.0, 112.0)
cam = Camera()

while not disp.isDone():
	original_img = cam.getImage().flipHorizontal()
	red_distance_img = original_img.colorDistance(color=Color.RED)
	red_bin = red_distance_img.threshold(100).invert()
	blobs = red_bin.findBlobs(minsize=50,maxsize=10720)
	if(blobs is not None):
		blob = max(blobs)
		mouse.move(15*(blob.x-256),12.5*(blob.y-192))
	red_bin.save(disp)
	if disp.mouseLeft:
		disp.done = True
		xaut.cleanup()