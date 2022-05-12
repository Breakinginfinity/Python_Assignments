
"""
Created on Sun Apr 21 10:16:34 2022

@author: Aman.Verma
"""


##########################################################################################
#------------------------------------Pandas In Python-------------------------------------#
##########################################################################################

import pandas as pd
import numpy as np
import os

#Setting the working directory

os.chdir(R'C:\Users\dell\Documents\PYTHON_SCRIPTS\PANDAS')

path_data = os.getcwd()
print(path_data)
#Master_Path
path_data= R'C:\Users\dell\Documents\PYTHON_SCRIPTS\PANDAS'
print(path_data)


#Branch_Path
input_path = os.path.join(path_data,"input")#Sub Folder1 
output_path = os.path.join(path_data,"output")#Sub Folder 2


#------------------------------------------CSV---------------------------------------#
print(os.cwd)
employee_df = pd.read_csv(os.path.join(input_path,"employees.csv"))
GoogleData = pd.read_csv("Googleplaystore_1.csv")

##########################################################################################
#3.Viewing Data
##########################################################################################

#Head of Data
GoogleData.head()

First_100=GoogleData.head(100)

#Tail of Data
GoogleData.tail()
Last_10=GoogleData.tail(10)


#Viewing the Columns of Data
GoogleData.columns

#Checking the Structure of Data
GoogleData.dtypes


# Print the info of Data
print(GoogleData.info())


#Summary of the Data
Des=GoogleData.describe()


#Including all the Data Levels
Des_all=GoogleData.describe(include='all')


#GoogleData_1 = GoogleData[(GoogleData.Category == "FAMILY")]

# Print the shape of Data
print(GoogleData.shape)



##########################################################################################
#4.Changing the type of data
##########################################################################################

#Converting a coloumn to a particular Data Type
pd.to_numeric(GoogleData.Rating)

#Multiple Columns
GoogleData_1=GoogleData.copy()
GoogleData_1.dtypes

#Univariate changes
GoogleData_1["Rating"] = GoogleData_1["Rating"].apply(str)
GoogleData_1["Rating"] = GoogleData_1["Rating"].apply(float)

#Multivariate changes

GoogleData_1[["Rating","Reviews"]] = GoogleData_1[["Rating","Reviews"]].apply(str)#Making same changes across columns
GoogleData_1 = GoogleData_1.astype({"Rating":'str',"Reviews":'float'})#Making different changes across columns
GoogleData_1.dtypes


##########################################################################################
#5.Selecting the Data
##########################################################################################


#Selecting only one Column 
GoogleData1= GoogleData['App']
GoogleData1= GoogleData[['App','Rating','Reviews','Category']]
GoogleData1= GoogleData.App

#Selecting only Multiple Columns

col_list = ['App','Category','Rating','Reviews']
GoogleData2= GoogleData[col_list]

#Based on Labels
GoogleData2= GoogleData.loc[:,'App']# All Rows

GoogleDat2= GoogleData.loc[200:300,['App','Size','Reviews']]
GoogleDat2.shape

#Based on Index
GoogleData2= GoogleData.iloc[:,[2,3,10]]

#Selecting Multiple Rows
GoogleData2= GoogleData.iloc[0:3,:]
GoogleData2_iloc= GoogleData.iloc[0:3,3:10]
GoogleData2_loc = GoogleData.loc[0:3,['App','Size']]

##########################################################################################
#6. Filtering the Data
##########################################################################################

GoogleData3 = GoogleData[GoogleData.Rating == 3].reset_index(drop=True)

GoogleData3 = GoogleData[GoogleData.Rating == 3]


GoogleData3 = GoogleData[GoogleData['Rating'] > 3]


#AND
GoogleData4 = GoogleData[(GoogleData.Rating > 3) & (GoogleData.Reviews > 10000 )].reset_index(drop=True)

#OR
GoogleData5 = GoogleData[(GoogleData.Rating > 3) | (GoogleData.Reviews > 10000 ) ]


#AND & OR
GoogleData5 = GoogleData[((GoogleData.Rating > 3) & (GoogleData.Reviews > 10000 )) | (GoogleData.Category == "ART_AND_DESIGN")]


GoogleData6 = GoogleData[GoogleData['Category'].isin(["ART_AND_DESIGN","HEALTH_AND_FITNESS"])]

#NOT
GoogleData4 = GoogleData[(GoogleData.Rating > 3) & ~(GoogleData.Reviews > 10000 )]

#MULITPLE NOT
GoogleData4 = GoogleData[~(GoogleData.Rating ==3) & ~(GoogleData.Reviews > 10000 )]
GoogleData4.to_csv(os.path.join(output_path,"Processed_Google_Data.csv"),index=False)

##########################################################################################
#7. Working with Missing Data
##########################################################################################

