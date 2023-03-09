
def degree(n, deg):    
    if deg == 0:
        return 1
    if deg == 1:
        return n  
    return n * degree(n, deg - 1)

n = int(input('Введите число: '))
deg = int(input('Введите степень: '))

print(degree(n, deg))