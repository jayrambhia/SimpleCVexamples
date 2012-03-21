from SimpleCV import *
"""
Applying Gaussian filter for DFT
Instead of iterating over whole big(512x512) image, and making a gaussian
filter, here we are making a gaussian filter of 64x64 and resizing it to fit 
the image to increase speed during run time. And then applying DFT on image.
"""
def applyGaussianfilter(im, dia=400, highpass=False, grayscale=True):
    """
        PARAMETERS:
    im: Image on which gaussian filter has to be applied
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
    
    img = applyGaussianfilter(im, dia=400,highpass=False,grayscale=False)
    
    im = Image("grayscale_lenn.png") #take image from here: http://i.imgur.com/O0gZn.png
    img = applyGaussianfilter(im, dia=400,highpass=True,grayscale=True)
    
    img = applyGaussianfilter(im, dia=400,highpass=False,grayscale=True)
    """
    w,h = im.size()
    flt = cv.CreateImage((64,64),cv.IPL_DEPTH_8U,1)
    dia = int(dia/((w/64.0+h/64.0)/2.0))
    if highpass:
        for i in range(64):
            for j in range(64):
                d = sqrt((j-32)**2+(i-32)**2)
                val = 255-(255.0*math.exp(-(d**2)/((dia**2)*2)))
                flt[i,j]=val
    else:
        for i in range(64):
            for j in range(64):
                d = sqrt((j-32)**2+(i-32)**2)
                val = 255.0*math.exp(-(d**2)/((dia**2)*2))
                flt[i,j]=val        
                
    flt = Image(flt)
    img = im.applyDFTFilter(flt,grayscale)
    return img
    
if __name__ == "__main__":
    im = Image("lenna")
    img = applyGaussianfilter(im,dia=10,highpass=False,grayscale=False)
    img.show()
