n = 0
e = 0

def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print('n e')
print('- -----------')

for n in range(10):
    e += 1 / fact(n)
    if n < 2:
        print(n, int(e))
    elif n == 2:
        print(n, float(e))
    else:
        print(n, "%.9f" % e)
