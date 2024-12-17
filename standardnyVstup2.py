import sys

def get_input():
    print("Zadaj číslo: ")
    x = sys.stdin.readline()
    return int(x)

while True:
    cislo = get_input()
    if cislo == 99:
        break


