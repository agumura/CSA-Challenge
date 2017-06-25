import cv2
import numpy as np
import copy
import matplotlib.pyplot as plt
import math 
import os

def average_colour(Imagename):
    img = cv2.imread(Imagename, cv2.IMREAD_GRAYSCALE)
    avrg_colour = img.mean()
    print(avrg_colour)
    return 
##..............................................................................
def RegionOfInterest(Img): 
    h, w = Img.shape 
    return Img[(h - 1600):h, 0:4000] 
##..............................................................................
    
def find_the_one_V2(Imagename): 
    img = cv2.imread(Imagename,cv2.IMREAD_GRAYSCALE)
    New_Img = RegionOfInterest(img)
    h,w = New_Img.shape
    pos_y = 0
    pos_x = 0 
    avrg_clr = 0 
    counter = 0
    max_pos_y = 0
    max_pos_x = 0
    max_avrg_clr = 0
    
    while ((avrg_clr < 80) and (counter != 200)): 
        
        if avrg_clr > max_avrg_clr:
            max_pos_y = pos_y
            max_pos_x = pos_x
            max_avrg_clr = avrg_clr
        
        
        pos_y += 75
        if pos_y >= h: 
            pos_y = 0 
            pos_x += 50
        ROI = New_Img[pos_y:(pos_y + 150), pos_x:(pos_x + 100)]
        avrg_clr = ROI.mean() 
        counter += 1 
#        print([avrg_clr, pos_y, pos_x])  # This line was for debugging!!
        
    return [max_pos_y, max_pos_x, max_avrg_clr]

##..............................................................................

## PROGRESS Check : 
# -> basically we need to change the shift values 
   ## --> 150 to 75 and 100 to 50
# -> figure out a good range for which we dont lose info 
   ## --> Fixed
# -> set a realisitc generalized loop limit 
   ## --> Fixed! 213.333 was calculated!

##//////////////////////////////////////////////////////////////////////////////
   
def accurate_fit(LoP, Imagename): # Note the list of positions (LoP), has (y,x)
    img = cv2.imread(Imagename,cv2.IMREAD_GRAYSCALE)
    New_Img = RegionOfInterest(img)
    base_y = LoP[0]
    base_x = LoP[1]
    main = LoP[2] 
    shftL = New_Img[base_y:(base_y + 150), (base_x - 10):(base_x - 10 + 100)]
    shftR = New_Img[base_y:(base_y + 150), (base_x + 10):(base_x + 10 + 100)]
    shft_L = shftL.mean() 
    shft_R = shftR.mean()
    
    while (shft_L > main) or (shft_R > main):
        if shft_L > main and shft_L > shft_R: 
            base_x -= 10
            main = shft_L 
        elif shft_R > main:
            base_x += 10 
            main = shft_R
        else:
            base_x += 10 
            main = shft_R
            
        shftL = New_Img[base_y:(base_y + 150), (base_x - 10):(base_x - 10 + 100)]
        shftR = New_Img[base_y:(base_y + 150), (base_x + 10):(base_x + 10 + 100)]
        shft_L = shftL.mean() 
        shft_R = shftR.mean()
    
    shftU = New_Img[(base_y + 10):(base_y + 10 + 150), base_x:(base_x + 100)]
    shftD = New_Img[(base_y - 10):(base_y - 10 + 150), base_x:(base_x + 100)]
    shft_U = shftU.mean() 
    shft_D = shftD.mean()    
    
    while (shft_U > main) or (shft_D > main):
        if shft_U > main and shft_U > shft_D: 
            base_y += 10
            main = shft_U 
        elif shft_D > main:
            base_y -= 10 
            main = shft_D
        else:
            base_y += 10 
            main = shft_U
            
        shftU = New_Img[(base_y + 10):(base_y + 10 + 150), base_x:(base_x + 100)]
        shftD = New_Img[(base_y - 10):(base_y - 10 + 150), base_x:(base_x + 100)]
        shft_U = shftU.mean() 
        shft_D = shftD.mean()
        
        
    return [base_y, base_x, main]

