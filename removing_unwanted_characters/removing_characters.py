import pandas as pd

messy_excel = "messy_excel.xlsx"

df_data = pd.read_excel(messy_excel)

for column in df_data.columns:
    df_data[column] = df_data[column].str.replace(r'\W',"")

df_data.to_excel("clean_data.xlsx",index=False)