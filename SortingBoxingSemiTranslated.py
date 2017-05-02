import cv2
import numpy as np
import copy
##import matplotlib.pyplot as plt

## img = cv2.imread("Test1.tif", cv2.IMREAD_GRAYSCALE) 
## This reads image from folder 

## plt.imshow(img, cmap='gray', interpolation='bicubic')
## plt.plot([], []) 
## plt.show() 

# This shows the image as a plot (pixels x pixels) 

# to referance a specific pixel we use: 
## px = img[a, b] where a and b are the coordinates! (0,0 is top left!) 
## px will return the colour value of the pixel
## we can change the colour of the px: 
## img[a, b] = [0, 0, 0] (blue,green,red) 

# We can do the same for a region of intrest (output all of their colours or 
# or change all of their colours together) 
## img[100:150, 100:150]  the first is y-axis the second is x-axis! 
## img[100:150, 100:150] = (0, 0, 0) to change colour of all pixels in the space

##..............................................................................

def RegionOfInterest(ImageName): 
    Img = cv2.imread(ImageName, cv2.IMREAD_GRAYSCALE)
    h, w = Img.shape 
    return Img[(h - 1600):h, 0:w] 
##..............................................................................

def pixelate(ImageName):
    Img = cv2.imread(ImageName, cv2.IMREAD_GRAYSCALE)
    dst = copy.copy(Img)
    

    Img[Img >= 128] = 255
    Img[Img < 128] = 0    
    
    for i in range(1,31, 2):
        cv2.blur(Img, (85, 85), dst, (-1,-1), 0 )
    
    dst[dst >= 128] = 255
    dst[dst < 128] = 0  
    
#    cv2.namedWindow('Ass', cv2.WINDOW_NORMAL)
#    cv2.imshow('Ass', dst) # shows image in a window called 'CSA1' 
#    cv2.waitKey(0)
#    cv2.destroyAllWindows() 
          
##..............................................................................
def avrg_colour(ImageName):
    im = cv2.imread(ImageName)
    return (im.mean())

##..............................................................................
def find_the_one(Img):
    i = 0
    #200x200 squares
    #Find topleft most white intensity
    #Recursive to number
    #Find center
    #Overlay grid
    
##..............................................................................
    
x = []
for q in range(15):
    x.append(0)
    
def whatBoxImIn(xGiven, yGiven, storage):
    ##Overlays grid based on fixed box height and width
    ##Uses this information to determine position of point given
    BoxHeight = 150
    BoxWidth = 200
    isIn = False
    
    x[15], y[15];
  
    while (isIn == False) :
        i = 0
        j = 0
        xIn = False
        yIn = False
        
        if (xGiven >= x[i]):
            i += 1
        else :
            xIn = true
        
        if (yGiven >= y[j]): 
            j += 1
        else:
            yIn = true
        
        if (yIn == true and xIn == true) :
            isIn = true
            storage[i][j] = 1
    
    offsetX = 301
    offsetY = 87
    
    for i in range(0, 15):
        x[i] += offsetX
        
    for i in range(0,5):
        y[j] += offsetY
        
    return 'sex'