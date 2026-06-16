import pandas as pd
import os
directory="C:/Users/pc/Desktop/"
os.makedirs(directory, exist_ok=True)

# Step 2: Create a DataFrame with some data
Fruits_prices = {
    'Fruits': ['Apple', 'Banana', 'Grapes'],  
    'Price': [120, 220, 330]               
}
df = pd.DataFrame(Fruits_prices)

file_path= os.path.join(directory, 'Summary.xlsx')

# Step 3: Save the DataFrame to a new Excel file named 'cat.xlsx'
df.to_excel(file_path, sheet_name='Summary', index=False)

print("Excel file 'Summary.xlsx' created successfully!")
