import pandas as pd #importuju knihovnu pandas s aliasem PD pro další práci

    #načtení csv
df_csv = pd.read_csv("pokemon_data.csv")

    #načtení excelu
#df_xlsx = pd.read_excel("pokemon_data.xlsx")

#print(df_xlsx.head(5)) #tail nebo head(kolik řádků chci vidět)

    #načtení hlavičky
#print(df_csv.columns)

    #načtení sloupců
#print(df_csv["Name"][0:5]) prvních 5 řádků
#print(df_csv[["Name", "Type 1", "HP"]]) #načtení více řádků najednou

    #načtení řádků
#print(df_csv.head(4))
#print(df_csv.iloc[1]) #načtení toho co je v řádku na indexu 1
#print(df_csv.iloc[0:4])

    #načtení určité pozice řádek X sloupec
#print(df_csv.iloc[2,1]) #index 2 řádku a 1 index sloupce

    #procházení řádků FOR loop
#for index,row in df_csv.iterrows():
    #print(index,row["Name"])

    #hledání v řádcích podle slova FIRE a sloupce Type
#print(df_csv.loc[df_csv["Type 1"] == "Fire"])



#print(df_csv.describe()) #udělá rychlou analýzu dat

#print(df_csv.sort_values(["Name"], ascending=False)) #seřazení podle jména vzestupně - ascending
#print(df_csv.sort_values(["Type 1", "HP"], ascending=True)) #ruzný řazení podle sloupce co obsahuje
#print(df_csv.sort_values(["Type 1", "Speed"], ascending=[1,0])) #řazení podle Type od A-Z = 1 jako True a podle rychlosti od nejvyšší = 0 jako False

        #ZMĚNY HODNOT

#df_csv["Total"] = df_csv["HP"] + df_csv["Attack"] + df_csv["Defense"] #přidám sloupec se součtem sloupců
#df = df_csv.drop(columns=["Generation"]) odstranění sloupce, ale musím si data uložit do nové proměnné

    #může být riskantní používání indexu v sumě a přesunování sloupců
#df_csv["Total"] = df_csv.iloc[:, 4:10].sum(axis=1) #zamykam si všechny řádky, a sloupec 4 až 9 (musím dát 10,aby to bralo správný index). sum a osa 1 = horizontálně
#posunutí TOTAL před číselné hodnoty

#list_sloupcu = list(df_csv.columns)
#df_csv = df_csv[list_sloupcu[0:2] + [list_sloupcu[-1]] + list_sloupcu[2:12]] #-1 posunutí TOTAL z poslední pozice za 2 index Legendery

        # uložení do nového souboru csv nebo exel
#df_csv.to_csv("upravene_pokemon.csv", index=False) #odstarní to první sloupec indexu
#df_csv.to_csv("upravene_pokemon.txt", index=False, sep="\t") #uloží soubor txt oddělený tabulátory
#df_csv.to_excel("upravene_pokemon.xlsx", index=False)

        # Filtrování dat - jednoduché filtrování pomocí metody LOC
#new_df = df_csv.loc[(df_csv["Type 1"] == "Grass") & (df_csv["Type 2"] == "Poison") & (df_csv["HP"] > 70)] #vyfiltruje, ale se starýma indexama
#resetování indexu
#new_df.reset_index(drop=True, inplace=True)

#filtrování podle obsahu
#obsahuje = df_csv.loc[df_csv["Name"].str.contains("Mega")] #vyfiltruje vše ve sloupečku Name - co má Mega
#obsahuje = df_csv.loc[~df_csv["Name"].str.contains("Mega")] #vyfiltruje vše ve sloupečku Name - co NEMÁ Mega před určení sloupce dám vlnku = alt + 126

#import re #pro filtrování podle libovolných písmen v názvu,atd...
#nazvy_co_zacinaji_na_PI = df_csv[df_csv["Name"].str.contains("^pi[a-z]*", flags=re.I,regex=True)] #^ začáteční písmeno [a-z]* všechny písmena za tim, flags - ignoruje velké,malé

#nazvy_co_zacinaji_na_PI.to_excel("nazev_pi.xlsx",index=False) #ale v ukládaném souboru si index mažu

        #změna hodnoty pomocí filtru
#df_csv.loc[df_csv["Type 1"] == "Fire", "Legendary"] = "Flamer" #co chci měnit, kde to chci měnit Legendery = co tam chci napsat
#df_csv.loc[df_csv["Total"] >200, ["Legendary"]] = "over 200" #měním hodnoty podle
#print(df_csv.loc[df_csv["Total"] > 150]) #chci zobrazit jen co je víc než 150

        #agregace GROUPBY metoda
#print(df_csv.groupby(["Type 1"]).mean()) #seřazení podle typu
#print(df_csv.groupby(["Type 1"]).mean().sort_values("Attack", ascending=False)) #agregace podle typu s nejvyšší Attack (ascending=False -> od nejvyššího)
# .sum / .mean / .count
df_csv["Count"] = 1 #pomocnej sloupec na každý řádek - podle toho si to sečtu
pocet_druhu = df_csv.groupby(["Type 1"]).count()["Count"] #první je co chci agregovat.count [podle čeho]
pocet_druhu.to_excel("Pocet druhu.xlsx")




