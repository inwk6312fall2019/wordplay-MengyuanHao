#exercise 9-1
def my_wordlist():
   t = []
     my_wordlist = open('words.txt')
       for line in my_wordlist:
         word = line.strip()
           if len(word) > 20:
       print(word)
   
#exercise 9-2
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True
def percentage(word,letter):
   i = 0
   t = total number of words
    for letter in word:
        if e in forbidden:
           i += 1
        else:
           return i
           
 ans = i / t * 100%
 print (ans)
 
 #wxercise 9-3
 def avoids(word, forbidden):
    for letter in word:
        if e in forbidden:
            return False
    return True
 print(word)
 
 #exercise 9-4
 def uses_only(word,available):
     for letter in word:
         if acefhlo not in avaliable:
              return False
         elif Hoe alfalfa not in avaliable:
              return True
         else:
              return True
             
#exercise 9-5
def uses_all(word,required):
    for letter in required:
        if aeiou not in word:
             return False
        elif aeiouy not in word:
             return False
        else:
             return True
             
#exercise 9-6
def is_abecedarian(word):
    i = 0
    while i < len(word) - 1:
      if word[i+1] < word[i]:
         return False
      i = i+1
    return True
print(i)

#exercise 9-7
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

#exercise 9-8
def is_palindrome(word):
    i = 0
    j = len(word) - 1
    while i<j:
         if word[i] != word[j]:
            return False
         i = i + 1
         j = j - 1
    return True
 def check(n):
    i = 100000
    while i <= 999999:
        if check(i):
        i = i + 1
 print(i)
 
 #exercise 9-9
 def is_reverse(x,y):
    while True:
     val[x],val[y] = val[y],val[x]
      return is_reverse(word,word)

#exercise 10-1
def nested_sum(list):
    total = 0
    for item in list:
        if isinstance(item,int):
           total = total + item
        elif isinstance(item,list):
           total = total + nested_sum(item)
    return total
    
 list = [[12],[13],[5,4]]
 print(nested_sum(list))
 
 #exercise 10-2
 def cumsum(t):
     sum = 0
     ans = []
     for n in t:
         sum = sum + n
         ans.append(sum)
     return ans
 
#exercise 10-3
def middle(t):
     return t[1:-1]
 
#exercise 10-4
def chop(t):
     del t[0]
     del t[-1]
     return t

#exercise 10-5
def is_sorted():
    i = 0
    while i < len(word) - 1:
          if word[i] < word[i+1]
             return True
          else:
             return False
    return t == sorted(t)
    
#exercise 10-6
def is_anagram(word1,word2):
    return sorted(word1) == sorted(word2)

#exercise 10-7
def has_duplicates(sl):
    for i in range(len(word)-1):
        if word[i] < len(word):
           return True
    return False

     
 
