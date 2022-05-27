# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if word == anagram:
        print("same word entered, not an anagram")
        quit()
    word = word.upper()
    anagram = anagram.upper()

    # sort out words in alphabetical order
    word = "".join(sorted(anagram))
    anagram = "".join(sorted(anagram))

    if len(word)==len(anagram) and word == anagram:
        print(True)
    else:
        print(False)

        
    return True
find_anagram("sore", "rose")

