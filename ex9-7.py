def three_consec(word):
    index = 0
    count = 0
    while index < len(word) - 1:
       if word[index] == word[index+1]:
          count = count + 1
          index = index + 2
       else if:
          return("found!")
       else:
          count = 0
          index += 1
       return("Not found!", count)
