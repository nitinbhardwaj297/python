def palin(sentence):
    if sentence == sentence[::-1]:
        print(sentence, " is a palindrome.")
    else:
        print(sentence, " isn't a palindrome.")



palin("PALINDROME")




