import pandas as pd
from pandas import ExcelWriter

#create database
data = {
    "FirstName": ["Satvik", "Avinash", "Lahri"],
    "LastName": ["Shah", "Kati", "Rath"],
    "Email": ["satshah@example.com", "avinashk@example.com", "lahri.rath@example.com"],
    "PhoneNumber": ["4537829158", "5892184058", "4528727830"]
}

#convert dataset to a dataframe
df = pd.DataFrame(data)


#create the ExcelWrite object
write = ExcelWriter("resource/emp.xlsx")
#write data to excel file
df.to_excel(write,sheet_name="Sheet1",index=False)
#save and close  excel file
write.close()

	
# Import pandas
import pandas
	
# Read data from Excel sheet
dataframe = pandas.read_excel('resource/emp.xlsx')
 
# Print the dataframe
print(dataframe)
 
# Print the number of rows and columns
print("====================================")
print("Number of rows and columns:", dataframe.shape)
 
# Print the data in the emails column only
print("====================================")
print("Emails:")
print(dataframe['Email'])
 
# Sort the data based on FirstName in ascending order and print the data
print("====================================")
print("Sorted data:")
print(dataframe.sort_values('FirstName'))