'''
Author: Jay Rambhia
Credits: SimpleCV library
'''
"""
Apply of butterworth highpass/lowpass filter.
"""
from SimpleCV import *

def applyButterworth(im,dia=400,order=2,highpass=False,grayscale=True):
    """
        PARAMETERS:
    im: Image on which butterworth filter has to be applied
    dia: int
        Diameter of Butterworth low pass filter
    order: int 
        Order of butterworth lowpass filter
    highpass: BOOL
        True: highpass filter
        False: lowpass filter
    grayscale: BOOL
    
    Examples:
    
    im = Image("lenna")
    img = applyButterworth(im, dia=400,order=2,highpass=True,grayscale=False)
    Output image: http://i.imgur.com/5LS3e.png
    
    img = applyButterworth(im, dia=400,order=2,highpass=False,grayscale=False)
    Output img: http://i.imgur.com/QlCAY.png
    
    im = Image("grayscale_lenn.png") #take image from here: http://i.imgur.com/O0gZn.png
    img = applyButterworth(im, dia=400,order=2,highpass=True,grayscale=True)
    Output img: http://i.imgur.com/BYYnp.png
    
    img = applyButterworth(im, dia=400,order=2,highpass=False,grayscale=True)
    Output img: http://i.imgur.com/BYYnp.png
    """
    r,c = im.size()
    flt = cv.CreateImage((r,c),cv.IPL_DEPTH_8U,1)
    if highpass:
        for i in range(c):
            for j in range(r):
                d = sqrt((j-int(r/2))**2+(i-int(c/2))**2)
                flt[i,j] = 255-(255/(1+(d/dia)**(order*2)))
    else:
        for i in range(c):
            for j in range(r):
                d = sqrt((j-int(r/2))**2+(i-int(c/2))**2)
                flt[i,j] = 255/(1+(d/dia)**(order*2))
    
    flt = Image(flt)
    img = im.applyDFTFilter(flt,grayscale)
    return img
    
if __name__ == "__main__":
    im = Image("lenna")
    img = applyButterworth(im,highpass=False,grayscale=False)
    img.show()
    
