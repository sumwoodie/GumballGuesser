# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:09:03 2021

@author: lde741
"""


import cv2
import math
   
# get the coordinates of the points clicked on the image 
def click_event(event, x, y, flags, params):
    font = cv2.FONT_HERSHEY_SIMPLEX 
    #BLACK RECTANGLE
    cv2.rectangle(resized, (0,0), (width,80), (0,0,0), -1)    
    global clickCounter
    
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        global jar_x1
        global jar_x2
        global jar_y1
        global jar_y2
        global gumball_x1
        global gumball_x2
        
        if clickCounter == 0:
            jar_x1 = x
            cv2.putText(resized, 'Select the MIDDLE RIGHT', (0,25), 
                    font, 1, (255, 0, 0), 2)
            cv2.putText(resized, 'side of the contaner', (0,65), 
                    font, 1, (255, 0, 0), 2)
        elif clickCounter == 1:
            jar_x2 = x
            cv2.putText(resized, 'Select the TOP CENTER', (0,25), 
                    font, 1, (255, 0, 0), 2)
            cv2.putText(resized, 'of the contaner', (0,65), 
                    font, 1, (255, 0, 0), 2)
        elif clickCounter == 2:
            jar_y1 = y
            cv2.putText(resized, 'Select the BOTTOM CENTER', (0,25), 
                    font, 1, (255, 0, 0), 2)
            cv2.putText(resized, 'of the contaner', (0,65), 
                    font, 1, (255, 0, 0), 2)
        elif clickCounter == 3:
            jar_y2 = y
            cv2.putText(resized, 'Select the MIDDLE LEFT', (0,25), 
                    font, 1, (255, 0, 0), 2)
            cv2.putText(resized, 'side of a Gumball', (0,65), 
                    font, 1, (255, 0, 0), 2)
        elif clickCounter == 4:
            gumball_x1 = x
            cv2.putText(resized, 'Select the MIDDLE RIGHT', (0,25), 
                    font, 1, (255, 0, 0), 2)
            cv2.putText(resized, 'side of a Gumball', (0,65), 
                    font, 1, (255, 0, 0), 2)
        elif clickCounter == 5:
            gumball_x2 = x
            jar_diameter = jar_x2 - jar_x1
            jar_height = jar_y2 - jar_y1
            jar_volume = jar_height * math.pi * (jar_diameter/2)**2
            gumball_diameter =  gumball_x2 - gumball_x1
            gumball_volume = 4/3 * math.pi * (gumball_diameter/2)**3
            guess = math.ceil(.64 * jar_volume / gumball_volume)
            cv2.putText(resized, '# of Gumballs are', (0,25), 
                    font, 1, (255, 0, 0), 2)
            cv2.putText(resized, str(guess), (20,65), 
                    font, 1, (255, 0, 0), 2)

        clickCounter += 1
  
        # Mark the spot
        cv2.putText(resized, 'X', (x,y), font, 0, (255, 0, 0), 5)
        cv2.imshow('GUMBALL GUESSER', resized)

# driver function
if __name__=="__main__":
    clickCounter = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # upload your image here
    img = cv2.imread("tall_far.jpg")
    
    #Resize the images if needed 
    scale_percent = 30 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    #BLACK RECTANGLE
    resized = cv2.rectangle(resized, (0,0), (width,80), (0,0,0), -1)
    
    cv2.putText(resized, 'Select the MIDDLE LEFT', (0,25), 
                    font, 1, (255, 0, 0), 2)
    cv2.putText(resized, 'side of the contaner', (0,65), 
                    font, 1, (255, 0, 0), 2)
    # displaying the image
    cv2.imshow('GUMBALL GUESSER', resized)
  
    # setting mouse hadler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('GUMBALL GUESSER', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)
  
    # close the window
    cv2.destroyAllWindows()
