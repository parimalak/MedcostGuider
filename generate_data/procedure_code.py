
import pandas as pd
import numpy as np
import glob

path = r'/data/'
filenames = glob.glob(path + "/cptMedical*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in filenames:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_,ignore_index=True)    

frame.columns=frame.columns.astype(str).str.lower().str.replace(' ','')

proc = frame[['proccode','proceduredescription','inpout','maxrate', 'effdate','pcrate']]
proc['effdate'] =proc['effdate'].replace(r'\s+', np.nan, regex=True)
proc = proc.dropna()

proc['proccode'] = proc.proccode.astype('category')
proc['proceduredescription'] = proc.proceduredescription.astype('category')
proc['inpout'] = proc.inpout.astype('category')



proc.maxrate =pd.to_numeric(proc.maxrate,errors = 'coerce')
proc.pcrate =pd.to_numeric(proc.pcrate,errors = 'coerce')
proc.maxrate.fillna(proc.maxrate.mean())
proc.pcrate.fillna(proc.pcrate.mean())

proc['rate']=proc[['pcrate','maxrate']].max(axis=1)

del proc['maxrate']
del proc['pcrate']

#extracting only year from date
proc['year'] = pd.DatetimeIndex(proc['effdate']).year

#Grouping years to 4 bins
proc['status'] = pd.cut(proc['year'],bins=4,labels=False)
labels = np.array('2014 2015 2016 2017'.split())

#labels = {0:2014,1:2015,2:2016,3:2017}
proc['status'] = labels[proc['status']]
proc['status'] =proc.status.astype('int')
#adjusting rates based on years
proc['rate'] = proc['rate'] + (proc['status']-proc['year'])*0.1
del proc['year']
del proc['effdate']
proc.rename(columns ={'status':'year'},inplace = True)
proc.to_csv(path+'proccode.csv',header = True,index = False)
