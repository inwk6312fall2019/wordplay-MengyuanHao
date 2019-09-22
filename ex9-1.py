def my_wordlist():
   t = []
     my_wordlist = open('words.txt')
       for line in my_wordlist:
         word = line.strip()
           if len(word) > 20:
       print(word)
