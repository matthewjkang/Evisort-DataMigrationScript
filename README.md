# Evisort-ZipfileProcesser

## Usage (assuming user knows very little about programming)
1. Download this repository. (Click on the green button that says code, download as a zip. Unzip the file.)
2. Drag the zip file into the same folder as the main.py file.  
3. Then open up your command line and cd into the directory (it should have 2 things : your target zip file and main.py).  
4. run the command : python3 main.py 

## What Does it Do?
1. Recursively unzips the zip file, along with any zip files that are within it, until there are no more zip files.  
2. Moves all PDF's into a folder at the top level.  
3. Moves all CSV's into a folder at the top level.  

## TODO
1. Create a dictionary that holds stores {"Document Name" : "Desired Document Rename"}. This must be extracted from specific CSV's
2. Rename all the PDF's according to the dictionary. 
