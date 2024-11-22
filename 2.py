import pandas as pd
import json
ListCon=[]
Month=("January","February","March","April","May","June","July","August","September","October","November","December")
for i in range (len(Month)):
    print(f"Введіть кількість беттоних плит виготовлених за {Month[i]}:")
    c=int(input())
    ListCon.append(c)
Dict1=dict(zip(Month,ListCon))
m1=pd.Series(Dict1)
with open("Beton.json","w") as f:
    for keys,values in m1.items():
        json.dump(keys,f)
        json.dump(values,f)
