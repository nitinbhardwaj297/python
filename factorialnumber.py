def script_fact(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(n,0):
            return n*i - 1

number = script_fact(5)
print(number)