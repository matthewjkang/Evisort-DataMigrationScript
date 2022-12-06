from ziphandler import *

if __name__ == '__main__':
    unpack_zip(find_zipfile())
    move_csv()
    move_pdf()
    print(len(os.listdir('CSVs')))