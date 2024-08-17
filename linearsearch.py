## linear search 

arr = []
n = int(input("enter the range: "))
number = int(input("enter the number: "))

for i in range(n):
    element = int(input())
    arr.append(element)

print("this is my array: ", arr)

for i in arr:
    if (i == number):
        print("element is present ",i)
    else:
        break

