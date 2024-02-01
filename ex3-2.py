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

    listLengths = [1000,2000,5000,10000]
    avg = []
    for i in listLengths:
        tm = timeit.timeit(lambda: changeSize(data,i), number=100)

        avg.append(tm/100)
        print("The average time for", i, "is", tm/100)



    #Produce a linear regression plot
    slope, intercept = np.polyfit(listLengths, avg, 1)
    plt.scatter(listLengths, avg)
    linevalues = [slope * x + intercept for x in listLengths]
    plt.plot(listLengths, linevalues, 'r')

    # Save the plot to a file named output.3.2.png
    plt.xlabel('Number of Records')
    plt.ylabel('Average Processing Time (seconds)')
    plt.title('Linear Regression: Number of Records vs. Average Processing Time')
    plt.savefig('output.3.2.png')

    print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))