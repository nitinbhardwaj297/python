def odd_string(number):
    max_odd = -1

    for digit in str(number):
        if int(digit) %2 !=0 and int(digit) > max_odd:
            max_odd = int(digit)

    return max_odd 
print(odd_string('451'))
print(odd_string('233445533'))
print(odd_string('-1'))


    


