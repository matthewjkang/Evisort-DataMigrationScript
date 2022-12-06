from ziphandler import *
from pathlib import Path, PurePath
import os
import re
import pandas as pd

"""
Problem : 
    Only the most recent version of PDFs must be kept

EX : 
    13Batch/13Batch/13Batch120221114100004/Contract Workspaces/2022/Jun/CW234xxxx/CW23432xx/CW2343257/CW2343257/CW2343257/WS3559690329/WS3662673164/Doc3662737342.pdf
    13Batch/13Batch/13Batch120221114100004/Contract Workspaces/2022/Jun/CW234xxxx/CW23432xx/CW2343257/CW2343257/CW2343257/WS3559690329/WS3662673164/Doc3662737342_ver_2_0.pdf
    13Batch/13Batch/13Batch120221114100004/Contract Workspaces/2022/Jun/CW234xxxx/CW23432xx/CW2343257/CW2343257/CW2343257/WS3559690329/WS3662673164/Doc3662737342_ver_3_0.pdf

    Keep "Doc3662737342_ver_3_0.pdf", move it to PDF repository, and rename it to "Doc3662737342.pdf". 
---
Problem 2 : 
    PDFs must be renamed according to this naming convention -> DocXXXX_CWXXXXX_File_Name

EX 2 : 
    [ Doc3707990967   |   Zones_Quote_K2015832.pdf   |   CW2336992/WS3362024048/Doc3364167552.pdf ] -> Doc3707990967_CW2336992_Zones_Quote_K2015832
"""

 
def handleVersions(unzippedFolderName):
    #INPUT : Name of folder that comes from extracting zipfile
    #OUTPUT : Full list of paths to PDF's, Corrected for version. PDF's that do not match the 'DocXXXXXXX' naming convention are exlucded. 

    uniqueList = [] # list of file paths that do NOT have a version number suffix
    verList = [] # list of file paths that DO have a version number suffix
    for path in Path(unzippedFolderName).rglob('*.pdf'): # For every pdf in the file structure ...
        if PurePath(path).parts[-1][:3] == 'Doc': # If the last part of the path starts with 'Doc' ...
            if '_ver_' not in str(path): # If '_ver_' is not in the name of the path ... 
                uniqueList.append(path) 
            else:
                verList.append(path)

    # This block creates a dictionary that keeps track of version number. 
    # If the version number is greater, than update your dictionary value with the higher ver number. 
    verDict = {} 
    for i in verList: # For every value in the list of paths that have '_ver_' in them ... 
        j = PurePath(i).parts[-1] 
        jx,jy = j.split('_',1) # 'Doc3662737342_ver_3_0.pdf' for example, would be split into "Doc3662737342" and "ver_3_0.pdf"
        if jx not in verDict: # If "Doc3662737342" is NOT in your dictionary, then add it in as a key, with the value being "ver_3_0.pdf"
            verDict[jx] = jy
        else: # If "Doc3662737342" IS in your dictionary, then check that jy (the version number), is greater than the dictionary["Doc3662737342"]
            if jy > verDict[jx]: #In Python, comparison works on strings, using lexicographic order. "Doc3662737342_ver_3_0.pdf" > "Doc3662737342.pdf"
                verDict[jx] = jy 

    # This block checks if the file paths in uniqueList have higher version numbers, and renames them accordingly if so. 
    sep = os.sep # One must use os.sep instead of hard coding '/' because file path separators are different on Windows and Mac. (Windows = '\')
    final = []
    for i in uniqueList:
        x,y = str(i).rsplit(sep,1) #Splits the path by the LAST delimiter. So expect a two object list
        doc = y[:-4] #Indexing to -4 means that the '.pdf' part gets excluded. file types with different length endings might mess this up.
        if doc in verDict:
            y = doc +"_"+verDict[doc]
        final.append(x+sep+y)

    return final

def csvDF(): 
    # Input : None
    # Output : A Pandas Dataframe containing data from ALL relevant CSV's

    move_csv() # This function requires move_csv() to have already been run
    mergelist = []
    for i in os.listdir('CSVs'):
        csv = pd.read_csv(
            os.path.join('CSVs',i)
        )
        if ("InternalId" in csv.columns) and ('Title' in csv.columns) and ('Location' in csv.columns):
            mergelist.append(i)

    combined_csv = pd.concat( [ pd.read_csv(os.path.join('CSVs',f)) for f in mergelist ] )

    return combined_csv


# move_csv()
def moveAndRename():
    df = csvDF()
    if not os.path.exists('PDFs'):
        os.makedirs('PDFs')
    for i in handleVersions(zipObj().folder):
        mystr = i
        splitstr = mystr.split('/')
        docname = splitstr[-1][:-4]
        cw = set(re.findall( r'CW[0-9]{7}', mystr)).pop()
        internalid = docname.split('_',1)[0]
        title = df.loc[df['InternalId'] == internalid]['Title'].values[0]

        newname = os.path.join('PDFs',internalid+"_"+cw+"_"+title)
        os.rename(i,newname)

