
def summ(a,b):
    if a < 0 or b < 0:
        return 0
    if b == 0:
        return a
    return summ(a + 1,b - 1)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(summ(a,b))