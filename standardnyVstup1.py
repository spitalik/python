import fileinput


for line in fileinput.input():
    print("Zadal si že:", line, end="")