import csv

csv_file = 'address_book_data.csv'

headrow = ['Name', 'Address', 'Mobile', 'Email']

datarow =   [
    ['Karan Sharma', 'House No. 45, Naya Bazar, Diggi Bazar Road, Ajmer', '7891234467', 'karan@gamil.com'],
    ['Happy Sharma', 'House No. 30, Vaishali Nagar, Near Gyan Vihar, Ajmer', '8231234467', 'happy@gamil.com'],
    ['Pankaj Agarwal', 'House No. 10,  Civil Lines, Behind Collectorate, Ajmer', '9782012345', 'pankaj@gamil.com']
    ]

rows = [headrow] + datarow

try:
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvf2:
        writer = csv.writer(csvf2)
        writer.writerows(rows)
    print(f"Address book CSV '{csv_file}' created successfully")
except Exception as e:
    print(f"An error occurred while creating the address book CSV file: {e}")