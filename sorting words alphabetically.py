string=str(input("enter the string"))

words=[word.lower() for word in string.split()]
words.sort()

print("The sorted words are:")
for word in words:
    print(word)
