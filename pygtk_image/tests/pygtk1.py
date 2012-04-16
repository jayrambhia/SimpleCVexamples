"""
This is an example of how to show images using pygtk.
I am trying to use pygtk to show images instead of pygame. I will add
other functionalities for video, mouse callback, etc.
And most importantly loading images. And if possible multiple windows.
"""
import gtk
from SimpleCV import *
import sys
class MainWindow():
    def __init__(self,image,mode="RGB"):
        print mode
        self.filename = image.filename.split("/")[-1].split(".")[0]
        if mode == "RGB":
            new_image = image.toRGB()   # iplimages have BGR colorspace. But gtk pixbuf has colorspace RGB.
        elif mode == "gray":
            print "gray"
            new_image = image.toGray()
        elif mode == "BGR":
            pass
        elif mode == "HSV":
            new_image = image.toHSV()
        elif mode == "HLS":
            new_image = image.toHLS()
        elif mode == "XYZ":
            new_image = image.toXYZ()
        else:
            print "Unknown colorspace"
            print "converting to RGB"
            new_image = image.toRGB()   # iplimages have BGR colorspace. But gtk pixbuf has colorspace RGB.
            
        self.img = new_image.getBitmap()
        self.win = gtk.Window()
        self.win.set_size_request(self.img.width,self.img.height)
        self.win.connect("delete_event",self.leave_app)
        self.win.set_title(self.filename)
        # As of now only gtk.gdk.COLORSPACE_RGB is available.
        self.img_pixbuf = gtk.gdk.pixbuf_new_from_data(self.img.tostring(),gtk.gdk.COLORSPACE_RGB,False,self.img.depth,self.img.width,self.img.height,self.img.width*self.img.nChannels)
        self.image = gtk.image_new_from_pixbuf(self.img_pixbuf)
        self.win.add(self.image)
        self.win.show_all()
        
    def leave_app(self,widget,event):
        self.win.destroy()
        gtk.main_quit()
        
if __name__ == "__main__":
    try:
        mode = sys.argv[2]
    except IndexError:
        print "Default mode RGB"
        mode="RGB"
    print sys.argv[1],mode
    image = Image(sys.argv[1],mode)
    MainWindow(image)
    gtk.main()
