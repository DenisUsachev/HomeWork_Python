# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

number = int(input('Введите шестизначный номер: '))

num = number % 1000

summ1 = num % 10 + num // 10  % 10 + num //100 % 10
summ2 = number % 10 + number // 10  % 10 + number //100 % 10

print('Yes'if summ1 == summ2 else 'No')