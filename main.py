# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word):

    str1 = input("string1:")
    str2 = input("string2:")
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if sorted_str1 == sorted_str2:
        print("True")
    else:
        print("False")

    return True


find_anagrams("hello")
