import pandas as pd
import numpy as np

df = pd.DataFrame({
    'StudentID': ['ESK001', 'ESK002', 'ESK003', 'ESK004'],
    'Name': ['Akash Sharma', 'Bhumi Jain', 'Chandra Bhanu', 'Diyan Purohit'],
    'Email': ['akash@gmail.com', 'bhumi.j@gmail.org', 'invalid-email', None],
    'Mobile': ['9876543210', '1234567890', '998877665', None],
    'EnrollmentDate': ['15-08-2023', '30/06/2023', '01-13-2024', None],
    'FeedBack': ['Student is very active. ', '   Excellent analytical skills.', 'Very  polite student.', 'Struggles with deadlines.']
})
print("Student DataFrame:")
print(df.to_string())
print()

print('Email Address Validation -->')
email_p = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
df['Email_Valid'] = df['Email'].str.match(email_p, na = False)

print(df[['Name', 'Email', 'Email_Valid']])
print()
print('Invalid Emails ->')
print(df[df['Email_Valid'] == False][['Name', 'Email']])
print()

print('Mobile Number Validation -->')
mobile_p = r"^[6-9][0-9]{9}$"
df['Mobile_Num_Valid'] = df['Mobile'].str.match(mobile_p, na = False)

print(df[['Name', 'Mobile', 'Mobile_Num_Valid']])
print()
print('Invalid Mobile Numbers ->')
print(df[df['Mobile_Num_Valid'] == False][['Name', 'Mobile']])
print()

print('Removing extra spaces -->')
df['Better_Lines'] = df['FeedBack'].str.replace(r"^\s+", ' ', regex = True).str.strip()
print(df[['FeedBack', 'Better_Lines']])
print()

print('Enrollment Date Format Validation -->')
date_p = r"^(0[0-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19|20)\d{2}$"
df['Date_Valid'] = df['EnrollmentDate'].str.match(date_p, na = False)
print(df[['EnrollmentDate', 'Date_Valid']])
print('Invalid Date -->')
print(df[df['Date_Valid'] == False][['Name', 'EnrollmentDate']])
print()

print('Final DataFrame')
print(df.to_string())