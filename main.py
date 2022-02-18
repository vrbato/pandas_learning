import pandas as pd
import plotly.express as px

df_gold_prices = pd.read_csv("monthly_gold_prices.csv")

#kouknutí se na data - posledních 20 proto tail
print(df_gold_prices.tail(20))

dates = df_gold_prices["Date"]
prices = df_gold_prices["Price"]

#jednoduchý operace
df_gold_prices["buy_price"] = prices * .9 #vytvoří to nový sloupec "buy price" který dopočítá 90% z cen
print(df_gold_prices["Price"].max())

#očištění dat
df_gold_prices["Date"] = df_gold_prices ["Date"].str.replace("-", "")
#zobrazení sešitu - proměnné
print(df_gold_prices)

#graf
fig = px.line(df_gold_prices, x = dates, y = prices, title = "Gold Prices over Time")
fig.show()
