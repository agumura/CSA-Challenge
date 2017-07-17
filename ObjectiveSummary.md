# CSA Challenge
    Images from Canada's very first satellite, Alouette-I, have been digitized! This data has rich historical value and is of interest to scientists today. The images can help us study how activity in the ionosphere can interfere with satellite signals for navigation, positioning and communications.
    
    An Ionogram is a graph which showcases charged ion density at different altitudes of the atmosphere. Each ionogram has, encoded within it, information about the location, date and time the graph was recorded. All of these Ionograms were originally printed on rolls of film in the 1960s - 1970s. They were recently scanned and uploaded as image files (.tif format).  

    The Problem: For scientists to use this data, they have to manually plow through thousands of pictures and decipher the coded metadata by hand. The Ionograms are also not organized by date or location so scientists can’t tell if the pictures they have are even from the same time period without deciphering each one. 
    
    Our Solution: Using Python's public libraries (OpenCV, Matplot.lib), we have created a program which will decode the metadata of all of the ionograms in a given directory and create a searchable text file with the names of each image along with the decoded information!  
