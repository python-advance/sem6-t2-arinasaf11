from itertools import islice

class fib:
  def __init__(self):
    self.elem = 0
    self.numb = 1
 
  def __iter__(self):
    return self
 
  def __next__(self): #Метод __next__ возвращает следующий по порядку элемент итератора
    value = self.numb
    self.numb += self.elem
    self.elem = value
    return value

f = fib()

start = int(input("От какого числа вести счет \t" ))
end = int(input("До какого числа \t" ))

print(list(islice(f, start, end)))
