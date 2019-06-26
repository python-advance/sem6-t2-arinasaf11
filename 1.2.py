from itertools import islice

def fib(a=0, b=1):
    yield a
    while True:
        yield b #функция вернёт генератор
        a, b = b, a + b

start = int(input("От какого числа начать счет " ))
end = int(input("До какого числа вести счет " ))

fib_list = list(islice(fib(), start, end))
print(fib_list)
