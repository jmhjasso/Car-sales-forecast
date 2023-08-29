# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:22:46 2023

@author: jesus.jasso2
"""
import pandas as pd
#Consolidating all the csv files in one master file
import glob
#Define the path where we have the csv file
directory = r'C:\Users\jesus.jasso2\ML\ACM LOT012\Datasets\20*.csv'
#print(directory)
#Get a list of all CSV files in the directory 
allcsv=glob.glob(directory)
print(allcsv)
#Initialize an empty DataFrame
DetSales012 = pd.DataFrame()
DetSales012



#file1=pd.read_csv(r'C:\\Users\\jesus.jasso2\\ML\\ACM LOT012\\Datasets\\2019SoldSales Lot 012.csv')
#file2=pd.read_csv(r'C:\\Users\\jesus.jasso2\\ML\\ACM LOT012\\Datasets\\2020SoldSales Lot 012.csv')
#merged=file1.merge(file2, on=['Make','Model'])
#merged=pd.merge(file1,file2, on=['Make','Model'])
#merged.head(5)

for df in allcsv:
    to_merge=pd.read_csv(df)  
    to_merge.head(5)
    merged=pd.merge(DetSales012,to_merge on=['Make','Model'])
    merged.to_csv(r'C:\Users\jesus.jasso2\ML\ACM LOT012\Datasets\Cons_Sales_Lot012.csv', index=False)
    print(Consolidated Sales lot 012 File created)

