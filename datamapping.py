"""
Problem : Some CSV's contain {DocName : PdfName} with same PdfName's. 
EX : "Signed Agreement 1.pdf" appears multiple times throughout different CSV's
      Doc3744174762 : Signed_Contract Documents.pdf
      Doc3374435585 : Signed_Contract Documents.pdf
      
Solution 1 : Just add a counter variable to each duplicated name. 
"Signed_Contract Documents.pdf" and "Signed_Contract Documentsv2.pdf"

Solution 2 : Find the CW name to each PdfName, and append that the front of each duplicated name.
"Sutherland Global Signed_Contract Documents.pdf" and "MarketStar QOZ Business LLC Signed_Contract Documents.pdf"


"""

import os
import pandas as pd

#x = os.path.join('CSVs',os.listdir('CSVs')[0])

mylist = []
for i in os.listdir('CSVs'):
    x = pd.read_csv(
        os.path.join('CSVs',i)
        )

    if ('Title' in x.columns) and ('Location' in x.columns):
        mylist += x['InternalId'].tolist()

print(len(mylist))
print(len(set(mylist)))