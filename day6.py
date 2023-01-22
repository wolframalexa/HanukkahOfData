import pandas as pd

customers = pd.read_csv("noahs-customers.csv")

# start with other people with the same last name
names = customers['name'].str.split(' ',expand=True)
customers['first'] = names[0]
customers['last'] = names[1].str.lower()

kochs = customers[customers['last'] == 'koch']
# print(kochs) # no luck!

# "subway fare" = lives within nyc
state = customers['citystatezip'].str.split(', ',expand=True)
state = state[1].str.split(' ', expand = True)

customers['state'] = state[0]
nycustomers = customers[customers['state'] == "NY"]

# find cheapest each item has ever been at noah's
orders_items = pd.read_csv("noahs-orders_items.csv")
cheapest = orders_items.loc[orders_items.groupby("sku").unit_price.idxmin()]
print(cheapest)

# find orders with cheapest items
orders = pd.read_csv('noahs-orders.csv')
cheaporders = pd.merge(cheapest, orders, on = "orderid", how="inner")

# find who's buying the cheapest items
cheapskates = pd.merge(nycustomers, cheaporders, on = "customerid", how = "inner")
print(cheapskates['phone'].mode())

# see if this woman shows up multiple times