from SimpleCV import *
from pygtk_image import *
from threading import Thread

def loadimage():
    image = Image("lenna")
    d = DisplayImage()
    print "Display"
    d.show_image(image.toRGB().getBitmap())
    print "threaded"
    time.sleep(3)
    d.show_image(Image("simplecv").toRGB().getBitmap())
    
def thread_gtk():
    Thread(target=start_gtk).start()
    
def start_gtk():
    gtk.main()
    

if __name__ == "__main__":
    loadimage()
