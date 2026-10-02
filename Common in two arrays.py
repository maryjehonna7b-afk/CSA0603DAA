arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

common = []

for x in arr1:
    if x in arr2:
        common.append(x)

print("Common Elements:", common)
