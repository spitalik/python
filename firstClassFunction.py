print("################################################")
print("# priklad 1")
print("################################################")

def funkcia():
    print("Hello world 1")

x = funkcia
x()

print("################################################")
print("# priklad 2")
print("################################################")

def function_factory():
    print("Toto je telo funkcie function_factory")
    def hello_world():
        print("Hello world 2")
    return hello_world  # Toto vrati na vystup telo funkcie

print(function_factory())

x = function_factory()
x()
# alebo 
function_factory()()

print("################################################")
print("# priklad 3")
print("################################################")

def adder(x,y):
    return x + y
def substractor(x,y):
    return x - y
def multiplier(x,y):
    return x * y

function_list = [adder, substractor, multiplier]

for function in function_list:
    print(function(1,2))

# alebo cez map
vysledok = list(map(lambda fun: fun(1,2), function_list))
print(vysledok)
# alebo rovno
print(list(map(lambda fun: fun(1,2), function_list)))

print("################################################")
print("# priklad 4")
print("################################################")

def function_wrapper(func, a, b):
    print("Toto je function_wrapper funkcia")
    return func(a, b)

print(function_wrapper(lambda a,b: a+b, 10, 20))