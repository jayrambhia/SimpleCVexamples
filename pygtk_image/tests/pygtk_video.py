"""
An example to show how pygtk can be used for continuous frames instead of pygame.
I have used threading and gobject.
"""
import gtk
from SimpleCV import *
from threading import Thread
import gobject
gtk.gdk.threads_init()

class MainWindow():
    def __init__(self):
        self.win = gtk.Window()
        self.img = None
        self.mouseX=None
        self.mouseY=None
        self.vid_flag=1
        self.cam = Camera()
        self.win.connect("delete_event",self.leave_app)
        self.img_box = gtk.EventBox()
        self.img_box.connect("button_press_event",self.press_callback)
        self.win.add(self.img_box)
        self.vid_thread()
        self.win.show_all()
    
    def press_callback(self,widget,data):
        self.mouseX = data.x
        self.mouseY = data.y
        print self.mouseX, self.mouseY
        self.image.drawRectangle(int(self.mouseX),int(self.mouseY),100,100,width=5)
        self.vid_flag=0                             # thread will end
        self.add_image(self.image.applyLayers())    # very important to do applyLayers()
                                                    # otherwise drawinglayers wouldn't be added
        time.sleep(0.05)    # need to give time delay, otherwise gtk gets two images to show in very less time. 
                            #give error Warning: g_object_ref: assertion `object->ref_count > 0' failed
        self.vid_flag = 1                           
        gobject.idle_add(self.vid_thread)           # start thread after image is shown.
                                                    # If gobject.idle_add() not added, self.add_image() waits for
                                                    # function to complete, and a new thread is created to show video
                                                    # and the effect can't be seen.
    
    def leave_app(self,widget,event):
        self.win.destroy()
        gtk.main_quit()
        self.vid_flag=0
        
    def vid_thread(self):
        #time.sleep(0.1)
        Thread(target=self.play_video).start()
        
    def play_video(self):
        while self.vid_flag:
            self.image = self.cam.getImage()
            self.add_image(self.image)
            time.sleep(0.05)
            
    def add_image(self,image=None):
        new_image = image.toRGB()
        img = new_image.getBitmap()
        if self.img is None:
            self.img = gtk.Image()
            self.win_add=1
        img_pixbuf = gtk.gdk.pixbuf_new_from_data(img.tostring(),gtk.gdk.COLORSPACE_RGB,False,img.depth,img.width,img.height,img.width*img.nChannels)
        self.img.set_from_pixbuf(img_pixbuf)
        if self.win_add:
            self.img_box.add(self.img)
            self.win_add=0
        self.img.show()
        
if __name__ == "__main__":
    MainWindow()
    gtk.main()
    

