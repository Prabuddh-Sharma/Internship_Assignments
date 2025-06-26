import pandas as pd

print('Convertion from series of Date-Strings to Timeseries -->')
date_ = [
    "2025-01-22",
    "2025-06-11 10:10:00",
    "June 27, 2025",
    "05/01/2025",
]
print('Date Strings:')
for ds in date_:
    print(ds)

date_series = pd.Series(date_)
time_series = pd.to_datetime(date_series, format='mixed')
print('\nDatetime Series\Time Series:')
print(time_series)


print()
print('Performing Inner Merge on the Common Column -->')

d1 = {'ID': [1, 2, 3, 4],
      'Name': ['Akash', 'Bhumi', 'Chandra', 'Divya'],
      'Age': [25, 30, 35, 28]}
df1 = pd.DataFrame(d1)
print('First DataFrame ->\n', df1)
print()
d2 = {'ID': [3, 4, 5, 6],
      'Subject': ['CS', 'Physics', 'Chemistry', 'Math'],
      'Marks': [22, 33, 44, 50]}
df2 = pd.DataFrame(d2)
print('Second DataFrame ->\n', df2)
print()
merge_ = pd.merge(df1, df2, on='ID', how='inner')
print('Merged DataFrame -->\n', merge_)

print()
print('Perform a Left Join of df1 And df2 on the "ID" Column -->')
left_merge = pd.merge(df1, df2, on='ID', how='left')
print(left_merge)

print()
print('Perform right join using pd.merge() -->')
right_merge = pd.merge(df1, df2, on='ID', how='right')
print("Result of pd.merge() -->\n", right_merge)

print()
print('Perform a join using df.join() based on the index -->')
df1_in = df1.set_index('ID')
df2_in = df2.set_index('ID')
join_ = df1_in.join(df2_in, how='left')
print('Result ->\n', join_)

print()
print('Merging with Multiple Keys -->')
df1['RTU_ID'] = [101, 102, 101, 103]
df2['RTU_ID'] = [101, 103, 104, 105]
mkey_merge = pd.merge(df1, df2, on=['ID', 'RTU_ID'], how='inner')
print('Resule -->\n', mkey_merge)

print()
print('Concatenate Three DataFrames -->')
df3 = pd.DataFrame({'ID': [1, 2, 3],
      'Name': ['Akash', 'Bhumi', 'Chandra'],
      'Age': [29, 30, 35]})
df4 = pd.DataFrame({'ID': [4, 5, 6],
      'Name': ['Ak', 'Bh', 'Cha'],
      'Age': [22, 10, 25]})
print('First DataFrame "df3" ->>\n', df3)
print()
print('Second DataFrame "df4" ->>\n', df4)
print()
merge_df3_df4 = pd.concat([df3, df4], ignore_index = True)
print('Result Of df3 and df4 merge Using pd.concat() -->\n', merge_df3_df4)
print()
df5 = pd.DataFrame({'ID': [1, 3, 5, 6],
      'City': ['Ajmer', 'Jaipur', 'Alvar', 'Delhi'],
      'Security_ID': [20, 13, 27, 38]})
final_merge = pd.merge(merge_df3_df4, df5, on='ID', how='inner')
print('Final Merge with df5 Using pd.merge() On a Common Key ->>\n', final_merge)