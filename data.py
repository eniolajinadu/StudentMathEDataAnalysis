#!/usr/bin/env python3

import matplotlib.pyplot as mat #for data visualization, i.e., to plot graphs, charts etc.
import pandas as pd #for data manipulation
import numpy as np #for numerical operations
import chardet #to detect what encoding of a file, in this case, the ".csv" file

with open('/home/eniolajinadu/GitHub/PLP-Projects/Python/week7/MathE dataset.csv', 'rb') as file: 
    raw_data = file.read()
    result = chardet.detect(raw_data) # to detect the encoding of the file
    encoding = result['encoding']
print(encoding) #prints out the encoding of the file

df = pd.read_csv('/home/eniolajinadu/GitHub/PLP-Projects/Python/week7/MathE dataset.csv', encoding=encoding, delimiter=';')
print(df.head(6)) #to display the first 6 lines of the dataset
print(df.info()) #to display the summary of the dataset
print(df.describe()) #to get a summary of the dataset
print(df.isnull().sum()) #to check for missing values in the dataset

df_keyword = df['Keywords'].str.contains(r'\bsample\b', case = False, na = False).sum()
print(f'Number of entries with "sample": {df_keyword}') #to count the number of entries with "sample"

df_grouped = df.groupby('Topic').agg({'Student Country':'count', 'Question ID':'count'})
print(df_grouped)

mat.plot(df['Student Country'], df['Topic'])
mat.xlabel ('Topic')
mat.ylabel('Student Country')
mat.title('Student Country vs Topic')
mat.show

mat.hist(df['Student Country'], bins=10, edgecolor='black')
mat.xlabel('Student Country')
mat.ylabel('Frequency')
mat.title('Histogram of Student Country')
mat.show()