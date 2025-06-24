import pandas as pd

print('Creating a Series from Dictionary ->')

dic = {'Day1':100, 'Day2':200, 'Day5':300, 'Day4':400}
s_dic = pd.Series(dic, dtype = float)
print(s_dic)

print()
print('Creating a Series from Lists ->')

lis = [111, 222, 333, 444]
s_lis = pd.Series(lis)
print(s_lis)
with_ind = pd.Series(lis, index=['Aa', 'Bb', 'Cc', 'Dd'])
print('With New Index ->')
print(with_ind)

print()
print('Accessing all Elements from Series "s_dic" ->')
for a in s_dic:
    print(a)
print('For Going Through both Index and Values of "s_dic" ->')
for i, v in s_dic.items():
    print(f'Index : {i} ; Value : {v}')
print('Accessing a Element at a Specific Index of "s_dic" ->')
print('Data at index 2 : ', s_dic[2])
