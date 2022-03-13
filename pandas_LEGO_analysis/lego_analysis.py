import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print("="*50)
print(f"{'Úkol jedna':^50}")
print("="*50)
df = pd.read_csv("datasets/lego_sets.csv")

theme = pd.read_csv("datasets/parent_themes.csv")

#spojení dvou souborů merge
merged = df.merge(theme, left_on="parent_theme", right_on="name")
merged.drop(columns="name_y", inplace=True) #odstranění sloupce
#print(merged[merged["set_num"].isnull()].shape) #zjistím přes filtrování - kolik je tam nulových hodnot (153 řádků,8)


#vyběr pouze licencovaných setů
licensed = merged[merged["is_licensed"]]
licensed = licensed.dropna(subset=["set_num"]) #vymažu si z proměnné licensed řádky, kde jsou nuly ve sloupci set_num

#vyběr konkrétního setu
star_wars = licensed[licensed["parent_theme"] == "Star Wars"]

#spočítat podíl star wars na všech licencovaných produktech
    #star_wars.shape #dotaz na počet řádek a sloupců (609, 8)
    #když chci počet položek zadam metodu shape a index [0] => rovnou to můžu použít do vzorce
the_force = (star_wars.shape[0]/licensed.shape[0])*100 #dělím pouze star_wars / všema licencovanýma
print(f"Výsledek úkolu_1 je: {the_force :.2f} %")

print("="*50)
print(f"{'Úkol dva':^50}")
print("="*50)

#seřazení podle roku od nejstaršího a zgroupování podle roku a parent_theme
licensed_sorted = licensed.sort_values("year")
licensed_sorted["count"] = 1 #pomocný sloupec pro počet
pocet_licencovanych_setu = licensed_sorted.groupby(["year", "parent_theme"]).sum().reset_index() #posčítáto podle pomocného sloupce count a je to ve skupinách podle let a theme a přiřadí nový index od 1. řádku =0
#print(pocet_licencovanych_setu.head(5))

max_prodej = pocet_licencovanych_setu.sort_values("count", ascending=False).drop_duplicates(["year"])#seřazení podle prodejů od nejprodávanější, vyloučení duplicit v roce
max_prodej.sort_values("year", inplace=True) #seřadím prodeje podle let, abych zjistil, kdy nebyl star-wars nejprodávanější
#max_prodej.to_excel("pocet_prodeju_podle_let.xlsx", index=False)

vysledek_ukol2 = 2017
print(f"Výsledek úkolu_2 je: {vysledek_ukol2}")

print(max_prodej.head(50))




