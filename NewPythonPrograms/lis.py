import pandas as pd

file_path='C:/Users/pc/Desktop/Sample.xlsx'
sheet_names=pd.ExcelFile(file_path).sheet_names
print(sheet_names[0])