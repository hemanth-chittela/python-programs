import sys
import pandas as pd
#from openpyxl import load_workbook
import xlsxwriter

# Get the path to summary.xlsx from command-line arguments
summary_file_path = str(sys.argv[1]) + "/Summary.xlsx"

# Read the existing Excel file with pandas
existing_df = pd.read_excel(summary_file_path, sheet_name=None)

# List of sheets to check
sheets_to_check = ["sheet1","tim","sheet2"]

# Initialize dictionary for storing sheet counts
data_for_summary = {}

# Check each sheet and count non-empty rows
for sheet_name in sheets_to_check:
    if sheet_name in existing_df:
        sheet_df = existing_df[sheet_name]
        filled_data_count = sheet_df.dropna(how='all').shape[0]
        data_for_summary[sheet_name] = filled_data_count
    else:
        print(f"Warning: '{sheet_name}' does not exist in the workbook.")
        data_for_summary[sheet_name] = 0

# Convert dictionary to DataFrame for 'Summary1' sheet with header included
summary1_df = pd.DataFrame(list(data_for_summary.items()), columns=['fruits', 'count'])

# Write the data to a new Excel file with xlsxwriter
new_summary_file_path = str(sys.argv[1]) + "/New_Summary.xlsx"

with pd.ExcelWriter(new_summary_file_path, engine='xlsxwriter') as writer:
    # Write existing sheets to the new file
    for sheet_name, df in existing_df.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    # Write the summary data to 'Summary1'
    summary1_df.to_excel(writer, sheet_name='Summary1', index=False, startrow=1, header=False)

    # Access the xlsxwriter workbook and worksheet objects
    workbook  = writer.book
    worksheet = writer.sheets['Summary1']
    
    # Set the cell format to wrap text and add border
    cell_format = workbook.add_format({'text_wrap': True, 'border': 0})
    
    # Write the header manually
    worksheet.write_string(0, 0, 'fruits', cell_format)
    worksheet.write_string(0, 1, 'count', cell_format)
    
    # Apply the format to the entire columns and cells
    worksheet.set_column('A:A', 20, cell_format)  # Adjust the width as needed
    worksheet.set_column('B:B', 10, cell_format)  # Adjust the width as needed
    
    # Write the data starting from the second row
    for row_num, (index, row) in enumerate(summary1_df.iterrows(), start=1):
        worksheet.write_string(row_num, 0, row['fruits'], cell_format)
        worksheet.write_number(row_num, 1, row['count'], cell_format)

print(f"'Summary1' sheet created in {new_summary_file_path} with the counts of filled data from sheets {', '.join(sheets_to_check)}.")
