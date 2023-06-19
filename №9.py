f = open('9.7588')
k = 0
for s in f:
    a = list(map(int, s.split()))
    povtor = sum(a) - sum(set)

    if len(set(a)) == 5 and (sum(set(a)) - povtor) / 4 <= 2*povtor:
        k += 1

print(k)