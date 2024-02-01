import json
import timeit
from matplotlib import pyplot as plt
import numpy as np

def changeSize(inputData, records):
    for i in range(records):
        inputData[i]["payload"]["size"] = 35

if __name__ == "__main__":
    f = open('large-file.json', encoding="utf8")
    data = json.load(f)
    f.close()

    times = timeit.repeat(lambda: changeSize(data,1000), repeat=1000, number=1)

    plt.hist(times, color='w', edgecolor = 'r',)
    plt.xlabel("Time(s)")
    plt.ylabel("Number of Trials")

    plt.savefig("output.3.3.png")
