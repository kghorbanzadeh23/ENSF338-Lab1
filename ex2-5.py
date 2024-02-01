import json
import timeit

def changeSize(inputData):
    for i in inputData:
        i["payload"]["size"] = 35

f = open('large-file.json', encoding="utf8")
data = json.load(f)
f.close()

time = []

for i in range(10):
    tm =timeit.timeit(lambda: changeSize(data), number=1)
    time.append(tm)
print("The average time is: ", sum(time)/len(time))