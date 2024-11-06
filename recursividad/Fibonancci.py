import timeit


def procesCurrent(n,a,b):
    c = 0
    for i in range(1,n):
        c = a + b
        a = b
        b = c
    return c

def recursividad(n,a,b):
    if n<=1:
        return b
    return recursividad(n - 1, b, a + b)

n = int(input("inglrese un valor n: "))

print(f"Sin recursividad: {procesCurrent(n,0,1)}")


print(f"Con recursividad: {recursividad(n,0,1)}")
print(timeit.timeit('recursividad(n,0,1)', setup="from __main__ import recursividad(n,a,b)", number = 500)
)