#pandas primarily uses the value np.nan to represent missing data

#Finding the columns with Missing Values
Miss = GoogleData.isnull().sum()
Miss_df = pd.DataFrame({'Missing_Value_Count':GoogleData.isnull().sum()}).reset_index()


#Total Sum of Missing Values
GoogleData.isnull().sum().sum()

#Imputing Missing values withe particular value
GoogleData7=GoogleData.fillna(value=0)
Miss = print(GoogleData7.isnull().sum())

#Working with particular columns
GoogleData7=GoogleData.copy()
GoogleData7['index']=GoogleData7.index
GoogleData7['Rating'] = GoogleData7['Rating'].fillna((GoogleData7['Rating'].mean()))

#Filtering based on odd rows
GoogleData7_odd = GoogleData7[::3]#N-1
GoogleData7_odd = GoogleData7[::2]

#Filterinf based on even rows
GoogleData7_even = GoogleData7[1::2]

#Append two data frames in Pandas
GoogleData8=GoogleData7.head(10).append(GoogleData7.tail(10)).reset_index(drop=True)
GoogleData8=GoogleData7.head(10).append([GoogleData7.tail(10),GoogleData7.tail(2)])
##########################################################################################
#8. Stats for the Variables
##########################################################################################

from dataprep.eda import create_report
WHO = pd.read_csv("WHO.csv")
df=WHO.copy()

StatWHO=WHO.describe()

WHO.columns

WHO.info()
WHO.dtypes
WHO.Population.mean() #Average
WHO['Population'].mean() 
WHO[['Population','Under15']].mean() 
WHO.Population.median() #Median, 50%
WHO.Population.sum() # Sum
WHO.Population.std() # Standard Deviation
WHO.Population.var() #Variance
WHO.Population.count() # Non Null

##########################################################################################
#9. Merging for the Variables
##########################################################################################
#pandas has full-featured, high performance in-memory join operations idiomatically very similar to relational databases like SQL.

#Merge Methods
#left=Use keys from left frame only
#right=Use keys from right frame only
#outer=Use union of keys from both frames
#inner=Use intersection of keys from both frames


left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})


right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})


center = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K5'],
                      'G': ['C0', 'C1', 'C4', 'C5'],
                       'H': ['D0', 'D1', 'D4', 'D5']})



result = pd.merge(right,left, on='key')#Default Join in Pandas is inner Join



#Based on Different Key Name
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

result = pd.merge(right, left, on=['key1', 'key2'])

result1=pd.merge(left,right,how='left',on=['key1','key2'])
result2=pd.merge(left,right,how='right',on=['key1','key2'])
result3=pd.merge(left,right,how='outer',on=['key1','key2'])
result4=pd.merge(left,right,how='inner',on=['key1','key2'])


# =============================================================================
# Chain Merge
# =============================================================================

#With Chain Merge
new_df = left.merge(right, on = ['key']).merge(center, on = ['key'], how = 'left')

#Without Chain Merge
new_df1 = pd.merge(left,right, on = ['key'])
new_df2 = pd.merge(new_df1,center, on = ['key'],how='left')



##########################################################################################
#10. Grouping the Variables
##########################################################################################


#1 groupby
df=WHO.copy()
df2= df.groupby(['Region']).sum().reset_index()

df2= df.groupby(['Region']).mean().reset_index()

#Multiple Groups
df3= df.groupby(['Country','Region']).sum().reset_index()

#Multiple variables and Multiple Measures:
df4 = df.groupby(['Region']).agg({'Population':'sum',
                                  'Under15':'mean'}).reset_index()

df4 = df4.rename(columns={'Population':'Population_sum','Under15':'Under15_mean'})


#Sumif/Countif/Average if
df['Total_Region_Pop']=df.groupby(['Region'])['Population'].transform('sum')

df['Region_Pop']= df['Population']/df['Total_Region_Pop']

##########################################################################################
#11. Pivot Tables
##########################################################################################


#Reshaping
All_Region = WHO[['Country','Region','Population']]
#Europe = Europe[Europe.Region == "Europe"]

All_Region_1=All_Region.pivot(index='Region', columns='Country', values='Population').reset_index()

All_Region_1=All_Region_1.fillna(value=0)


#If the values argument is omitted, and the input DataFrame has more than one column of values which are not used as column or index inputs to pivot, then the resulting “pivoted” DataFrame will have hierarchical columns whose topmost level indicates the respective value column

#Melt
All_Region_2=All_Region_1.melt(id_vars=['Region'],var_name='Country_Name')
All_Region_2=All_Region_2[All_Region_2.value>0].reset_index(drop=True)
All_Region_2= All_Region_2.rename(columns = {"value":"Population"})


