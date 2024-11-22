import array
import json
ListCon=[]
Month=("January","February","March","April","May","June","July","August","September","October","November","December")
for i in range (len(Month)):
    print(f"Введіть кількість беттоних плит виготовлених за {Month[i]}:")
    c=int(input())
    ListCon.append(c)
Series=array.array('i',ListCon)
Dict1=dict(zip(Month,ListCon))
with open("Beton.json","w") as f:
    json.dump(Dict1,f)
print(a)