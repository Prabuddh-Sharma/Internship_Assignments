import pandas as pd
import numpy as np
import re

print('Data Analysis of Student Performance Data -->')
print("Loading data from 'student_data.csv'...\n")

filepath = 'C:\\Users\\prabu\\Desktop\\Jupyter Files\\Data_Files\\student_data.csv'
try:
    df = pd.read_csv(filepath)
    print('CSV loaded successfully. First 5 rows:')
    print(df.head().to_string())
    print(f'\nDataFrame shape: {df.shape}')
    print(f'Column data types:\n{df.info()}')
except FileNotFoundError:
    print('Error: "student_data.csv" not found.')
    exit()
print()

print('Data Type Conversion and Data Cleaning -->')
df['EnrollmentDate'] = pd.to_datetime(df['EnrollmentDate'], format='%d-%m-%Y', errors='coerce')
print("\n'EnrollmentDate' converted to datetime.")

df['GPA'] = pd.to_numeric(df['GPA'], errors='coerce')
df['StudyHours_Weekly'] = pd.to_numeric(df['StudyHours_Weekly'], errors='coerce')

df['Attendance_Percentage'] = df['Attendance_Percentage'].astype(str).str.replace('%', '', regex=False)
df['Attendance_Percentage'] = pd.to_numeric(df['Attendance_Percentage'], errors='coerce')

print(f"\nDataFrame info after type conversions:\n{df.info()}")
print()

print("Data Cleaning with Regex and String Methods -->")

df['Name_Cleaned'] = df['Name'].str.replace(r'\s+', ' ', regex=True).str.strip()

email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
df['Email_Valid'] = df['Email'].str.match(email_pattern, na=False)
print("\n'Email' addresses validated.")

mobile_pattern = r"^[6-9][0-9]{9}$"
df['Mobile_Valid'] = df['Mobile'].astype(str).str.match(mobile_pattern, na=False)
print("'Mobile' numbers validated.")
print()

print("Handling Missing and Invalid Data -->")

df.loc[df['Email_Valid'] == False, 'Email'] = np.nan
print("Invalid Emails replaced with NaN.")

df.loc[df['Mobile_Valid'] == False, 'Mobile'] = np.nan
print("Invalid Mobile Numbers replaced with NaN.")
print()

mean_gpa = df['GPA'].mean()
df['GPA_Filled'] = df['GPA'].fillna(mean_gpa).round(2)
print(f"Missing GPA values imputed with mean GPA ({mean_gpa:.2f}).")

# Impute missing StudyHours_Weekly with median
median_study_hours = df['StudyHours_Weekly'].median()
df['StudyHours_Filled'] = df['StudyHours_Weekly'].fillna(median_study_hours)
print(f"Missing StudyHours_Weekly values imputed with median ({median_study_hours}).")

# Impute missing Attendance_Percentage with mean
mean_attendance = df['Attendance_Percentage'].mean()
df['Attendance_Filled'] = df['Attendance_Percentage'].fillna(mean_attendance).round(1)
print(f"Missing Attendance_Percentage values imputed with mean ({mean_attendance:.1f}).")

print(f"\nDataFrame info after handling missing values:\n{df.info()}")
print()

print("Final Cleaned and Processed DataFrame ->>")
print(df.head(10).to_string())
print(f"\nFinal DataFrame shape: {df.shape}")
print()
print(f"Final DataFrame info:\n{df.info()}")