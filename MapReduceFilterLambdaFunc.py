numbers = [2, 3, 4, 5, 6]
print(numbers)

def return_power(number, power=2):
    return number ** power

print("################################################")
print("# priklad 1 - standardne programovanie")
print("################################################")

temp = []
for number in numbers:
    temp.append(return_power(number))
print(temp)

print("################################################")
print("# priklad 2 - map")
print("################################################")
# list(...) konstruktor, ktory vyrobi pole z map
temp = list(map(return_power, numbers))
print(numbers)
print(temp)
# to iste
print (list(map(return_power, numbers)))
# lambda
print (list(map(lambda number: number ** 2, numbers)))

print("################################################")
print("# priklad 3 - filter")
print("################################################")
# funkcia iduca do filtra musi vracat tree/false
print (numbers)

def jeCisloParne(number):
    return (number % 2 == 0);

print(list(filter(jeCisloParne, numbers)))    
print(number) #naplnene hore cez for number in numbers:, dobra debilina
print(list(filter(lambda a: a % 2 == 0, numbers)))    

print("################################################")
print("# priklad 3 - reduce")
print("################################################")
from functools import reduce
def sucet(a, b):
    print("a, b:", a, ", ",b)
    return a + b
print(reduce(sucet, numbers))

print("#cez lambda")
print(reduce(lambda x, y: x + y, numbers))

print("################################################")
print("# cez map a reduce vratit z kazdeho cisla v poli jeho faktorial")
print("################################################")
numbers = range(1, 11)
print (numbers)
#print(list(map(lambda a: range(1, a + 1), numbers)))
print(list(map(lambda a: reduce(lambda x, y: x*y , range(1, a + 1)), numbers)))



