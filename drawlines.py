'''
Author: Jay Rambhia
email: jayrambhia777@gmail.com
irc nick: jayrambhia
blog: http://jayrambhia.wordpress.com
'''
"""
drawlines.
Draws lines on image joining two distinct point. Points are marked using mouse clicks.

Usage:
drawlines(img)

credits: SimpleCV library
"""
from SimpleCV import *

def drawlines(img):
    disp = Display()
    pt1 = None
    pt2 = None
    img.show()

    while disp.isNotDone():
        if disp.mouseLeft:
            if pt1 is None and pt2 is None:
                pt1 = pg.mouse.get_pos()    # get first point. point is a tuple of two integers.
            elif pt1:
                pt2 = pg.mouse.get_pos()    # get second point
            
            if pt1 is not None and pt2 is not None:
                if pt1 != pt2:
                    # if points are distinct
                    img.drawLine(pt1,pt2,thickness=2)   # draw the line joining both the points
                    img.show()
                    pt1= None  
                    pt2 = None

if __name__ == "__main__":
    #img = Image("the_beatles791.jpg")
    cam = Camera()
    img = cam.getImage()
    drawlines(img)
