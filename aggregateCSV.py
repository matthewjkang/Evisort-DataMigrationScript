import pandas as pd
from ziphandler import *
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

mergelist = []
for i in os.listdir('CSVs'):
    csv = pd.read_csv(
        os.path.join('CSVs',i)
    )
    if ("InternalId" in csv.columns) and ('Title' in csv.columns) and ('Location' in csv.columns):
        mergelist.append(i)

combined_csv = pd.concat( [ pd.read_csv(os.path.join('CSVs',f)) for f in mergelist ] )

combined_csv.to_csv( "combined_csv.csv", index=False )
