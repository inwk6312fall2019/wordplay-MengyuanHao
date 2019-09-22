def uses_all(word,required):
    for letter in required:
        if aeiou not in word:
             return False
        elif aeiouy not in word:
             return False
        else:
             return True
