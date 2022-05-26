# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(sorted(word)== sorted(anagram)):
       print("The two words are anagrams")
       return True
    else:
       print("The two words are not anagrams")
       return False
    
    
     