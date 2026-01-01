arr = [10, 5, 10, 15, 10, 5]
d = dict()
for i in arr:
    d[i] = d.get(i, 0) + 1
print(d)