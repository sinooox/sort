import random

def gen():
    size = int(input())
    lst = []

    for _ in range(size):
        lst.append(random.randint(0, 20))

    return lst

def bubble(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


def sort(lst):
    n = len(lst)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if lst[j] < lst[m]:
                m = j
        lst[i], lst[m] = lst[m], lst[i]

    return lst

lst = gen()
print(sort(lst))

