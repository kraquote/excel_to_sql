# **Excel Converter**
## This python script can convert Excel file to **sql importable** file.
## **Depencies and function**
> Depencies : - pip show pandas

> Charset: UTF-8


| Function        | Params           | Utility  |
| :---------------: |:----------------:| :--------:|
| getarray()       | None | This function request you with wich array you want to work. |
| read_excel()        | name => str format | This function gives you the different lines (index : **0**, *numpy array*), the number of lines (index: **1**), the different columns (index: **2**) and the number of columns (index: **3**).|
| generate_sql()   | **tbl** => all lines of your array, **n_tbl** => number of lines in your array, **col** => all columns of your array, **n_col** => number of columns, **name** => name for your sql file      | This function create a file in the folder ***"sql"***, this file is importable in database.|
| drop() | None | This function gives you the possibilities to delete a file. |

## **Examples**
### Setup all fucntion
```python
import reader as rd 

name = rd.getarray()
array = rd.read_excel(name)
rd.generate_sql(array[0], array[1],array[2],array[3], "name_of_sql_file")
rd.drop()
```
### **Depencies**
```python
pip show pandas
```
### Results in console
```
Name: pandas
Version: 1.5.1
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: https://pandas.pydata.org
Author: The Pandas Development Team
Author-email: pandas-dev@python.org
License: BSD-3-Clause
Location: c:\users\axdeb\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages
Requires: numpy, python-dateutil, pytz
Required-by: xarrayfolder) 
``` 

### **GetArray**
```python
name = rd.getarray()
```
### Result in console
```
> Excel name, extension is required ?(Check if the array is on the right folder) 
``` 
### **Read_Excel**
```python
array = rd.read_excel(name)
```
### Return
```
[tbl, n_tbl, col, n_col] 
``` 
### **Generate_sql**
```python
rd.generate_sql(array[0], array[1],array[2],array[3], "name_of_sql_file")
```
### Result in console
```
> SQL File Name (Extension didn't require): 
> The file was perfectly create !
``` 
### **Drop**
```python
rd.drop()
```
### Result in console
```
>   Wich file you want to delete (Extension Required): 
>  "File yourfile.ex deleted."
``` 
## **Error**
