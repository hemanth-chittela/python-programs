import pandas as pd

# Step 1: Create and save the 'dog.xlsx' file
dog_data = {
    'Column1': ['DogData1', 'DogData2', 'DogData3'],
    'Column2': [400, 500, 600]
}
dog_df = pd.DataFrame(dog_data)
dog_df.to_excel('summary1.xlsx', index=False)
print("Excel file 'dog.xlsx' created successfully!")

# Step 2: Read the existing 'cat.xlsx' file
cat_df = pd.read_excel('Summary.xlsx')

# Step 3: Read the newly created 'dog.xlsx' file
dog_df = pd.read_excel('Summary1.xlsx')

# Step 4: Write both DataFrames to separate sheets in 'cat.xlsx'
with pd.ExcelWriter('Summary.xlsx') as writer:
    # Save the original cat data to the first sheet
    cat_df.to_excel(writer, sheet_name='Summary', index=False)
    
    # Save the dog data to a new sheet
    dog_df.to_excel(writer, sheet_name='New_Summary', index=False)

print("Excel file 'cat.xlsx' updated with DogData sheet successfully!")
