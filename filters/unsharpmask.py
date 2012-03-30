from SimpleCV import *
from butterworthfilter import *
from gaussianfilter import *

def highboost(im,mask,boost=1):
    img = im
    for i in range(boost):
        img = img + mask
    return img
    
def applyUnsharpMask(im,boost=1,dia=400,order=2,grayscale=False):
    """
    PARAMETERS:
    im: Image on which unsharp masking/highboost filtering has to be done
    boost: int  
            boost = 1 => unsharp masking
            boost > 1 => highboost filtering
    dia: int
        Diameter of Gaussian/Butterworth low pass filter
    order: int 
        Order of butterworth lowpass filter
    grayscale: BOOL
    
    Examples: 
    ======================================================================
    Gaussian Filters:
    im = Image("lenna")
    img = applyUnsharpMask(im,2,grayscale=False) #highboost filtering
    output image: http://i.imgur.com/A1pZf.png
   
    img = applyUnsharpMask(im,1,grayscale=False) #unsharp masking
    output image: http://i.imgur.com/smCdL.png
    
    im = Image("grayscale_lenn.png") #take image from here: http://i.imgur.com/O0gZn.png
    img = applyUnsharpMask(im,2,grayscale=True) #highboost filtering
    output image: http://i.imgur.com/VtGzl.png
    
    img = applyUnsharpMask(im,1,grayscale=True) #unsharp masking
    output image: http://i.imgur.com/bywny.png
    ======================================================================
    Butterworth Filters:
    im = Image("lenna")
    img = applyUnsharpMask(im,1,dia=400,order=2,grayscale=False) # unsharp masking
    output image: http://i.imgur.com/jd0ka.png
    
    img = applyUnsharpMask(im,1,dia=400,order=2,grayscale=False) #highboost filtering
    output image: http://i.imgur.com/EyvTI.png
    
    im = Image("grayscale_lenn.png") #take image from here: http://i.imgur.com/O0gZn.png
    img = applyUnsharpMask(im,1,dia=400,order=2,grayscale=True) # unsharp masking
    output image: http://i.imgur.com/IR1rE.png
    
    img = applyUnsharpMask(im,1,dia=400,order=2,grayscale=True) #highboost filtering
    output image: http://i.imgur.com/IVxhI.png
    """
    if boost < 0:
        print "boost >= 1"
        return None
    #lpIm = applyButterworth(im,dia=400,order=1,grayscale=grayscale,highpass=False)
    # Need to add both using mapping!
    lpIm = applyGaussianfilter(im,dia=400,grayscale=grayscale,highpass=False)
    mask = im - lpIm
    img = highboost(im,mask,boost)
    return img
    
if __name__ == "__main__":
    im = Image("lenna")
    img = applyUnsharpMask(im,2,dia=400,grayscale=False)
    #img = applyUnsharpMask(im,2,dia=400,order=2,grayscale=False) #For Butterworth
    img.show()
