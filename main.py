import os
from zipfile import ZipFile
from pathlib import Path, PurePath


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

zipFileName = find_zipfile()
unzippedFileName = zipFileName[:-4]

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
    """
    if not os.path.exists('PDFs'):
        os.makedirs('PDFs')

    mydict = {}
    for path in Path(unzippedFileName).rglob('*.pdf'):
        #print(PurePath(path).parts)
        docname = PurePath(path).parts[-1] # the prefix of the document, ex : 'SavingsAgreement.pdf'

        newpath = os.path.join('PDFs',docname)

        if docname not in mydict:
            mydict[docname]=1
            os.rename(path,newpath)
        else:
            mydict[docname]+=1
            newpath = os.path.join('PDFs',docname+'v'+str(mydict[docname]))
            os.rename(path,newpath)
        
        #     print(path)
        # os.rename(path,newpath)

def move_csv():
    """ Move all CSVs in the folder structure to a centralized location : A new folder in the root level directory. 
    Parameters:
        dir (str) : path to a folder 
    Returns:
        None
    """
    if not os.path.exists('CSVs'):
        os.makedirs('CSVs')

    for path in Path(unzippedFileName).rglob('*.csv'):
        docname = PurePath(path).parts[-1]
        newpath = os.path.join('CSVs',docname)
        os.rename(path,newpath)





if __name__ == '__main__':
    unpack_zip(find_zipfile())
    move_pdf()
    print(len(os.listdir('PDFs')))