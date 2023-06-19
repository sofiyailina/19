otv = 0
for post1 in 'пятница':
    for post2 in 'пятница':
        for post3 in 'пятница':
            for post4 in 'пятница':
                for post5 in 'пятница':
                    s = post1 + post2 + post3 + post4 + post5
                    if s[0] != 'н' and s.count('я') == 1:
                        otv += 1
print(otv)
