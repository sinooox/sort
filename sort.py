import random

size = int(input())
lst = []

for _ in range(size):
    lst.append(random.randint(0, 20))

print(lst)

for i in range(size-1):
    for j in range(size - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print(lst)
