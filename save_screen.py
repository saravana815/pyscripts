import os
import sys
import time
#---------------------------------------------------------
#User Settings:
SaveDirectory='C:\Users\sargandh\Documents\saravana_frm_xp\Saravana\py_scripts\screen_shots_ie\\'
from PIL import ImageGrab

num = 1
while True:
    num = raw_input("Enter question number to save :  ")
    print "Question num :", str(num)
    #img=ImageGrab.grab()
    img=ImageGrab.grab(bbox=(50, 100, 1220, 1080))
    #img=ImageGrab.grab(bbox=(300, 100, 1520, 1080))
    #saveas=os.path.join(SaveDirectory,'ScreenShot_'+time.strftime('%Y_%m_%d_%H_%M_%S')+'.png')
    saveas=os.path.join(SaveDirectory,'question_'+str(num)+'.png')
    img.save(saveas)
