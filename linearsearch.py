arr = []

n = int(input("enter the range: "))
number = int(input("enter the number: "))
for i in range(n):
    element = int(input())
    arr.append(element)

print("this is the array: ", arr)

for i in arr:
    if (i == number ):
        print("this is the element ", i )
        break

    
