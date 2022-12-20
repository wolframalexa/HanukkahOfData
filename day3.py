import pandas as pd

customers = pd.read_csv("noahs-customers.csv")

# aries - march 21 to april 20
# start = '03-21'
# end = '04-20'
# born in the year of the dog
customers = customers[(customers['birthdate'] >= '1958-03-21') & (customers['birthdate'] <= '1958-04-20') | (customers['birthdate'] >= '1970-03-21') & (customers['birthdate'] <= '1970-04-20') | (customers['birthdate'] >= '1982-03-21') & (customers['birthdate'] <= '1982-04-20')]

# in the same neighborhood as day 2 answer, South Ozone Park
city = customers['citystatezip'].str.split(', ',expand=True)
customers['city'] = city[0]

customers = customers[customers['city'] == "South Ozone Park"]
print(customers.head())