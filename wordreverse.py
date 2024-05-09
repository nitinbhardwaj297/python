# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"


# def reverse_string(sentence):
#     word = sentence.split()
#     reversing_string = word[::-1]
#     reversed_string = ' '.join(reversing_string)
#     return reversed_string

# reversed_string = reverse_string("hello my name is nitin")
# print(reversed_string)

sentence = "This data is accessible"
word = sentence.split()
print(word)

reverse_string = word[::-1]
print(reverse_string)
reveresed_string = ' '.join(reverse_string)
print(reveresed_string)