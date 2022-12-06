import os
from zipfile import ZipFile
from pathlib import Path, PurePath

class zipObj: # Used to easily access zipfile name and folder name
    def find_zipfile():
        """Finds the first zip file in your directory that needs to be unzipped. There can only be one.
        Parameters:
            None
        Returns:
            zipfiles[0] (str) : a path to the first zipfile that you want to unpack
        """
        zipfiles = []
        for i in os.listdir():
            if i[-4:] == '.zip':
                zipfiles.append(i)
        if len(zipfiles) != 1:
            return '''
            You have more than one initial zipfile in this folder.
            Make sure that there is only one zip file and start again'''
        else:
            return zipfiles[0]

    zipf = find_zipfile()
    folder = find_zipfile()[:-4] # Folder is the name of the folder that comes from the extracted zipfile.

def unpack_zip(zipfile='', path_from_local=''):
    """ Recursively unpack all nested zip files 
    Parameters:
        zipfile (str) : file path to zip file
        path_from_local (str) : file path to local directory (optional)
    Returns:
        extract_path (str) : path to extracted zip file
    """
    filepath = path_from_local+zipfile
    extract_path = filepath.strip('.zip')+'/'
    parent_archive = ZipFile(filepath)
    parent_archive.extractall(extract_path)
    namelist = parent_archive.namelist()
    parent_archive.close()
    for name in namelist:
        try:
            if name[-4:] == '.zip':
                unpack_zip(zipfile=name, path_from_local=extract_path)
        except:
            print('failed on', name)
            pass
    return extract_path

def move_pdf():
    """ Move all PDFs in the folder structure to a centralized location : A new folder in the root level directory. 
    Parameters:
        dir (str) : path to a folder 
    Returns:
        None
    ---
    Problem : Some PDF's have the same name. 
    EX : "Signed Contract Documents.pdf" appears 5 times in the file structure, in different contract workspaces.

    Solution : Add a counter varaible to the end of each repeated pdf.
    "Signed Contract Documents.pdf" vs "Signed Contract Documentsv2.pdf"
    ---
    """
    unzippedFileName = zipObj().zipf
    if not os.path.exists('PDFs'):
        os.makedirs('PDFs')

    mydict = {}
    for path in Path(unzippedFileName).rglob('*.pdf'):
        docname = PurePath(path).parts[-1] # the prefix of the document, ex : 'SavingsAgreement.pdf'
        newpath = os.path.join('PDFs',docname)

        if docname not in mydict:
            mydict[docname]=1
            os.rename(path,newpath)
        else:
            mydict[docname]+=1
            name,ext = docname[:-4],docname[-4:] 
            newpath = os.path.join( 'PDFs',name+'v'+str(mydict[docname])+ext) 
            os.rename(path,newpath)

def move_csv():
    """ Move all CSVs in the folder structure to a centralized location : A new folder in the root level directory. 
    Parameters:
        dir (str) : path to a folder 
    Returns:
        None
    ---
    Problem : Some CSV's have the same name. 
    EX : "index.csv" appears 3 times in the file structure, in different contract workspaces.

    Solution : Add a counter varaible to the end of each repeated CSV.
    "index.csv" vs "indexv2.csv"
    ---
    """
    unzippedFileName = zipObj().folder
    if not os.path.exists('CSVs'):
        os.makedirs('CSVs')

    mydict = {}
    for path in Path(unzippedFileName).rglob('*.csv'):
        docname = PurePath(path).parts[-1] # the prefix of the document, ex : 'SavingsAgreement.pdf'
        newpath = os.path.join('CSVs',docname)

        if docname not in mydict:
            mydict[docname]=1
            os.rename(path,newpath)
        else:
            mydict[docname]+=1
            name,ext = docname[:-4],docname[-4:] 
            newpath = os.path.join( 'CSVs',name+'v'+str(mydict[docname])+ext) 
            os.rename(path,newpath)


