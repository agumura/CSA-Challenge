import cv2
import numpy as np
import copy
import matplotlib.pyplot as plt
import math
from PIL import Image
#from scipy import ndimage

def simpleBlobDetector(ImageName) :
    im = cv2.imread(ImageName, cv2.IMREAD_GRAYSCALE)
    width, height = im.shape

    dst = copy.copy(im)
    

    im[im >= 128] = 255
    im[im < 128] = 0    
    
    #for i in range(1,31, 2):
    #    cv2.blur(im, (20, 20), dst, (-1,-1), 0 )      

    #img = Image.open(ImageName)
    
    #cv2.resize(im, dst, dst.size(), 0, 0, cv2.INTER_AREA)
    #cv2.resize(im, dst, dst.size(), 0, 0, cv2.INTER_AREA)
    #resized_image = cv2.resize(im, (x, y)) 
    #dst = cv2.resize(resized_image, (height, width)
    pixelSize = 20

    
    image = Image.open(ImageName).convert("L")
    
    a = math.floor(image.size[0]/pixelSize)
    b = math.floor(image.size[1]/pixelSize)   
    
    image = image.resize((a, b), Image.NEAREST)
    image = image.resize((image.size[0]*pixelSize, image.size[1]*pixelSize), Image.NEAREST)    

    image = image.resize((a/2, b/2), Image.NEAREST)
    image = image.resize((image.size[0]*pixelSize, image.size[1]*pixelSize), Image.NEAREST)    
   
    dst = np.array(image)
    
    #data = np.asarray( image, dtype="int32" )
    #img = Image.fromarray( np.asarray( np.clip(npdata,0,255), dtype="uint8"), "L" )  
    #dst = cv2.imread(data)
    
    
    #img = img.resize((20,20),Image.ANTIALIAS) # downsize
    #img = img.resize((369,472), Image.ANTIALIAS) # upsize     
    
    a = 60
    
    dst[dst >= a] = 255
    dst[dst < a] = 0   
    
    #plt.imshow(dst, cmap='gray', interpolation='bicubic')
    #plt.plot([], []) 
    #plt.show()       
    
    params = cv2.SimpleBlobDetector_Params() 
    # Change thresholds
    params.filterByColor = True
    params.blobColor = 255

    params.filterByCircularity = True
    params.minCircularity = 0.0
    params.maxCircularity = 1
    
    params.filterByConvexity = True
    params.minConvexity = 0.0
    params.maxConvexity = 1
    
    params.filterByInertia = True
    params.minInertiaRatio = 0.1
    
    detector = cv2.SimpleBlobDetector_create(params)  
    
    keypoints = detector.detect(dst)
    
    params.filterByConvexity = True
    params.minConvexity = 0
    params.maxConvexity = 1     
    
    #params.filterByArea = True
    #params.minArea = 40
    
    detector2 = cv2.SimpleBlobDetector_create(params)  
    keypoints2 = detector2.detect(dst)
    
    keypoints.extend(keypoints2)
    
    #imf = cv2.imread(dst, cv2.IMREAD_GRAYSCALE)
    
    im_with_keypoints = cv2.drawKeypoints(dst, keypoints, np.array([]), (255,99,71), 0)
       
    plt.imshow(im_with_keypoints, cmap='gray', interpolation='bicubic')
    plt.plot([], []) 
    plt.show()    
    
    for keyPoint in keypoints:
        x = keyPoint.pt[0]
        y = keyPoint.pt[1]
        s = keyPoint.size
        print ("X: ", x, "Y: ", y, "Z: ", s)
        
def downsize(ImageName):
    img = Image.open(ImageName)
    #im = cv2.imread(ImageName, cv2.IMREAD_GRAYSCALE)    
    #newSourceFile = copy.copy(im)
    
    img = img.resize((20,20),Image.ANTIALIAS) # downsize
    img = img.resize((369,472), Image.ANTIALIAS) # upsize    
    #img.save(newSourceFile, quality = 95, dpi=(72,72), optimize = True) 
    
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.plot([], []) 
    plt.show()        

def downsize2(ImageName):
    backgroundColor = (0,)*3
    pixelSize = 15
    
    image = Image.open(ImageName)
    image = image.resize((image.size[0]/pixelSize, image.size[1]/pixelSize), Image.NEAREST)
    image = image.resize((image.size[0]*pixelSize, image.size[1]*pixelSize), Image.NEAREST)
    pixel = image.load()
    
    """for i in range(0,image.size[0],pixelSize):
        for j in range(0,image.size[1],pixelSize):
            for r in range(pixelSize):
                pixel[i+r,j] = backgroundColor
                pixel[i,j+r] = backgroundColor"""
    
    plt.imshow(image, cmap='gray', interpolation='bicubic')
    plt.plot([], []) 
    plt.show()        
