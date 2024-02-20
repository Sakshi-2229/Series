# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 01:35:18 2023

@author: sai
"""

#write a pandas program to create and display a one-dimensional array-like
#containing an array of data.

import pandas as pd
ds=pd.Series([2,4,6,8,10])
print(ds)

#####################################################################

#write a pandas program to convert a panda module Series
#to python list and its type.
#IMP

import pandas as pd
ds=pd.Series([2,4,6,8,10])
print("Pandas Series and type")
print(ds)
print(type(ds))
print("Convert Pandas Series to Python List")
print(ds.tolist())
print(type(ds.tolist()))

########################################################################

#write a pandas program to add, subtract, multiple and divide series

import pandas as pd
ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,9])
ds = ds1 + ds2
print("Add two Series:")
print(ds)
print("Subtract two series:")
ds = ds1 - ds2
print(ds)
print("Multiply two series:")
ds = ds1 * ds2
print(ds)
print("Divide two Series:")
ds = ds1 / ds2
print(ds)

###############################################################

# write a pandas program to compare the elements of the series

ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,10])
print("Series1:")
print(ds1)
print("Series2:")
print(ds2)
print("Compare the elements of the said series:")
print("Equals:")
print(ds1 == ds2)
print('Greater than:')
print(ds1 > ds2)
print('Less then:')
print(ds1 < ds2)

#################################################################

#Write pandas program to convert a dictionary to a pandas series

d1 = {'a':100,'b':200,'c':300,'d':400,'e':500}
print("Original Dictionary:")
print(d1)
new_series = pd.Series(d1)
print("Converted Series:")
print(new_series)

####################################################################

#Write pandas program to convert numpy array to a pandas series

import numpy as np
import pandas as pd
n_a=np.array([10,20,30,40,50])
print("Numpy array:")
print(n_a)
new_series=pd.Series(n_a)
print("Converted Pandas Series: ")
print(new_series)

####################################################################

#Write pandas program to change data types of given column or series

s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original data Series:")
print(s1)
print("Change the said data to numeric:")
s2 = pd.to_numeric(s1, errors='coerce') #It will replace all non-numeric values 
                                        #with NaN.
print(s2)

######################################################################

#write a pandas program to convert
#first column of dataframe as a series

#iloc - used for index    [index]
#loc - used for name      [column_name]

d = {'col1': [1,2,3,4,5,6], 'col2': [2,3,4,5,6,7], 'col3': [2,4,5,7,8,3]}
df = pd.DataFrame(data=d)
print("Original DataFrame:")
print(df)
s1=df.iloc[:,0]         #all rows and 0th column
print("\n1st Column of a Series:")
print(s1)
print(type(s1))

######################################################################

s = pd.Series([['Red', 'Green', 'White'],['Red', 'Black'], ['Yellow']])
print("Original Series of list:")
print(s)
'''
Output
0    [Red, Green, White]
1           [Red, Black]
2               [Yellow]
'''
#transform a wide-format DataFrame with nested lists into a long-format Series.
s=s.apply(pd.Series).stack().reset_index(drop=True)
print("One Series:")
print(s)
'''
Output
0       Red
1     Green
2     White
3       Red
4     Black
5    Yellow
'''


#Another way
s = pd.Series([['Red', 'Green', 'White'],['Red', 'Black'], ['Yellow']])
print("Original Series of list:")
print(s)
s=s.apply(pd.Series) 
s=s.stack() 
s=s.reset_index(drop=True)
print("One Series:")
print(s)

##################################################################
#Write pandas program to add some data to existing series


s = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original data Series:")
print(s)
print("\nData series after adding some data:")
new_s=pd.concat([s, pd.Series([500, "php"])], ignore_index=True)
print(new_s)

##########################################################################

# write pandas program to sort the given series.

s = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original data Series:")
print(s)
new_s=pd.Series(s).sort_values()    #by default it is ascending order sorting
print(new_s)


############################################################################

#write a pandas program to change the order of index of given series

s=pd.Series(data=[1,2,3,4,5], index = ['A', 'B', 'C', 'D', 'E'])
print("Original Data Series:")
print(s)
s=s.reindex(index=['B', 'A', 'C', 'D', 'E'])
print("Data series after the order of index:")
print(s)

#####################################################################
























