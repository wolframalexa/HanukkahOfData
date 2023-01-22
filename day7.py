import pandas as pd

customers = pd.read_csv("noahs-customers.csv")
products = pd.read_csv("noahs-products.csv")

# they bought the same thing at the same time, except diff colours
orders = pd.read_csv("noahs-orders.csv")
orders_items = pd.read_csv("noahs-orders_items.csv")

# only items in-store
orders = orders[orders['shipped'] == orders["ordered"]]
times = orders['ordered'].str.split(' ',expand=True)
orders['date'] = times[0]
orders['time'] = times[1]
orders = orders.drop(['ordered', 'shipped'], axis = 1)

items = pd.merge(orders, orders_items, on="orderid", how='inner')
items = pd.merge(items, products, on="sku", how="inner")

# only items with colours
items = items[items['desc'].str.endswith(')')]

# split out colours
colours = items['desc'].str.split(' \(',expand=True)
items['desc'] = colours[0]
items['colour'] = colours[1]


# find all of emily's orders
emily = customers[customers['phone'] == "914-868-0316"]
emilyitems = pd.merge(emily, items, on="customerid", how="inner")
# make things a little easier to read
emilyitems = emilyitems.drop(['name', 'address', 'citystatezip', 'birthdate', 'phone'], axis = 1)


for index, row in emilyitems.iterrows():
    # find same date, same item, diff colour
    guy = items[(items['date'] == row['date']) & (items['desc'] == row['desc']) & (items['colour'] != row['colour'])]
    # lns = pd.concat(guy)
    emilyitems = pd.concat([emilyitems, guy], ignore_index = True)

# remove unique rows 
emilyitems = emilyitems[emilyitems.duplicated(subset=["date"], keep=False)].sort_values('date') # dates
emilyitems = emilyitems[emilyitems.duplicated(subset=["desc"], keep=False)].sort_values('date') # diff items

# there at around the same time is 2019/06/01, customer 8835
customers = customers[customers['customerid'] == 8835]
print(customers) # imagine moving in with someone on staten island