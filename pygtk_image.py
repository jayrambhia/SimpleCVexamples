"""
Trying to use pygtk to show images instead of pygame. Giving some problems.
Need to work on threading. And add more functionality. I think I might replace
pygame with pygtk.
Created a small test for it. pygtk_image_test.py
"""
import gtk
from SimpleCV import *
from threading import Thread
import gobject
gtk.gdk.threads_init()

class DisplayImage():
    def __init__(self,title="SimpleCV"):
        self.img = None
        self.img_gtk = None
        self.mouseX=0
        self.mouseY=0
        self.win = gtk.Window()
        self.win.set_title(title)
        self.win.connect("delete_event",self.leave_app)
        self.image_box = gtk.EventBox()
        # Need to add more functionality here
        self.image_box.connect("button_press_event",self.press_callback)
        self.win.add(self.image_box)
        self.thread_gtk()           # thread for gtk.main() . Need to 
                                    # consider multiple images too.
    
    def leave_app(self,widget,event):
        gtk.main_quit()
    
    def show_image(self,image):
        self.img = image
        if self.img_gtk is None:
            self.img_flag=0
            self.img_gtk = gtk.Image()
        self.img_pixbuf = gtk.gdk.pixbuf_new_from_data(self.img.tostring(),gtk.gdk.COLORSPACE_RGB,False,self.img.depth,self.img.width,self.img.height,self.img.width*self.img.nChannels)
        self.img_gtk.set_from_pixbuf(self.img_pixbuf)
        if not self.img_flag:
            self.image_box.add(self.img_gtk)
            self.img_flag=1
        self.img_gtk.show()
        self.win.show_all()
        
    def thread_gtk(self):
        Thread(target=self.start_gtk).start()
        
    def start_gtk(self):
        gtk.main()
    
    def leave_app(self,widget,data):
        self.win.destroy()
        gtk.main_quit()
        
    def press_callback(self,widget,event):
        # I'll add more functionality here
        self.mouseX = int(event.x)
        self.mouseY = int(event.y)
        print self.mouseX, self.mouseY
        
