# Evisort-DataMigrationScript
Takes a zip file, sent to us from Ariba, and reorganizes / renames key documents.

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
2. Clean up PDFs throughout the file structure.  
    - In cases with same document, different version numbers, only the highest version number is kept. 
    - Renames the PDF's according to the convention 'DocXXXXX_CWXXXXX_File_name.pdf'
3. Moves all CSV's into a folder at the top level.  
4. Aggregate those CSVs, create a dataframe that maps InternalId to Document Title. 
5. Looks at each PDF that needs to be renamed, searches for its correct Document Title given its InternalID, and renames and moves the PDF.

## Known Limitations
1. This will only work on data that comes in the format that SAP Ariba uses.
2. Certain PDF's are unreadable, but this is because the actual PDF within the zipfile contains a broken PDF.
    - Only occurs in certain documents that have a version number. The non-versioned PDF is valid though.
    - I can fix this easily by using the non-versioned PDF.


