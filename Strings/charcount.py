def countchar(string):
    char = input("enter the char: ")

    count_char = 0

    for i in string:
        if char in string:
            count_char+=1
        else:
            continue
            
    return count_char

string1 = "nitin"
output = countchar(string1)
print(f"The character '{char}' appears {output} times in the string.")



