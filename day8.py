import pandas as pd

customers = pd.read_csv("noahs-customers.csv")
products = pd.read_csv("noahs-products.csv")
orders = pd.read_csv("noahs-orders.csv")
orders_items = pd.read_csv("noahs-orders_items.csv")

# find all collectibles
coll = products[products['sku'].str.startswith('COL') == True]

# find all orders containing collectibles
collordersitems = pd.merge(coll, orders_items, on='sku', how="inner")
collorders = pd.merge(collordersitems, orders, on="orderid", how="inner")
collcustomers = pd.merge(collorders, customers, on="customerid", how="inner")

custcounts = collcustomers.groupby(['customerid']).count()
print(custcounts.loc[custcounts['sku'].idxmax()])

# assuming the person who owns all the collectibles also owns the most collectibles
collector = customers[customers['customerid'] == 4308]
print(collector)