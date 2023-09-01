import sys

def count(n: int):
    res = 0
    while n > 0:
        if n % 2:
            res += 1
        n = n // 2
    return res


print(count(int(sys.argv[1])))
