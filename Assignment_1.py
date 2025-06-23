
#Assignment 1 -> Question 1

studentname = input('Enter Name:')
studentclass = input('Enter Class:')

print('\nEnter Marks')
m1 = float(input('Math:'))
m2 = float(input('Physics:'))
m3 = float(input('Chem:'))
m4 = float(input('CS:'))
m5 = float(input('Civics:'))

totalmarks = m1+m2+m3+m4+m5
percentage = (totalmarks/500)*100

print('Result', end=' -> ')
print(f'Name: {studentname}', end=' ; ')
print(f'Class: {studentclass}', end=' ; ')
print(f'Total Marks: {totalmarks:.2f}', end=' ; ')
print(f'Percentage: {percentage:.2f}%')


#Assignment 1 -> Question 2

str1 = input('Enter First String:')
str2 = input('Enter Second String:')

concat_str = str1+str2
print(f'Original Strings - 1. {str1}, 2. {str2}', end=' ; ')
print(f'Concatenated String - {concat_str}')

print('\nString Methods ->')
print(f'I. Title Function: "{concat_str.title()}"')
print(f'II. Length Function: "{len(concat_str)}"')
print(f'III. Uppercase Function: "{concat_str.upper()}"')
print(f'IV. Lower Function: "{concat_str.lower()}"')
print(f'V. Capitalized Function: "{concat_str.capitalize()}"')
print(f'VI. Center with width 50 ; Fill Spaces "-" : "{concat_str.center(50, '-')}"')
print(f'VII. Count Function [COUNT OF "t"]: "{concat_str.count('t')}"')
print(f'VIII. Find Function: "{concat_str.find('py')}"')
print(f'IX. Replace Function [replace "o" with "*"]: "{concat_str.replace('o', '*')}"')
print(f'X. Does the string start with "he" [startswith Function]: "{concat_str.startswith('he')}"')
print(f'XI. Does the string end with "wo" [endswith Function]: "{concat_str.endswith('wo')}"')
print(f'XII. rpartition Function: "{concat_str.rpartition('nt')}"')
print(f'XIII.  Function: "{concat_str.rpartition('nt')}"')

letters = 'tone'
key = '1234'
encoding = concat_str.maketrans(letters, key)
print('XIX. maketrans() and translate() Function: ', concat_str.translate(encoding))

