import pandas as pd

customers = pd.read_csv("noahs-customers.csv")
names = customers['name'].str.split(' ',expand=True)
customers['first'] = names[0].str.lower()
customers['last'] = names[1].str.lower()

# find j.d. customers
customers = customers[(customers['first'].str[0] == 'j') & (customers['last'].str[0] == 'd')]

# orders in 2017
orders = pd.read_csv("noahs-orders.csv")
orders = orders[orders['ordered'].str[0:4] == "2017"]

# coffee orders
items = pd.read_csv("noahs-orders_items.csv")
items = items[items['sku'] == 'DLI1464']

# coffee orders in 2017
coffee2017 = pd.merge(items, orders, on = "orderid", how = "inner")

# j.d. who ordered coffee in 2017
new = pd.merge(customers, coffee2017, on = "customerid", how = "inner")
print(new.head())