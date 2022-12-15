import magic
import os

def checkmime(): # In place, no arguments. TODO : Consider whether or not I should folder as an argument.
    mime = magic.Magic(mime=True)
    mimetypedict = { # Add more file types as they come up I guess 
        'application/msword':'.doc', #Doc
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document':'.docx', # DocX
        'application/vnd.ms-excel':'.xls', # Old Excel
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':'.xlsx', #Excel
        'text/plain':'.txt', # Text file
        'text/csv':'.csv' #CSV file
    }

    mydir = 'Renamed_PDFs'
    allpdf = os.listdir(mydir)
    for i in allpdf:
        path = os.path.join(mydir,i)
        mytype = mime.from_file(path) # Get the mime type
        if mytype in mimetypedict:
            correctsuffix = mimetypedict[mytype] # find the corresponding suffix for the mime type found in mytype
            correctpath = os.path.join(mydir,os.path.splitext(i)[0]+correctsuffix)
            os.rename(path,correctpath)

