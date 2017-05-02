import cv2
import numpy as np
import copy
import matplotlib.pyplot as plt

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
    return Img[(h - 1600):h, 0:4000] 


##..............................................................................

def pixelate(Img):
    dst = copy.copy(Img)

    Img[Img >= 128] = 255
    Img[Img < 128] = 0    
    
    for i in range(1,31, 2):
        cv2.blur(Img, (85, 85), dst, (-1,-1), 0 )
    
    #dst[dst >= 128] = 255
    #dst[dst < 128] = 0  
    
    return dst
    
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
    for i in range(0, 20): 
        for j in range(0,8): 
            X1 = i*200
            Y1 = j*200 
            X2 = X1 + 200 
            Y2 = Y1 + 200 
            
            ROI2 = Img[Y1:Y2, X1:X2] 
            
            Pixel_Intensity = ROI2.mean() 
            
            
            if Pixel_Intensity >= 5: 
                print([X1, Y1, X2, Y2])
                print(Pixel_Intensity)
                return [X1, Y1, X2, Y2] 
    print("No bright pixels within ROI")




##..............................................................................

## TESTING! 
def test_func(ImageName): 
    ROI = RegionOfInterest(ImageName) 
    final = pixelate(ROI)
    
    Lst = find_the_one(final)
    cv2.rectangle(final, (Lst[0], Lst[1]), (Lst[2], Lst[3]), (255,255,255), 2)
    
    plt.imshow(final, cmap='gray', interpolation='bicubic')
    plt.plot([], []) 
    plt.show()
    

##..............................................................................

def All_Positions(Img): 
    Lst_X = [] 
    Lst_Y = [] 
    
    for i in range(0, 20): 
        for j in range(0,8): 
            X1 = i*200
            Y1 = j*200 
            X2 = X1 + 200 
            Y2 = Y1 + 200     
            
            ROI2 = Img[Y1:Y2, X1:X2] 
            
            Pixel_Intensity = ROI2.mean() 
            
            if Pixel_Intensity >= 5:
                Lst_X.append(X1) 
                Lst_Y.append(Y1) 
                
    print(Lst_X) 
    print(Lst_Y)
    return [Lst_X, Lst_Y] 

##..............................................................................

def test_func2(ImageName): 
    ROI = RegionOfInterest(ImageName) 
    final = pixelate(ROI)
    LOPs = All_Positions(final)
    
    n = len(LOPs[0])
    
    for i in range(0,n):
        x = (LOPs[0])[i]
        y = (LOPs[1])[i]
        x2 = x + 200 
        y2 = y + 200 
        
        cv2.rectangle(final, (x, x2), (y, y2), (255,255,255), 2)
        
    
            
    plt.imshow(final, cmap='gray', interpolation='bicubic')
    plt.plot([], []) 
    plt.show()    
    
##..............................................................................
    
    
    