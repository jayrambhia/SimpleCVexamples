'''
Author: Jay Rambhia
Credits: SimpleCV library
'''
"""
Apply butterworth highpass/lowpass filter.
Instead of iterating over whole big(512x512) image, and making a butterworth
filter, here we are making a butterworthfilter of 64x64 and resizing it to fit 
the image to increase speed during run time. And then applying DFT on image.
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
    img = applyButterworth(im, dia=240,order=2,highpass=True,grayscale=False)
    Output image: http://i.imgur.com/5LS3e.png
    
    img = applyButterworth(im, dia=240,order=2,highpass=False,grayscale=False)
    Output img: http://i.imgur.com/bG1l9.png
    
    """
    w,h = im.size()
    flt = cv.CreateImage((64,64),cv.IPL_DEPTH_8U,1)
    dia = int(dia/((w/64.0+h/64.0)/2.0))
    if highpass:
        for i in range(64):
            for j in range(64):
                d = sqrt((j-32)**2+(i-32)**2)
                flt[i,j] = 255-(255/(1+(d/dia)**(order*2)))
    else:
        for i in range(64):
            for j in range(64):
                d = sqrt((j-int(r/2))**2+(i-int(c/2))**2)
                flt[i,j] = 255/(1+(d/dia)**(order*2))
    
    flt = Image(flt)
    flt_re = flt.resize(w,h)
    img = im.applyDFTFilter(flt_re,grayscale)
    return img
    
if __name__ == "__main__":
    im = Image("lenna")
    img = applyButterworth(im,dia=400,order=1,highpass=True,grayscale=False)
    img.show()
