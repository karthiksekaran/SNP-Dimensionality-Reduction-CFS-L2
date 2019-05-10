import pandas as pd
print("#========================================Part 1======================================================")

l = []
new = pd.read_csv("Processed-Dataset.csv")
for index, row in new.iterrows():
    l.append(index)
n = len(l)
sub_temp = n
col = []
for column in new:
    col.append(column)
m = len(col)
print(n)
print(m)
samples = m-1
list_var = []
repeat_list = []
temp_list = []
ind = 0
AA = 1
BB = 10
AB = 100
t1 = t2 = t3 = t7 = 0
t4 = []
t6 = []
t5 = []
t8 = []
while(n>0):
    list_var.append(new.iloc[ind])
    repeat_list.append(new.iloc[ind])
    temp_list.append(new.iloc[ind])
    for index in temp_list:
        for i in range(1,m):
            temp_var = index[i]
            cast = temp_var
            if(AA==cast):
                t1=t1+1
            elif (BB == cast):
                t2=t2+1
            elif (AB == cast):
                t3=t3+1
            else:
                print("Unknown")
                t7=t7+1
        t4.append(t1)
        t5.append(t2)
        t6.append(t3)
        t8.append(t7)
    t1 = t2 = t3 = t7 = 0
    temp_list = []
    ind = ind + 1
    n = n-1
p_t1 = []
p_t2 = []
p_t3 = []
print("#========================================Part 2======================================================")
for i in t4:
    p_t1.append((i/samples)*100)
for i in t5:
    p_t2.append((i/samples)*100)
for i in t6:
    p_t3.append((i/samples)*100)
print("#========================================Part 3======================================================")
headers = []
headers.append('ID_REF')
test = pd.read_csv("Processed-Dataset.csv")
for index, row in new.iterrows():
    headers.append(row[0])
tmp = 0
inc = 0
update = []
len_p = len(p_t1)
while(len_p>0):
    if((30<p_t1[tmp]<35)|(30<p_t2[tmp]<35)|(30<p_t3[tmp]<35)):
        inc = inc + 1
        update.append(headers[tmp])
    tmp = tmp + 1
    len_p = len_p - 1
sub = sub_temp-len(update)
for i in range(0,sub):
    update.append('NaN')

import csv
csvfile = "minimized.csv"
with open(csvfile, "w") as output:
    output.close()
csvfile = "minimized.csv"
with open(csvfile, "a") as output:
    writer = csv.writer(output)
    writer.writerow(update)
    output.close()
data = pd.read_csv("minimized.csv")
dataset = data.T
dataset.to_csv("minimized-norm.csv")
data = pd.read_csv("Processed-Dataset-Copy-2.csv")
data.insert(0, "ID_REF_NEW", update)
data.to_csv("Feature-Selected.csv", index=False)
