#Look READ ME
import reader as rd 

name = rd.getarray()
array = rd.read_excel(name)
rd.generate_sql(array[0], array[1],array[2],array[3], "job")
rd.drop()