from SimpleCV import *
from SimpleCV.Display import Display 

cam = Camera()
disp = Display(resolution=(640,480))
face_cascade = HaarCascade("face.xml","Faces")

while not disp.isDone():
	original_img = cam.getImage().flipHorizontal()
	faces = original_img.findHaarFeatures(face_cascade)
	if (faces is not None):
		faces.draw()
		print faces.coordinates()
	original_img.save(disp)
	if disp.mouseLeft:
		disp.done = True
