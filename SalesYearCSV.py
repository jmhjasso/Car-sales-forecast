#import pandas as pd

#Reading the dataset
#cars_data=pd.read_csv(r'C:\Users\jesus.jasso2\ML\ACM LOT012\Datasets\Last 4 years sales Lot 012.csv')

#changing the SaleDate field from Object to DateTime format
#cars_data['SaleDate']= pd.to_datetime(cars_data['SaleDate'])

#InitDate=cars_data['SaleDate'].min()
#LateDate=cars_data['SaleDate'].max()


#Funtion to automatically get sales of make and model by year, 1 csv file created per year
#def SalesYearFile(InitDate, LateDate):
    
InitYear=InitDate.year
LatestYear=LateDate.year
    #Loop to automatically separate data year by year
while InitYear <= LatestYear:
        Firstday='1/1/'+str(InitYear)
        LastDay='12/31/'+str(InitYear)
            
        #separating by specific year data from the original dataset
        cd=cars_data[cars_data['SaleDate'].between(Firstday, LastDay) ]
                
        #Removing repossessions and returns
        cd = cd[~cd['Account_Status'].isin(['Repossessed','Returned'])]
               
        #Adding a 1 to each column to get the total sum
        SoldYear=str(InitYear)+'Sold'
        cd.insert(2, SoldYear, 1)
               
        #let's find out the summary of  make, model by year
        cd=cd.groupby(['Make', 'Model', ]).count()[SoldYear]
                
        #Saving the summary in a csv file
        PathDescr="C:/Users/jesus.jasso2/ML/ACM LOT012/Datasets/"
        TempName= SoldYear + "Sales Lot 012.csv"
        PathFile = PathDescr + TempName
        cd.to_csv(PathFile)     
        print(str(SoldYear+'Sales Lot 012.csv file created'))        
        #Let's go to the next year
        InitYear+=1
        
print("Files Created")
