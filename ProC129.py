import pandas as pd
import numpy as np 
import csv

df = pd.read_csv("dwarf_stars.csv")
df = df.dropna()
'''

new_radii = []
new_masses = []

#getting radius
radii = df['Radius'[1:]]    
#converting radius into solar radius
for row in radii:
    row = float(row*0.102763)
    new_radii.append(row)

#getting mass
masses = df['Mass'[1:]]
#converting radius into solar masses
for mass in masses:
    mass = float(mass * 0.000954588)
    new_masses.append(mass)

#Writing all the data in new csv file
with open("new_Radi_mass.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow("Radius","Mass")
    csvwriter.writerows(new_radii)
    csvwriter.writerows(new_masses)

'''
df["Radius"] = 0.102763*df["Radius"]
df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Mass"] = 0.000954588*df["Mass"] 



df.to_csv("new_Radi_mass.csv")
#Merging data in 2 files

dataset_1 = []
dataset_2 = []

with open("bright_stars.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open("new_Radi_mass.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

headers_1 = dataset_1[0]
data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
data_2 = dataset_2[1:]

headers = headers_1+headers_2
data = []

for index,data_row in enumerate(data_1):
    data.append(data_1[index]+data_2[index])

with open("total_stars.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(data)




