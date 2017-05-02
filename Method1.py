import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('Test1.tif', cv2.IMREAD_GRAYSCALE)  # Reads the image in folder 

cv2.imshow('CSA1', img) # shows image in a window called 'CSA1' 
cv2.waitKey(0)
cv2.destroyAllWindows() 


