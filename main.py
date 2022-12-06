from ziphandler import *
from pdfHandler import *

'''
1. find the zip file name
2. recursively unpack the zip file
3. move all csv's to the CSV directory
4. create a dataframe by aggregating all relevant CSVs
5. use handleVersions to create a list (of full file paths) of all PDFs in the file structure
    - PDFs that include version number will only select the highest version number. Lower versions will not be included in the list.
6. create the NEW PDF NAMES by using string manipulation / regex on each file path in the handleVersions list
    - os.rename(path_to_file,destination)
        path_to_file = full file path (from handleVersion list)
        destination = NEW PDF NAME
    - We do not want the wrong file to be moved (wrong version gets moved, etc)
'''

if __name__ == '__main__':
    unpack_zip(zipObj().zipf)
    moveAndRename()