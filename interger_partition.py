def partition(number):
    prob = []
    prob.append((number, ))
    for x in range(1, number):  
        for y in partition(number - x):
            prob.append(tuple(sorted((x,) + y)))
    return prob
k = int(input("Enter your number:"))

patterns = partition(k)
print("No of patterns:", len(patterns))
for pattern in patterns:
    print('+'.join([str(v) for v in pattern]))