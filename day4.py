import pandas as pd

customers = pd.read_csv("noahs-customers.csv")

# first pastries from noah's 
# pastries have prefix "bky"
items = pd.read_csv("noahs-products.csv")
items['ispastry'] = items['sku'].str.startswith('BKY')

# orders that contain pastries
orders_items = pd.read_csv("noahs-orders_items.csv")
pastryorders = pd.merge(items, orders_items, on = "sku", how = "inner")
pastryorders = pastryorders[pastryorders['ispastry'] == True]

# before a certain time in the morning
orders = pd.read_csv("noahs-orders.csv")
allorders = pd.merge(pastryorders, orders, on="orderid", how="inner")
allorders = allorders[allorders['ordered'] == allorders['shipped']] # only in-store

# split date and time
times = allorders['ordered'].str.split(' ',expand=True)
allorders['date'] = times[0]
allorders['time'] = times[1]
allorders = allorders.sort_values('time')

# early in the morning, around 5am
allorders = allorders[(allorders['time'] < '05:00:00') & (allorders['time'] > '04:00:00')]
# "a few years ago"
allorders = allorders[allorders['date'] < '2020-12-31']
# assuming < 1 pastry
allorders = allorders[allorders['qty'] > 1]
print(allorders)

lady = pd.merge(customers, allorders, on="customerid", how="inner")
print(lady['phone'])
