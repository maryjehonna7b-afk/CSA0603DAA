arr = [1, 2, 1]

total = 0

for i in range(len(arr)):
    distinct = set()

    for j in range(i, len(arr)):
        distinct.add(arr[j])
        total += sum(x * x for x in distinct)

print("Sum of squares of distinct elements:", total)
