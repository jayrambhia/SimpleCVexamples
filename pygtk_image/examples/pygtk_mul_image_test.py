"""
I am trying to use pygtk to show images instead of pygame.
Here I am trying to show multiple images at once.
"""
from SimpleCV import *
from pygtk_image import *

d1 = DisplayImage()
d2 = DisplayImage()
i1 = Image("lenna")
while not (d1.isDone() or d2.isDone()):
    try:
        d1.show_image(i1.toRGB().getBitmap())
        time.sleep(0.1)
        d2.show_image(i1.toGray().getBitmap())
        time.sleep(0.1)
    except KeyboardInterrupt:
        d1.quit()
        d2.quit()
