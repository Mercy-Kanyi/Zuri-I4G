def find_anagram(word, anagram):
    
    #change words to lowercase
    word = word.lower()
    anagram = anagram.lower()

    #remove whitespaces from the words
    word = word.replace(" ", "")
    anagram = anagram.replace(" ", "")

    if (sorted(word) == sorted(anagram)):
        return True
    else:
        return False
    
print("'Elvis' and 'lives': ", find_anagram("Elvis", "lives"))