##..............................................................................

def show_case_Test(Imagename, base_y, base_x):
    img = cv2.imread(Imagename,cv2.IMREAD_GRAYSCALE)
    New_Img = RegionOfInterest(img)
    
    cv2.rectangle(New_Img, (base_x, base_y), ((base_x + 100), (base_y + 150)), (255,255,255), 2)
                        
    plt.imshow(New_Img, cmap='gray', interpolation='bicubic')
    plt.plot([], []) 
    plt.show()        

# This is a really Important test which can show exactly how the two functions 
# work together to find an accurate fit for the leading 1! 
# This is the base for the rest of the entire project! 

##..............................................................................

def grid_overlay(Imagename, base_y, base_x):
    img = cv2.imread(Imagename,cv2.IMREAD_GRAYSCALE)
    New_Img = RegionOfInterest(img)
    
    grid = [[],[],[],[]] 
    multiplier = 0 
    
    for i in range(12): 
        new_y = base_y + 200 
        new_base_x = base_x + 130 + (multiplier * 275)
        
        box = New_Img[base_y:new_y, new_base_x:(new_base_x + 275)] 
        avrg_clr = box.mean() 
        #print(avrg_clr) for debugging
        
        if avrg_clr >= 5: 
            grid[0].append(1)
        else:
            grid[0].append(0) 
        
        multiplier += 1
    
    multiplier = 0
        
    for i in range(12): 
        new_base_y = base_y + 200 
        new_base_x = base_x + 130 + (multiplier * 275)
        
        box = New_Img[new_base_y:(new_base_y + 250), new_base_x:(new_base_x + 275)] 
        avrg_clr = box.mean() 
        # print(avrg_clr) for debugging
        
        if avrg_clr >= 5: 
            grid[1].append(2)
        else:
            grid[1].append(0) 
        
        multiplier += 1 
    
    multiplier = 0
        
    
    for i in range(12): 
        new_base_y = base_y + 200 + 250
        new_base_x = base_x + 130 + (multiplier * 275)
                
        box = New_Img[new_base_y:(new_base_y + 250), new_base_x:(new_base_x + 275)] 
        avrg_clr = box.mean() 
        # print(avrg_clr) for debugging
                
        if avrg_clr >= 5: 
            grid[2].append(4)
        else:
            grid[2].append(0)
        
        multiplier += 1 
    
    multiplier = 0
    
    
    for i in range(12): 
        new_base_y = base_y + 200 + 500
        new_base_x = base_x + 130 + (multiplier * 275)
                
        box = New_Img[new_base_y:(min((new_base_y + 250), 1600)), new_base_x:(new_base_x + 275)] 
        avrg_clr = box.mean() 
        # print(avrg_clr) for debugging 
        
        if avrg_clr >= 5: 
            grid[3].append(8)
        else:
            grid[3].append(0)
        
        multiplier += 1
    
    return grid
##..............................................................................

def complete_grid_overlay(Imagename, base_y, base_x): 
    img = cv2.imread(Imagename,cv2.IMREAD_GRAYSCALE)
    New_Img = RegionOfInterest(img)
    
    multiplier = 0 
    
    for i in range(12): 
        new_y = base_y + 200 
        new_base_x = base_x + 130 + (multiplier * 275)
        
        cv2.rectangle(New_Img, (new_base_x, base_y), ((new_base_x + 275), (new_y)), (255,255,255), 2)
        
        multiplier += 1
    
    multiplier = 0
        
    for i in range(12): 
        new_base_y = base_y + 200 
        new_base_x = base_x + 130 + (multiplier * 275) 
        
        cv2.rectangle(New_Img, (new_base_x, new_base_y), ((new_base_x + 275), (new_base_y + 250)), (255,255,255), 2)
        
        multiplier += 1 
    
    multiplier = 0
        
    
    for i in range(12): 
        new_base_y = base_y + 200 + 250
        new_base_x = base_x + 130 + (multiplier * 275)
        
        cv2.rectangle(New_Img, (new_base_x, new_base_y), ((new_base_x + 275), (new_base_y + 250)), (255,255,255), 2)
        
        multiplier += 1 
    
    multiplier = 0
    
    
    for i in range(12): 
        new_base_y = base_y + 200 + 500
        new_base_x = base_x + 130 + (multiplier * 275)
                
        box = New_Img[new_base_y:(min((new_base_y + 250), 1600)), new_base_x:(new_base_x + 275)] 
        avrg_clr = box.mean() 
        
        cv2.rectangle(New_Img, (new_base_x, new_base_y), ((new_base_x + 275), (min((new_base_y + 250), 1600))), (255,255,255), 2)
        
        multiplier += 1
    
    plt.imshow(New_Img, cmap='gray', interpolation='bicubic')
    plt.plot([], []) 
    plt.show()
    
