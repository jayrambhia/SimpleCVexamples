"""
This is an example of how SimpleCV can be used so easily to do anything.
I am controlling volume and changing songs in banshee media player by
detecting optical flow.
Banshee has a bug, so a banshee window should be opened before running
this program.
I am using multiprocessing and multithreading to control banshee media
player.

Requirements:
SimpleCV, and its dependencies
alsaaudio library to control volume
Banshee Media Player

Tested on Ubuntu 11.10
"""
from SimpleCV import *
import os
import time
import threading
import sys
from multiprocessing import Process
import alsaaudio

def banshee():
    """
    Start a banshee window if it is not opened
    """
    os.system('banshee --play')
    time.sleep(5)
    return
    
    
class do(threading.Thread):
    def __init__(self):
        """
        starting a thread
        """
        threading.Thread.__init__(self)
        
    def run(self):
        m = alsaaudio.Mixer()   # defined alsaaudio.Mixer to change volume
        scale_amount = (300,250)    # increased from (200,150). works well
        d = Display(scale_amount)
        cam = Camera()
        prev = cam.getImage().scale(scale_amount[0],scale_amount[1])
        time.sleep(0.5)
        buffer = 20
        count = 0
        prev_t = time.time()    # Note initial time
        while d.isNotDone():
            current = cam.getImage()
            current = current.scale(scale_amount[0],scale_amount[1])
            if( count < buffer ):
                count = count + 1
            else:
                fs = current.findMotion(prev, method="LK")   # find motion
                # Tried BM, and LK, LK is better. need to learn more about LK
                if fs:      # if featureset found
                    dx = 0
                    dy = 0
                    for f in fs:
                        dx = dx + f.dx      # add all the optical flow detected
                        dy = dy + f.dy
                
                    dx = (dx / len(fs))     # Taking average
                    dy = (dy / len(fs))

                    prev = current
                    time.sleep(0.01)
                    current.save(d)
                    
                    if dy > 2 or dy < -2:
                        vol = int(m.getvolume()[0]) # getting master volume
                        if dy < 0:
                            vol = vol + (-dy*3)
                        else:
                            vol = vol + (-dy*3)
                        if vol > 100:
                            vol = 100
                        elif vol < 0:
                            vol = 0
                        print vol
                        m.setvolume(int(vol))   # setting master volume
                        
                    if dx > 3:
                        cur_t = time.time()
                        if cur_t > 5 + prev_t:  # adding some time delay
                            self.play("next")   # changing next
                            prev_t = cur_t
                        
                    if dx < -3:
                        cur_t = time.time()
                        if cur_t > 5 + prev_t:
                            prev_t = cur_t
                        self.play("previous")   # changing previous
                        
    def play(self,command):
        """
        change, next or prev
        """
        os.system('banshee --'+command)     # giving command to change
        
        
def main():
 
    p = Process(target = banshee)   #Create a process which will initiate banshee window
    p.start()   # starting the process
    
    command = do()  # Create a thread
    command.start() # start the thread
    command.join()  # wait for the thread to complete
    p.terminate()   # After thread ends, terminate the main process
    print 'terminate'
    
if __name__ == '__main__':
    main()
