# Evisort-ZipfileProcesser

## Problem Statement
* Given a zip file with more nested zip files inside, recursively unzip all zip files until the file structure contains no more zip files.  
* Then, rename all PDF's within the file structure according to naming conventions that are provided by CSV's within the file structure. 

**TLDR :**  
Input = Zip file  
Output = Folder with renamed PDFs

## Usage (assuming user knows very little about programming)
1. Download this repository. (Click on the green button that says code, download as a zip. Unzip the file.)
2. Drag the zip file into the same folder as the main.py file.  
3. Then open up your command line and cd into the directory (it should have 2 things : your target zip file and main.py).  
4. run the command : python3 main.py  

**Limitiations and Precautions**: Do not give me a zip bomb 😐  
 **Prerequisites:** Python3 must be downloaded on your computer

## What Does it Do?
1. Recursively unzips the zip file, along with any zip files that are within it, until there are no more zip files.  
2. Moves all PDF's into a folder at the top level.  
3. Moves all CSV's into a folder at the top level.  

## TODO
1. Create a dictionary that holds stores {"Document Name" : "Desired Document Rename"}. This must be extracted from specific CSV's
2. Rename all the PDF's according to the dictionary. 
3. Check if any CSV's are overwritten / lost due to same name. 
