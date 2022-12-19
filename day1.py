import pandas as pd
import re

customers = pd.read_csv("noahs-customers.csv")
names = customers['name'].str.split(' ',expand=True)
customers['first'] = names[0]
customers['last'] = names[1].str.lower()

# map names to phone numbers
chars = {"a":"2","b":"2","c":"2","d":"3","e":"3","f":"3","g":"4","h":"4","i":"4","j":"5","k":"5","l":"5","m":"6","n":"6","o":"6","p":"7","q":"7","r":"7","s":"7","t":"8","u":"8","v":"8","w":"9","x":"9","y":"9","z":"9"}

lns = []
for index, row in customers.iterrows():
    ln = row['last']
    for key in chars:
    # print(key, type(chars[key]))
        ln = ln.replace(key, chars[key])
    lns.append(ln)
customers['nametophone'] = lns

# process phone numbers
customers['phone'] = customers['phone'].str.replace("-",'')
privateeye = customers[customers['phone'] == customers['nametophone']]
print(privateeye)