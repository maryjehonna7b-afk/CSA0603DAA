arr = [3, 1, 2, 3, 1, 3]
k = 2

count = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and (i * j) % k == 0:
            count += 1

print("Number of valid pairs:", count)
