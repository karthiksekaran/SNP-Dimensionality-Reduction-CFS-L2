print("#========================================Part 1======================================================")
import pandas as pd
dataset = pd.read_csv("GSE16619-Original.csv")
dataset.replace({'AA':'100','BB':'10','AB':'1','NC':'0'}, inplace=True)
dataset.to_csv("Dataset-Processed.csv", index=False)
print("#========================================Part 2======================================================")
new = pd.read_csv("Dataset-Processed.csv", index_col=None)
l = []
list_var = []
col = []
for column in new:
    col.append(column)
m = len(col)
for index, row in new.iterrows():
    l.append(index)
n = len(l)
ind=0
AA='100'
BB='10'
AB='1'
No_Call='0'
t1=0
t2=0
t3=0
t4=0
non_repeat_list = []
repeat_list = []
temp_list = []
temp_var = 0
cast = 0
dummy_var=0
while(n>0):
    list_var.append(new.iloc[ind])
    repeat_list.append(new.iloc[ind])
    temp_list.append(new.iloc[ind])
    for index in temp_list:
        for i in range(1,m):
            temp_var = index[i]
            cast = str(temp_var)
            if(AA==cast):
                t1=t1+1
            elif (BB == cast):
                t2=t2+1
            elif (AB == cast):
                t3=t3+1
            elif (No_Call == cast):
                t4=t4+1
            else:
                print("Unknown")
        cal = (t4/m)*100
        if((t1==m-1)|(t2==m-1)|(t3==m-1)|(t4==m-1)|(cal>0)):
            list_var.pop()
        else:
            dummy_var = 0
    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0
    temp_list = []
    ind = ind + 1
    n = n - 1
red=len(list_var)
rep=len(repeat_list)
deleted=rep-red
import csv
csvfile = "transformed-modified.csv"
headers = list(new.columns.values)
with open(csvfile, "w") as output:
    writer = csv.writer(output)
    writer.writerow(headers)
    output.close()
with open(csvfile, "a") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(list_var)
    output.close()
file = pd.read_csv('transformed-modified.csv', index_col=None)
file.dropna()
file.to_csv("final.csv", index=False)
print("#========================================Part 3======================================================")
new = pd.read_csv("final.csv")
del new['ID_REF']
new.to_csv("Updated_new.csv", index=False)
new = pd.read_csv("Updated_new.csv",dtype=int)
l = []
l.append(new.mode(axis=1))
temp = list([i[0] for i in l])
dum = []
for i in temp[0]:
    dum.append(i)
inc = 0
final_list = []
csvfile = "temp.csv"
with open(csvfile, "w") as output:
    output.close()
headers = list(new.columns.values)
with open(csvfile, "w") as output:
    writer = csv.writer(output)
    writer.writerow(headers)
    output.close()
for i in dum:
    j = int(i)
    final_list.append(new.iloc[inc].replace(0,j))
    with open(csvfile, "a") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(final_list)
    final_list = []
    inc = inc + 1
file = pd.read_csv('temp.csv', index_col=None)
file.dropna()
file.to_csv("1.Processing.csv", index=False)
print("========================================Part 4======================================================")
import pandas as pd
data = pd.read_csv("final.csv")
l = []
l.append(data.iloc[:,0])
temp = list([i for i in l])
dum = []
for i in temp[0]:
    dum.append(i)
data = pd.read_csv("1.Processing.csv")
data.insert(0, "ID_REF", dum)
data.to_csv("Processed-Dataset.csv", index=False)
print("Program Executed Successfully")