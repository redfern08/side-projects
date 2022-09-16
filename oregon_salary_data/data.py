import pandas as pd
import json
import openpyxl

url = 'https://data.oregon.gov/resource/salary.json' # This is the url the data is gathered from

data = pd.read_json(url)    # Data is being read by the Pandas framework
df = pd.DataFrame(data)     # Put the data in a data frame that is readable to the user
df2 = df.drop_duplicates(keep=False)    # Eliminate duplicates
salary_data = df2.rename(    # Each column is being renamed for easy readability
    columns={
        "fiscal_year": "Fiscal Year",                  
        "agency_title": "Agency Title",                    
        "classification": "Class", 
        "annual_salary": "Annual Salary", 
        "full_part_time": "Full/Part Time",   
        "service_type": "Service Type",   
        "agency": "Agency #"
    }
)
with pd.ExcelWriter("sample_sheet.xlsx", mode='w', engine='openpyxl') as writer:
    salary_data.to_excel(writer)