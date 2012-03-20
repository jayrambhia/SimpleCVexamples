from SimpleCV import *

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
    img = applyButterworth(im, dia=400,highpass=True,grayscale=False)
    Output image: http://i.imgur.com/DttJv.png
    
    img = applyButterworth(im, dia=400,highpass=False,grayscale=False)
    Output img: http://i.imgur.com/PWn4o.png
    
    im = Image("grayscale_lenn.png") #take image from here: http://i.imgur.com/O0gZn.png
    img = applyButterworth(im, dia=400,highpass=True,grayscale=True)
    Output img: http://i.imgur.com/9hX5J.png
    
    img = applyButterworth(im, dia=400,highpass=False,grayscale=True)
    Output img: http://i.imgur.com/MXI5T.png
    """
    r,c = im.size()
    flt = cv.CreateImage((r,c),cv.IPL_DEPTH_8U,1)
    if highpass:
        for i in range(c):
            for j in range(r):
                d = sqrt((j-int(r/2))**2+(i-int(c/2))**2)
                val = 255-(255.0*math.exp(-(d**2)/((dia**2)*2)))
                flt[i,j]=val
    else:
        for i in range(c):
            for j in range(r):
                d = sqrt((j-int(r/2))**2+(i-int(c/2))**2)
                val = 255.0*math.exp(-(d**2)/((dia**2)*2))
                flt[i,j]=val        
                
    flt = Image(flt)
    img = im.applyDFTFilter(flt,grayscale)
    return img
    
if __name__ == "__main__":
    im = Image("lenna")
    img = applyGaussianfilter(im,highpass=False,grayscale=False)
    img.show()
