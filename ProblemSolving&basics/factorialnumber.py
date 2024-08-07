def script_fact(n):
    for i in range(n,0):
        var = n*i-1
        count +=var
        return count

number = script_fact(5)
print(number)