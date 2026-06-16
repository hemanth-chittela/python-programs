import xlsxwriter

def create_fruits_excel(filename):
    # Create a new Excel file and add a worksheet
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    # Define a format for the header
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': '#D7E4BC',
        'border': 1
    })

    # Set the width of the first column (A) to 20
    worksheet.set_column('A:A', 20)

    # Write the column header "Fruits" in cell A1
    worksheet.write(0, 0, 'Fruits', header_format)

    # List of fruits to write into the worksheet
    fruits = ['Apple', 'Banana', 'Grapes', 'Orange', 'Mango']

    # Write each fruit in the column starting from the second row
    for i, fruit in enumerate(fruits, start=1):  # start=1 since row 0 is the header
        worksheet.write(i, 0, fruit)  # Writing fruits in column A

    # Close the workbook
    workbook.close()
create_fruits_excel("example.xlsx")
