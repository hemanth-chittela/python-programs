import pandas as pd

# Step 2: Create a DataFrame with some data
Summary = {
    'Column1': ['Data1', 'Data2', 'Data3'],  # This creates the rows for Column1
    'Column2': [100, 200, 300]               # This creates the rows for Column2
}
df = pd.DataFrame(Summary)

# Step 3: Save the DataFrame to a new Excel file named 'cat.xlsx'
df.to_excel('Summary.xlsx', sheet_name='Summary', index=False)

print("Excel file 'Summary.xlsx' created successfully!")
