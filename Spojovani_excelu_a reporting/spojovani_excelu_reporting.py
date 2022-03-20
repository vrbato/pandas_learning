import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import numpy as np
import matplotlib.pyplot as plt

#uložení soubrů do proměné - ty si můžu potom přepisovat - nemusím zadávat cestu mám to ve stejné složce
excel_file_1 = "shift_data.xlsx"
excel_file_2 = "third_shift_data.xlsx"

#načtení souborů z jednotlivých listů v souboru shift_data a načtení třetí sady dat ze souboru third_shift_data
#mám víc listů v prvním souboru, musím je načíst jednotlivě

df_first_shift = pd.read_excel(excel_file_1, sheet_name="first")
df_second_shift = pd.read_excel(excel_file_1, sheet_name="second")
df_third_shift = pd.read_excel(excel_file_2)

#print(df_first_shift["Product"])

#spojení všech listů do jednoho
df_all = pd.concat([df_first_shift, df_second_shift, df_third_shift])
#print(df_all)

#spočítání, která směna je nejproduktivnější ze všech
pivot = df_all.groupby(["Shift"]).mean() #vytvořil jsem si agregovanou tabulku podle směn
#nyní si chci vybrat co mě zajímá
shift_productivity = pivot.loc[:,"Production Run Time (Min)" : "Products Produced (Units)"].sort_values("Products Produced (Units)", ascending=False) # : znamená že chceme všechny sloupce a podle čeho vložím do stringu sloupec
#export do excelu
#shift_productivity.to_excel("Produktivita_smen_celkem.xlsx")
df_all.to_excel("vsechny_smeny_vystup.xlsx")

#tvorba grafu
shift_productivity.plot(kind="bar") #plot je metoda pro tvorbu grafu z knihovny plotly do závorky druh grafu
#plt.show() #ukázání grafu


print(shift_productivity)
