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
        #print "Initialize"
        self.img = None
        self.img_gtk = None
        self.mouseX = 0
        self.mouseY = 0
        self.mouse_rawX = 0
        self.mouse_rawY = 0
        self.done = False
        self.thrd = None
        self.win = gtk.Window()
        self.win.set_title(title)
        self.win.connect("delete_event",self.leave_app)
        self.image_box = gtk.EventBox()
        self.image_box.connect("motion_notify_event",self.motion_callback)
        self.image_box.connect("button_press_event",self.press_callback)
        self.win.add(self.image_box)
        #self.thread_gtk()           # thread for gtk.main() . Need to 
                                    # consider multiple images too.
    
    def show_image(self,image):
        self.img = image
        if self.img_gtk is None:
            self.img_flag=0
            self.img_gtk = gtk.Image()          # Create gtk.Image() only once (first time)
        self.img_pixbuf = gtk.gdk.pixbuf_new_from_data(self.img.tostring(),
                                                        gtk.gdk.COLORSPACE_RGB,
                                                        False,
                                                        self.img.depth,
                                                        self.img.width,
                                                        self.img.height,
                                                        self.img.width*self.img.nChannels)
        self.img_gtk.set_from_pixbuf(self.img_pixbuf)
        if not self.img_flag:
            self.image_box.add(self.img_gtk)    # Add Image in the box, only once (first time)
        self.img_gtk.show()
        self.win.show_all()
        if not self.img_flag:
            self.thread_gtk()                   # gtk.main() only once (first time)
            #print "change flag"
            self.img_flag=1                     # change flag
        
    def thread_gtk(self):
        # changed this function. Improved threading.
        #print "create thread"
        self.thrd = Thread(target=gtk.main, name = "GTK thread")
        self.thrd.daemon = True
        #print "start thread"
        self.thrd.start()
        #print "thread_gtk end"
    
    def leave_app(self,widget,data):
        self.done = True
        self.win.destroy()
        gtk.main_quit()
        
    def press_callback(self,widget,event):
        self.mouseX = int(event.x)
        self.mouseY = int(event.y)
        self.mouse_rawX = int(event.x_root)
        self.mouse_rawY = int(event.y_root)
        print self.mouseX, self.mouseY, self.mouse_rawX, self.mouse_rawY,"press"
        
    def motion_callback(self,widget,event):
        self.mouseX = int(event.x)
        self.mouseY = int(event.y)
        self.mouse_rawX = int(event.x_root)
        self.mouse_rawY = int(event.y_root)
        print self.mouseX, self.mouseY, self.mouse_rawX, self.mouse_rawY,"motion"
    
    def isDone(self):
        return self.done
    
    def quit(self):
        self.done = True
        self.win.destroy()
        gtk.main_quit()
    
