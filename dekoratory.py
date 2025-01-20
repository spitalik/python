print("################################################")
print("# priklad 1")
print("################################################")
visitor = {
    "name": "Michal",
    "age": 13
}

def play_movie():
    print("I am playing movie!!!")

def check_adult(func):

    def wrapper():
        if visitor["age"] >= 18:
            func()
        else:
            print("Nemaš vek na spustenie tejto funkcionality")    
    
    return wrapper

# obalenie dekoratorom
play_movie = check_adult(play_movie)
play_movie()

# pouzitie sintactic sugar, aby som neusel používať obaľovač
@check_adult
def show_picture():
    print("I am showing picture!!!")

show_picture()

print("################################################")
print("# priklad 2")
print("################################################")

import datetime
import time

def duration_checker(func):
    def wrapper(*args):
        print(datetime.datetime.now())
        return_value = func(*args)
        print(datetime.datetime.now())
        return return_value
    return wrapper

@duration_checker
def sleeper(seconds, name):
    time.sleep(seconds)
    return "Dobre ranko " + name

pom = sleeper(1, "Michal")    
print(pom)











