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
lis = []
lis.append("Class")
for i in range(0,96):
    n = 'Thyroid'
    lis.append(n)
for i in range(0,129):
    n = 'Control'
    lis.append(n)
csvfile = "id-features.csv"
with open(csvfile, "a") as output:
    writer = csv.writer(output)
    writer.writerow(lis)
    output.close()
data = pd.read_csv("id-features.csv")
dt = data.T
dt.to_csv("Completed.csv", header=False)