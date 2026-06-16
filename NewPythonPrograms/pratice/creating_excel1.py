import pandas as pd
import os

# Define the directory path
directory = "C:/Users/pc/Desktop/"

# Ensure the directory exists (no need to create it as it should already exist)
os.makedirs(directory, exist_ok=True)

# Step 1: Create and save the 'Summary1.xlsx' file
dog_data = {
    'Column1': ['DogData1', 'DogData2', 'DogData3'],
    'Column2': [400, 500, 600]
}
dog_df = pd.DataFrame(dog_data)
dog_file_path = os.path.join(directory, 'Summary1.xlsx')
dog_df.to_excel(dog_file_path, index=False)
print("Excel file 'Summary1.xlsx' created successfully!")

# Step 2: Read the existing 'Summary.xlsx' file
cat_file_path = os.path.join(directory, 'Summary.xlsx')

# Load existing data from Summary.xlsx (if it exists)
try:
    cat_df = pd.read_excel(cat_file_path, sheet_name='Summary')
except FileNotFoundError:
    # Create an empty DataFrame if the file or sheet does not exist
    cat_df = pd.DataFrame()

# Step 3: Read the newly created 'Summary1.xlsx' file
dog_df = pd.read_excel(dog_file_path)

# Step 4: Write both DataFrames to separate sheets in 'Summary.xlsx'
with pd.ExcelWriter(cat_file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    # Save the original cat data to the first sheet
    cat_df.to_excel(writer, sheet_name='Summary', index=False)
    
    # Save the dog data to a new sheet
    dog_df.to_excel(writer, sheet_name='New_Summary', index=False)

print("Excel file 'Summary.xlsx' updated with DogData sheet successfully!")
