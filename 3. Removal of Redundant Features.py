import pandas as pd
data = pd.read_csv("Feature-Selected.csv")
import csv
l = []
q=t=0
a = list(data['ID_REF_NEW'])
b = list(data['ID_REF'])
csvfile = "identified-features.csv"
with open(csvfile, "w") as output:
    output.close()
up = []
down = []
count = 0
for i in a:
    if i in b:
        up.append(b.index(i))
    elif((i=='NaN')|(i=="NaN")):
        count = count + 1
        break
    else:
        print("Error")
        break
print(count)
print("Loop Break")
            #print(len(up))
headers = list(data.columns.values)
with open(csvfile, "w") as output:
    writer = csv.writer(output)
    writer.writerow(headers)
    output.close()
for i in up:
    l.append(data.iloc[i])
with open(csvfile, "a") as output:
    writer = csv.writer(output, lineterminator="\n")
    writer.writerows(l)
data = pd.read_csv("identified-features.csv")
del data['ID_REF_NEW']
data.dropna()
data.to_csv("id-features.csv", index=False)
import pandas as pd
import csv
dt = pd.read_csv("Labels - 16619.csv")
del dt['ID_REF']
dt.to_csv("Labels-Only.csv", index=False)
dt = pd.read_csv("Labels-Only.csv")
lis = []
lis.append("Class")
for index,rows in dt.iterrows():
    lis.append(rows[0])
csvfile = "id-features.csv"
with open(csvfile, "a") as output:
    writer = csv.writer(output)
    writer.writerow(lis)
    output.close()
data = pd.read_csv("id-features.csv")
del data['GSM417174']
del data['GSM417231']
del data['GSM417234']
del data['GSM417242']
del data['GSM417251']
del data['GSM417252']
del data['GSM417381']
del data['GSM417382']
dt = data.T
dt.to_csv("Complete.csv", header=False)