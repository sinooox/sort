import random, time

f = open('time.txt', 'w')

def gen(size):
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

def quickSort(lst):
    if len(lst) <= 1:
        return lst
    else:
        q = random.choice(lst)
        L = []
        M = []
        R = []
        for element in lst:
            if element < q:
                L.append(element)
            elif element > q:
                R.append(element)
            else:
                M.append(element)

        return quickSort(L) + M + quickSort(R)

size = int(input('enter size: '))
lst = gen(size)

startFirst = time.time()
lst2 = bubble(lst)
endFirst = time.time() - startFirst
f.write(str(endFirst) + '\n')

startSecond = time.time()
lst3 = sort(lst)
endSecond = time.time() - startSecond
f.write(str(endSecond) + '\n')

startThird = time.time()
lst4 = quickSort(lst)
endThird = time.time() - startThird
f.write(str(endThird) + '\n')

f.close()
