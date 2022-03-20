import pandas as pd

soubor_1 = "Workbook1.xlsx"

df_1 = pd.read_excel(soubor_1, sheet_name="1st")
df_2 = pd.read_excel(soubor_1, sheet_name="2nd")

# print(df_1.head(5))
# print(df_2.head(5))

all_data = pd.concat([df_1, df_2], axis=0) #dávám axis = 0 aby byly nadpisy v jedné řádce, pokud 1 tak budou vedle sebe
#print(all_data)

productivity_df = all_data.groupby(["Operator","Line #"]).mean()#.sort_values("Amount", ascending=False)
print(productivity_df["Amount"])
