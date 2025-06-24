import pandas as pd

print('Creating a DataFrame from a two-dimensional Python list (Also Known As List of Lists) ->')
lis_2d = [[1, 'A', 11.11],
          [2, 'B', 22.22],
          [3, 'C', 33.33],
          [4, 'D', 44.44]]
data_lis_2d = pd.DataFrame(lis_2d, columns=['ID', 'Names', 'Marks'], index=['i','ii','iii','iv'])
print(data_lis_2d)

print()
print('Creating a DataFrame from a dictionary ->')
dict2 = {'Name': ['Alar', 'Bhar', 'Char'],
        'Age': [25, 30, 35],
        'City': ['Ajmer', 'Jaipur', 'Alvar']}
data_dict = pd.DataFrame(dict2, index=[1,2,3])
print(data_dict)

print()
print('Creating a DataFrame using list of tuples ->')
tup = [('Abhi', 'Shar', 6),
       ('Chandra', 'Jai', 7),
       ('Divyan', 'Kha' , 8),
       ]
data_tup = pd.DataFrame(tup, columns=['FirstName', 'LastName', 'Class'], index=['I', 'II', 'III'])
print(data_tup)

print()
print('Creating a DataFrame using list of dictionaries ->')
dict_in_dict = [{'Name': 'Ale', 'Score': 85, 'Grade': 'B'},
                {'Name': 'Bhumi', 'Score': 92, 'Grade': 'A'},
                {'Name': 'Chan', 'Score': 78, 'Grade': 'C'}]
data_dict_in_dict = pd.DataFrame(dict_in_dict)
print(data_dict_in_dict)

print()
print('Iterating Over Rows ->')
data = {
    'Student_ID': [101, 102, 103, 104, 105, 106, 107],
    'Name': ['Ale', 'Bhumi', 'Chan', 'Divyan', 'Emma', 'Fatema', 'Gautam'],
    'Age': [20, 22, 21, 23, 20, 22, 21],
    'Subject': ['CS', 'Math', 'Physics', 'CS', 'Math', 'Physics', 'CS'],
    'Score': [85, 90, 78, 92, 88, 75, 95]
}
df_data = pd.DataFrame(data)
print(df_data)
print('Using iterrows() ->')
for i, r in df_data.iterrows():
    print(f'Index: {i}; Name: {r['Name']}; Subject: {r['Subject']}; Score: {r['Score']}')
print()
print('Using itertuples() ->')
for ro in df_data.itertuples():
    print(f'ID: {ro.Student_ID}; Score: {ro.Score}')
print()
print('Using items() ->')
for col1, col2 in df_data.items():
    print(f'{col1} : \n{col2}')

print()
print('Selecting Rows Based on Conditions ->')
print('Students older than 20 --> ')
sel = df_data[df_data['Age'] > 20]
print(sel)
print('Students of CS with Scores higher than 85 -->')
sel2 = df_data[(df_data['Subject'] == 'CS') & (df_data['Score'] > 85)]
print(sel2)

print()
print('Selecting a Row Using .iloc[] ->')
print('Only One Row -->')
sel_row = df_data.iloc[0]
print(sel_row)
print('Multiple Rows -->')
sel_rows = df_data.iloc[[0, -1]]
print(sel_rows)

print()
print('Limited Rows Selection with Specific Column ->')
print('Multiple Rows And One Column -->')
sel_rsc = df_data.iloc[:2, df_data.columns.get_loc('Name')]
print(sel_rsc)
print('Multiple Rows And Multiple Columns -->')
sel_rscs = df_data.iloc[:3][['Name', 'Score']]
print(sel_rscs)

print()
print('Dropping Rows Based on Condition ->')
print('Removing Students With "Physics" -->')
drop_rs = df_data[df_data['Subject'] == 'Physics']
print(drop_rs)

print()
print('Inserting a Row at a Given Position ->')
print('Original DataFrame -->')
print(df_data)
print('Inserting Between Index 2 And 3 -->')
new_ro = {'Student_ID': 107, 'Name': 'NewStu', 'Age': 21,'Subject': 'Physics', 'Score': 77}
new_r = pd.DataFrame([new_ro])
df_data_top = df_data.iloc[:3]
df_data_buttom = df_data.iloc[3:]
new_df_data = pd.concat([df_data_top, new_r, df_data_buttom]).reset_index(drop=True)
print(new_df_data)

print()
print('Creating a List from Rows ->')
list_df_data = df_data.values.tolist()
print(list_df_data)