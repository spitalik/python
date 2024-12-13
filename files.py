# priklad 1
print("priklad 1")
file_reader = open('FileFolder/dataFile.txt')
print(file_reader)
file_reader.close
print("")

# priklad 2 - lepsdie cez content manager
print("priklad 2")
with open('FileFolder/dataFile.txt','r') as file:
    print(file.readlines())
    print(type(file.readlines()))
    
print("")

# priklad 3 - čítanie po riadkoch
print("priklad 3")
with open('FileFolder/dataFile.txt','r') as file:
    for line in file.readlines():
        print(line, end="")
print("")

# priklad 4 - zápis po riadkoch
print("priklad 4")
with open('FileFolder/newDataFile.txt','w',encoding='utf-8') as file:
    for line in ["Jožo","Mišo","Fero"]:
        file.write(line)
        file.write("\n")

print("")

# priklad 5 - append do existujúceho
print("priklad 4")
with open('FileFolder/newDataFile.txt','a',encoding='utf-8') as file:
    for line in ["Valika","Violka","Tobi","Lydka"]:
        file.write(line)
        file.write("\n")

print("")


print("")










