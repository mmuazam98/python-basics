def sort_tuple(tup):
    lst = len(tup)
    for i in range(0, lst):

        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup


# tup = [(1, 7), (1, 3), (3, 4, 5),
#        (2, 2)]

i = input('Enter a list of tuples: ')

l = []

for tup in i.split('),('):
    tup = tup.replace(')', '').replace('(', '')
    l.append(tuple((tup).split(',')))

print(sort_tuple(l))
