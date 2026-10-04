arr = ["apple", "hello", "madam", "level", "world"]

for word in arr:
    if word == word[::-1]:
        print("First Palindromic String:", word)
        break
