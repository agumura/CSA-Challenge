import cv2
import numpy as np
import copy
import matplotlib.pyplot as plt
from scipy import ndimage

def simpleBlobDetector(ImageName) :
    im = cv2.imread(ImageName, cv2.IMREAD_GRAYSCALE)
    dst = copy.copy(im)

    im[im >= 128] = 255
    im[im < 128] = 0    
    
    for i in range(1,31, 2):
        cv2.blur(im, (20, 20), dst, (-1,-1), 0 )
    
    dst[dst >= 128] = 255
    dst[dst < 128] = 0      
    
    params = cv2.SimpleBlobDetector_Params() 
    # Change thresholds
    params.filterByColor = True
    params.blobColor = 255


    #params.filterByArea=True
    #params.minArea = 81*3.14
    
    detector = cv2.SimpleBlobDetector_create(params)  
    
    keypoints = detector.detect(dst)
    
    im_with_keypoints = cv2.drawKeypoints(dst, keypoints, np.array([]), (255,99,71), 0)
    
    plt.imshow(im_with_keypoints, cmap='gray', interpolation='bicubic')
    plt.plot([], []) 
    plt.show()    
    
    for keyPoint in keypoints:
        x = keyPoint.pt[0]
        y = keyPoint.pt[1]
        s = keyPoint.size
        print ("X: ", x, "Y: ", y, "Z: ", s)
        
def downsize(ar, fact):
    assert isinstance(fact, int), type(fact)
    sx, sy = ar.shape
    X, Y = np.ogrid[0:sx, 0:sy]
    regions = sy/fact * (X/fact) + Y/fact
    res = ndimage.mean(ar, labels=regions, index=np.arange(regions.max() + 1))
    res.shape = (sx/fact, sy/fact)
    return res    