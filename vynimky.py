# try:
#     a = 1/0
# except ZeroDivisionError:    
#     print("Delenie nulou")

# try:
#     # a = 1/0
#     pole = [1, 2, 3]
#     pole[10]
# except Exception as e:    
#     print("Nastala chyba:", e)

def podiel(number1, number2):
    pom = 0
    try:
        pom = number1/number2

    except TypeError as e:
        print("Neposielaj mi tu somariny")
    except Exception as e:
        print("Nastala chyba:", e.__str__)
    return pom

print(podiel(1,0))    

    