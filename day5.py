import pandas as pd

customers = pd.read_csv("noahs-customers.csv")

# queens village
city = customers['citystatezip'].str.split(', ',expand=True)
customers['city'] = city[0]
customers = customers[customers['city'] == "Queens Village"]

# # noah's market sweatshirt, actually called a jersey for some reason
items = pd.read_csv("noahs-products.csv")
# jerseys = items[items['desc'].str.startswith("Noah's Jersey")]

# # orders containing jerseys
orders_items = pd.read_csv("noahs-orders_items.csv")
orders = pd.read_csv("noahs-orders.csv")

# jerseyorders = pd.merge(orders_items, jerseys, on="sku", how = "inner")
# jerseycustomers = pd.merge(jerseyorders, orders, on='orderid', how='inner')
# print(jerseycustomers)

# # customers from queens village who have ordered jerseys
# qnsjersey = pd.merge(jerseycustomers, customers, on="customerid", how="inner")
# # qnsjersey = pd.merge(qnsjersey, customers, on="customerid", how="inner")
# print(qnsjersey)
# this is empty??

# customers who buy cat food
cat_items = items[items['desc'].str.contains('Cat')]
catorders = pd.merge(orders_items, cat_items, on="sku", how="inner")
catorders = pd.merge(catorders, orders, on="orderid", how="inner")
qnscatcust = pd.merge(customers, catorders, on="customerid", how="inner")

# pick the woman who buys the most...
qnscatcust = qnscatcust[qnscatcust['name'] == 'Anita Koch']
print(qnscatcust['phone'])
