#  Найдите сумму цифр трехзначного числа.


number = int(input('Введите трёхзначное число: '))
summ = 0

summ = number % 10 + number // 10  % 10 + number //100 % 100
print(summ)