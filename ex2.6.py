import timeit

def fact_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fact_list_com(n):
    if n ==0:
        return 1
    else:
        return n * fact_list_com(n-1)

if __name__ == "__main__":
    
    # check the timed functions of both approaches  
    timed_function_loop = lambda: [fact_loop(n) for n in range(101)]
    timed_function_list_com = lambda: [fact_list_com(n) for n in range(101)]

    # executes these functions 1000
    time_loop = timeit.timeit(timed_function_loop, number=1000)
    time_list_com = timeit.timeit(timed_function_list_com, number=1000)

    print(f"Time taken for factorial using a for loop: {time_loop:.6f} seconds")
    print(f"Time taken for factorial using list comprehension: {time_list_com:.6f} seconds")