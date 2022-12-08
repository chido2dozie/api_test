import openpyxl

# Load excel workbook
workbook = openpyxl.load_workbook('/Users/chidozieamefule/Downloads/Copy of Credentials.xlsx')


def read_excel():
    # Print all sheet names on workbook
    print(workbook.sheetnames)

    # Accessing the individual sheets
    sheet = workbook['Credentials']

    # Print Login details on line 3
    print('Username: ' + str(sheet['A3'].value) + '\nPassword: ' + str(sheet['B3'].value))


read_excel()
