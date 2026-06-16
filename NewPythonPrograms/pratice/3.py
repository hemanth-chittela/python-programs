import xlsxwriter

def example(wb, excel_file):
    # Create a header format
    header_format = wb.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': '#D7E4BC',
        'border': 1
    })


    center_format = wb.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })


    # Add a new worksheet with the name based on the file name
    sheetname = wb.add_worksheet(str(excel_file).split('/')[-1].split('.')[0])

    # Write "Fruits" in the first cell with the header format
    sheetname.write(0, 0, "Fruits", header_format)

    # List of fruits to be added as data
    fruits = ["Apple", "Banana", "Orange", "Grapes", "Strawberry"]
    
    # Write each fruit to the worksheet, starting from the second row
    for i, fruit in enumerate(fruits, start=1):
        sheetname.write(i, 0, fruit, center_format)
    
    # Set the column width
    sheetname.set_column('A:A', 40)
    
    # Apply autofilter to the column
    sheetname.autofilter('A1:A6')

    return sheetname 

# Example usage
if __name__ == "__main__":
    # Specify the path to the Excel file
    excel_file = "C:/Users/pc/Desktop/your_excel_file.xlsx"
    
    # Create a new Excel file and a workbook object
    wb = xlsxwriter.Workbook(excel_file)
    
    # Call the example function with the workbook and file path
    example(wb, excel_file)
    
    # Close the workbook to save the file
    wb.close()
