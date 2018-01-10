word1=input("Enter a Sentence :")
word1=word1.upper()
word2=word1.split()

for word in word2:
    print(word[0],end="")