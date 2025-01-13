#1
result = [number for number in range(2, 22) if number % 2 == 0]
print(result)

#2
result = [(number if number % 2 == 0 else number * 10) for number in range(0, 20)]
print(result)

#3
string = "informatika s Misom je cool";
print (string.split())
print ([len(word) for word in string.split()])

arr = ["This", "is", "string"]
print(arr)
print(" ".join(arr))

