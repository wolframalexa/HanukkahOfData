import pandas as pd

customers = pd.read_csv("noahs-customers.csv")

# start with other people with the same last name
names = customers['name'].str.split(' ',expand=True)
customers['first'] = names[0]
customers['last'] = names[1].str.lower()

kochs = customers[customers['last'] == 'koch']
print(kochs) # no luck!

# "subway fare" = lives within nyc
state = customers['citystatezip'].str.split(', ',expand=True)
state = state[1].str.split(' ', expand = True)
print(state)

customers['state'] = state[0]
print(customers)
nycustomers = customers[customers['state'] == "NY"]
print(nycustomers)