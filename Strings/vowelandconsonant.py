
def vowelsandconsonants(string):


    vowels_count=0
    consonant_count=0
    vowel = ['a','e','i','o','u']
   
    string = string.replace(" ","").lower()
    
    for char in string:
        if char in vowel:
            vowels_count+=1
        else:
            consonant_count+=1
    
    return vowels_count, consonant_count

text = " hi this side nitin "
vowels,consonants = vowelsandconsonants(text)
print("vowels: ", vowels)
print("consonants: ", consonants)