##..............................................................................
def translator(grid):
    year = 1960 + (grid[0])[0] + (grid[1])[0] + (grid[2])[0] + (grid[3])[0]
    
    day_of_year =  100*((grid[0])[1] + (grid[1])[1] + (grid[2])[1] + (grid[3])[1]) \
                +  10*((grid[0])[2] + (grid[1])[2] + (grid[2])[2] + (grid[3])[2])  \
                + ((grid[0])[3] + (grid[1])[3] + (grid[2])[3] + (grid[3])[3])
    
    hour = 10*((grid[0])[4] + (grid[1])[4] + (grid[2])[4] + (grid[3])[4]) + \
           (grid[0])[5] + (grid[1])[5] + (grid[2])[5] + (grid[3])[5]
    
    minute = 10*((grid[0])[6] + (grid[1])[6] + (grid[2])[6] + (grid[3])[6]) + \
             (grid[0])[7] + (grid[1])[7] + (grid[2])[7] + (grid[3])[7]
             
    second = 10*((grid[0])[8] + (grid[1])[8] + (grid[2])[8] + (grid[3])[8]) + \
             (grid[0])[9] + (grid[1])[9] + (grid[2])[9] + (grid[3])[9]
    
    station_number = 10*((grid[0])[10] + (grid[1])[10] + (grid[2])[10] + (grid[3])[10]) + \
                    (grid[0])[11] + (grid[1])[11] + (grid[2])[11] + (grid[3])[11]
    
    return [year, day_of_year, hour, minute, second, station_number]

##..............................................................................
def Decipher_All(Imagename):
    LoP = find_the_one_V2(Imagename)
    LoP2 = accurate_fit(LoP, Imagename)
    grid = grid_overlay(Imagename, LoP2[0], LoP[1])
    Final = translator(grid)
    return Final
##..............................................................................
def Decipher_All_UFV(Imagename):
    LoP = find_the_one_V2(Imagename)
    LoP2 = accurate_fit(LoP, Imagename)
    grid = grid_overlay(Imagename, LoP2[0], LoP[1])
    Final = translator(grid)
    message = 'year is {0}, day of year is {1}, time is {2}:{3}:{4}, station # is {5}'
    final_message = message.format(Final[0], Final[1], Final[2], Final[3], Final[4], Final[5])
    return final_message
##..............................................................................
def quick_test(Imagename): 
    LoP = find_the_one_V2(Imagename)
    LoP2 = accurate_fit(LoP, Imagename)
    grid = grid_overlay(Imagename, LoP2[0], LoP[1])
    return grid
##..............................................................................
def quick_test2(Imagename): 
    LoP = find_the_one_V2(Imagename)
    LoP2 = accurate_fit(LoP, Imagename)
    grid = complete_grid_overlay(Imagename, LoP2[0], LoP[1])
    return
##..............................................................................

def translate_all(path, file_name):
    # where path1 is the location of all files that need to be translated 
    # where file_name is the output file
    # ***NOTE*** This file must be in the same directory as the output file
    f = open(file_name, 'w')
    for file in os.listdir(path):
        message = Decipher_All_UFV(file)
        addition = 'File name is {0}, '.format(file)
        final = addition + message 
        f.write(final + "\n")
    f.close()
    return("it worked?!")

        
        
    
    
    
    