#Finding Summary Statistics for One Variable
Agg_1 = WHO.groupby('Region').agg({"Population": [min, max, sum, np.median,np.mean,np.var,np.std]}).reset_index() 
Agg_1 = WHO.groupby('Region').agg({"Population": ['min','max','sum','median','mean','std']}).reset_index() 


Stats = WHO.describe()
#Finding Summary Statistics for More than One Variable
Agg_2=pd.pivot_table(WHO, values=['Population','Under15'], index=['Region'], 
                     aggfunc={'Population':[np.mean,np.min,np.max],
                      'Under15':[np.mean,np.min]}).reset_index()

Agg_2=pd.pivot_table(WHO, values=['Population','Under15'], index=['Region'], 
                     aggfunc={'Population':['mean','max'],
                      'Under15':['mean','min']}).reset_index()

# =============================================================================
# Dropping Duplicates
# =============================================================================



#Subset takes a column or list of column label.
  
#keep: keep is to control how to consider duplicate value. It has only three distinct value and default is ‘first’.

#If ‘first’, it considers first value as unique and rest of the same values as duplicate.
#If ‘last’, it considers last value as unique and rest of the same values as duplicate.
#If False, it consider all of the same values as duplicates

#inplace: Boolean values, removes rows with duplicates if True.

#Return type: DataFrame with removed duplicate rows depending on Arguments passed
# dropping ALL duplicte values 
data_1.drop_duplicates(subset =["First Name","Gender"],
                     keep = 'first', inplace = True) 

cols_name = ['First Name', 'Gender', 'Start Date', 'Last Login Time', 'Salary']

data_duplicates=data_1.duplicated(subset = cols_name)
data_1.columns

data_duplicates= pd.concat([data_1,data_duplicates],axis=1)

# =============================================================================
# Sorting Values
# =============================================================================

# making data frame from csv file 
data = pd.read_csv("employees.csv") 
data_1 = data.copy()

# sorting by first name 
#1st Way
data_2 = data_1.sort_values("First Name",inplace = False, ascending = True).reset_index(drop=True)
#2nd Way
data_1.sort_values("First Name",inplace = True, ascending = True)
data_1= data_1.reset_index(drop=True)
                           
data_1.sort_values(["First Name","Salary"],inplace = True, ascending = [True,False]) 

# =============================================================================
# Control Structures
# =============================================================================

# =============================================================================
# If-Else
# =============================================================================
data2 = pd.read_csv("New_Employee.csv") 
data2.Age
data2['Age']
 
def Age_cat(y):
    if y>=20 and y<25 :
        return 'Between 20-25'
    elif y>=25 and y<30 :
        return 'Between 26-30'
    else:
        return 'Above 30'

#bucketting rating to a new column         
data2['Age_Cat'] = data2['Age'].apply(Age_cat)


# =============================================================================
# Sets
#A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements. 
#Python’s set class represents the mathematical notion of a set. 
#The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. 
#This is based on a data structure known as a hash table. Since sets are unordered, we cannot access items using indexes like we do in lists.
# =============================================================================

s1 = {1,2,3,4}
type(s1)

s1 = {1,1,1,1,1,4,1000}
s1

s1[0]

s1.add(4) # can't add a pre-existing element
s1

a = set([1,2,3,4,5]) # Superset
b = set([1,2,3]) #Subset


#Operations
# If all elements of b exist in a , then b is called a subset of a
# If all elemnts of b exists in a  , then a is called superset of b

b.issubset(a)
a.issuperset(b)

a.union(b)
a.update(b)
a.intersection(b)
a.difference(b)
b.difference(a)


s1 = set([1,2,3])
s1.remove(2)

# =============================================================================
# For - Loop 
# =============================================================================

# Iterating over a list 
print("List Iteration") 
l = ["Data Science", "is a ", "Great Subject!"] 
len(l)
l[0]
type(l)

for i in l: 
    #i=l[0]
    print(i) 
       
# Iterating over a tuple (immutable) 
print("/nTuple Iteration") 
t = ("Data Science", "is a ", "Great Subject!") 
for i in t: 
    print(i) 
       
# Iterating over a String 
print("/nString Iteration")     
s = "Data"
for i in s : 
    print(i) 
       
# Iterating over dictionary 
print("/nDictionary Iteration")    
d = dict()  
d['xyz'] = 123
d['abc'] = 345
for i in d :
    #print(i)
    print("%s-->%d" %(i, d[i]))
    
for i in d :
    #print(i)
    print(str(i) +"-->"+ str(d[i]))#same as line 538
     #print(i, d[i])# i = key, d[i]= value of the key

d['xyz']
# Nested For Loops
for i in range(1, 6): 
    #i=3
    for j in range(i): 
        #j=1
        print(i, end=' ') 
        i+=1
    print() 
    
    
y=range(1, 6)
len(y)

