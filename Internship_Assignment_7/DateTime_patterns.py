import numpy as np
import pandas as pd

df = pd.DataFrame({
    'StudentID': ['ESK001', 'ESK002', 'ESK003', 'ESK004', 'ESK005', 'ESK006'],
    'Name': ['Akash', 'Bhumi', 'Chandra', 'Diyan', 'Annu', 'Farhan'],
    'EnrollDate_': ['15-08-2023', '01-17-2022', '28-02-2024', '30/06/2023', '01-13-2024', '25-04-2025'],
    'Score': [85, 72, 91, 65, 78, 88]})
print('Student DataFrame ->')
print(df.to_string())
print()

print('Convert to Datetime Objects -->')
df['Converted_Dates'] = pd.to_datetime(df['EnrollDate_'], format = '%d-%m-%Y', errors='coerce')
print(df[['EnrollDate_', 'Converted_Dates']])
print()
print('Invalid Dates -->')
print(df[df['Converted_Dates'].isna()][['Name', 'EnrollDate_']])
print()

print('Date Components -->')
df['Enroll_Year'] = df['Converted_Dates'].dt.year
df['Enroll_Month'] = df['Converted_Dates'].dt.month
df['Enroll_Day'] = df['Converted_Dates'].dt.day
df['Enroll_DayName'] = df['Converted_Dates'].dt.day_name()
print(df[['Converted_Dates', 'Enroll_Year', 'Enroll_Month', 'Enroll_Day', 'Enroll_DayName']])
print()

print('Sorting by Date -->')
sort_by_date = df.sort_values(by = 'Converted_Dates', ascending = True)
print(sort_by_date[['Name', 'Converted_Dates']])
print()

print('Final DataFrame -->')
print(df.to_string())
