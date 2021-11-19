
# This program is using the scraper tool and capital IQ

import pandas as pd
import matplotlib.pyplot as plt

## Importing the datasets into pndas dataframes
groupaa = pd.read_csv(r"C:\Users\adeja\Downloads\WEIGHTINGS.csv")
sexp = pd.read_csv(r"C:\Users\adeja\Downloads\somebs.csv")
US_com = pd.read_csv(r"C:\Users\adeja\OneDrive\Desktop\UPS sheets\painALL US listed companies.csv")



## Turning the pandas series of the industry group and sectors into lists.
groups = (sexp['Industry Group'].tolist())
groups_dict ={}
sectors = (sexp['Industry Sector']).tolist()
sectors_dict = {}


groups_US = US_com['Industry Group'].tolist()
sector_US = US_com['Sector'].tolist()
US_sectors_dict = {}
US_groups_dict = {}

###

for c in range(len(groups)):
    groups_dict[groups[c]] = (groups.count(groups[c])/len(groups))*100
for c in range(len(sectors)):
    sectors_dict[sectors[c]] = sectors.count(sectors[c])#/len(sectors)*100


for c in range(len(groups_US)):
    US_groups_dict[groups_US[c]] = groups_US.count(groups_US[c]) #/ len(groups_US) * 100
for c in range(len(sector_US)):
    US_sectors_dict[sector_US[c]] = sector_US.count(sector_US[c]) # / len(sector_US) * 100

keys_groups = list(groups_dict.keys())
key_sectors = list(sectors_dict.keys())
US_groups_dict = {k: US_groups_dict[k] for k in keys_groups}
US_sectors_dict = {k: US_sectors_dict[k] for k in key_sectors}


print(f'Results of the Total pop (IND_GROUPS) {US_groups_dict}')
print(f'results of sample(IND_GROUPS) {groups_dict}')
print(f'Results of the Total pop (IND_SECTORS) {US_sectors_dict}')
print(f'results of sample (IND_SECTORS) {sectors_dict}')

#keys = list(sectors_dict.keys())
#new_dict = US_sectors_dict
#for i in US_sectors_dict.keys():
    #new_dict[i] = US_sectors_dict.get(i) - sectors_dict.get(i)

#la = []
#for i in new_dict.keys():
    #if new_dict.get(i) < 5:
       # la.append(i)
#new_dict = {key:val for key, val in new_dict.items() if key in la}



#print(f'Results of the Total pop (IND_GROUPS) {US_groups_dict}')
#print(f'results of sample(IND_GROUPS) {groups_dict}')
#print(f'Results of the Total pop (IND_SECTORS) {US_sectors_dict}')
#print(f'results of sample (IND_SECTORS) {sectors_dict}')


vals = list(sectors_dict.values())
keys2 = list(US_sectors_dict.keys())
vals2 = list(US_sectors_dict.values())
plt.bar(keys2[0:12], vals2[0:12])


plt.xlabel("Industry Sectors")
plt.xticks(rotation = 45)
plt.ylabel("% of total difference")
plt.title("Differences in industry sector proportion from population and sample")

plt.show()


