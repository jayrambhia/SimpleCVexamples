"""
I am trying to use pygtk instead of pygame.
This is an example which uses pygtk to show video (image frames).
"""
from SimpleCV import *
from pygtk_image import *

cam = Camera()
d = DisplayImage()
while not d.isDone():
    try:
        i = cam.getImage()
        i.drawRectangle(d.mouseX,d.mouseY,50,50,width=5)
        d.show_image(i.applyLayers().toRGB().getBitmap())
        time.sleep(0.1)
    except KeyboardInterrupt:
        d.quit()
        break
