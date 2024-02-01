import timeit

def fact(n):
    sum = 1
    for i in range(1,n+1):
        sum = sum * i
    
    return sum

def forLoop():
    for i in range(100):
        num = fact(i)

def listComprehension():
    num = [fact(i) for i in range(100)]

tm =timeit.timeit(lambda: fact(100), number=10000)
print("The average time of fact(100) is: ", tm)

tm =timeit.timeit(lambda: forLoop(), number=1000)
print("The average time for using for loop is: ",tm)
tm = timeit.timeit(lambda: listComprehension(), number=1000)
print("The average time for using list comprehension is: ", tm)