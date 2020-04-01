# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 
@author: Vishal
"""

import matplotlib.pyplot as plt
import pandas as pd

"""
Expected json Data format
"""
data={
    "productdata":
        {
    "product": [1,2,3,4,5,6,7,8],#this data is product VS sales 
     "sales": [1,2,3,4,5,6,7,8],
        },
    "Agedata":{
            "age":[1,2,3,4,5,6],#this data is age of people who enter to buy goods
              },
    "Saleswrtage":
              {
            #Sales with respect to age
            "sales2":[1,2,3,4,5,5],
            "age":[1,2,3,4,5,6]
              }
    
    }
#data1=json.dumps(data, indent=4)
#print(data)

df = pd.DataFrame(data['productdata'])
df.plot(kind='bar',x='product', y='sales')
plt.savefig('output1.png')

df = pd.DataFrame(data['Agedata'])
df.plot(kind='pie',x='False',y='age')
plt.savefig('output2.png')

df = pd.DataFrame(data['Saleswrtage'])
df.plot(kind='pie',x='age',y='sales2')
plt.savefig('output3.png')




