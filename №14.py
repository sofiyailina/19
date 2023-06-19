for x in '0123456789abc':
    a = int('9897' + x + '21', 13)
    b = int('12' + x + '023', 13)
    if (a-b) % 12 == 0:
        print((a-b) // 12)