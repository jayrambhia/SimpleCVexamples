from SimpleCV import *

"""
Applying Gaussian filter for DFT
Instead of iterating over whole big(512x512) image, and making a gaussian
filter, here we are making a gaussian filter of 32x32 and resizing it to fit 
the image to increase speed during run time. And then applying DFT on image.
"""
def applyGaussianfilter(im, dia=400, highpass=False, grayscale=True):
    """
        PARAMETERS:
    im: Image on which unsharp masking/highboost filtering has to be done
    boost: int  
            boost = 1 => unsharp masking
            boost > 1 => highboost filtering
    dia: int
        Diameter of Gaussian filter
    highpass: BOOL
        True: highpass filter
        False: lowpass filter
    grayscale: BOOL
    
    Example:
    
    im = Image("lenna")
    img = applyGaussianfilter(im, dia=400,highpass=True,grayscale=False)
    Output image: http://i.imgur.com/DttJv.png
    
    img = applyGaussianfilter(im, dia=400,highpass=False,grayscale=False)
    Output img: http://i.imgur.com/PWn4o.png
    
    im = Image("grayscale_lenn.png") #take image from here: http://i.imgur.com/O0gZn.png
    img = applyGaussianfilter(im, dia=400,highpass=True,grayscale=True)
    Output img: http://i.imgur.com/9hX5J.png
    
    img = applyGaussianfilter(im, dia=400,highpass=False,grayscale=True)
    Output img: http://i.imgur.com/MXI5T.png
    """
    w,h = im.size()
    flt = cv.CreateImage((32,32),cv.IPL_DEPTH_8U,1)
    dia = int(dia/((w/32.0+h/32.0)/2.0))
    if highpass:
        for i in range(32):
            for j in range(32):
                d = sqrt((j-16)**2+(i-16)**2)
                val = 255-(255.0*math.exp(-(d**2)/((dia**2)*2)))
                flt[i,j]=val
    else:
        for i in range(32):
            for j in range(32):
                d = sqrt((j-16)**2+(i-16)**2)
                val = 255.0*math.exp(-(d**2)/((dia**2)*2))
                flt[i,j]=val        
                
    flt = Image(flt)
    img = im.applyDFTFilter(flt,grayscale)
    return img
    
if __name__ == "__main__":
    im = Image("lenna")
    img = applyGaussianfilter(im,dia=10,highpass=False,grayscale=False)
    img.show()
