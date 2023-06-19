def convert(number, base):
    digits = '0123456789ABC'
    if number == 0:
        return '0'
    result = ''
    while number > 0:
        digit = digits[number % base]
        result = digit + result
        number = number // base
    return result

def in3(x):
    s = ''
    while x != 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]

for n in range(1, 1000):
    n3 = in3(n)
    if n % 3 == 0:
        n3 = n3 + n3[-2:]
    else:
        ost = n % 3 * 5
        n3 = n3 + in3(ost)
    r = int(n3, 3)
    if r >= 146:
        print(n)
        break