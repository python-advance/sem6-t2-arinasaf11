lst = [0, 1, 1]
n = int(input('Введите количество чисел: '))
fib1, fib2 = 1, 1

if n < 3:
  print(lst)
else:
  for i in range(3, n):
   fib1, fib2 = fib2, fib1 + fib2
   lst.append(fib2)
print(lst)
