import string

def main():
    print("This is the longest word program\nPut in a sentence and we will tell you the longest word in your sentence")
    words = input(str)
    longestWord(words)

def longestWord(sen):
    strippedSentence = sen.translate(str.maketrans("","",string.punctuation))
    splitWords = strippedSentence.split(" ")
    maxLength= 0
    
    for everyWord in splitWords:
        wordLength=len(everyWord)
        if(wordLength>maxLength) and everyWord.isalnum():
            maxLength=len(everyWord)
            largestWord=everyWord
                   
    print(largestWord)

main()

