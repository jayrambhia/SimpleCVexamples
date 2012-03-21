'''
Author: Jay Rambhia
Credits: SimpleCV library
'''
"""
Apply of butterworth highpass/lowpass filter.
Instead of iterating over whole big(512x512) image, and making a butterworth
filter, here we are making a butterworthfilter of 64x64 and resizing it to fit 
the image to increase speed during run time. And then applying DFT on image.
"""
from SimpleCV import *

def applyButterworth(im,dia=400,order=2,highpass=False,grayscale=True):
    """
        PARAMETERS:
    im: Image on which unsharp masking/highboost filtering has to be done
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
    w,h = im.size()
    flt = cv.CreateImage((32,32),cv.IPL_DEPTH_8U,1)
    dia = int(dia/((w/32.0+h/32.0)/2.0))
    if highpass:
        for i in range(32):
            for j in range(32):
                d = sqrt((j-16)**2+(i-16)**2)
                flt[i,j] = 255-(255/(1+(d/dia)**(order*2)))
    else:
        for i in range(32):
            for j in range(32):
                d = sqrt((j-16)**2+(i-16)**2)
                flt[i,j] = 255/(1+(d/dia)**(order*2))
    
    flt = Image(flt)
    flt_re = flt.resize(w,h)
    img = im.applyDFTFilter(flt_re,grayscale)
    return img
    
if __name__ == "__main__":
    im = Image("lenna")
    img = applyButterworth(im,dia=400,order=1,highpass=True,grayscale=False)
    img.show()
