import re # regex
import sys # interactivity

def cleanup(sampleString):
    sampleString = sampleString.replace("’","") # remove fancy apostrophe
    sampleString = sampleString.replace("\'","") # remove normal apostrophe
    sampleString = re.sub(r'[^\w\s]',' ',sampleString) # replace all other punctuation with a space
    sampleString = re.sub(' +',' ',sampleString) # remove double spaces
    sampleString = sampleString.lower() # change everything to lowercase
    return sampleString

score = 0
length = 0

def wordCount(tPhrase):
    global score # global variable
    global length

    original = tPhrase # stores a copy of the original for double checking purposes

    # Occurence of word chains
    highestIndex = 0;
    index = 0

    # Cleanup input text TODO make this only run the first time through loop
    tPhrase = cleanup(tPhrase)

    # Change input text to list
    tPhrase = tPhrase.split()

    # create new variable to store tweets in a list
    tempTweets = tweets.split()

    # Loop through all tweets
    for i in range(0,len(tempTweets)):

        # Loop through all words in the phrase
        for j in range(0,len(tPhrase)):

            # If in range AND found a matching pair of words
            if i + index < len(tempTweets) and tempTweets[i+index] == tPhrase[j]:
                index = index + 1

            # If no more matching pairs found
            else:

                # Record highest index if needed
                if index > highestIndex:
                    highestIndex = index

                # Reset index
                index = 0

                # continue

    # Prints the longest chain found, and the number of words in the chain
    if highestIndex == 0:
        print(highestIndex,tPhrase[:highestIndex+1])
    else:
        print(highestIndex,tPhrase[:highestIndex])

    # keeps all words not found in the previous chain
    del tPhrase[:highestIndex]

    # Increments Score TODO make alg more realistic
    score = score + 1.5**highestIndex

    # Convert back to string
    tPhrase = ' '.join(tPhrase)

    # Checks if recursion is finished
    if not tPhrase or tPhrase == original:
        highestPossibleScore = 1.5**length
        errorMargin = 100*(score/highestPossibleScore)
        # print(highestPossibleScore,score)
        if errorMargin > 100:
            print("Your sentence is", errorMargin, "percent similar to what Donald Trump would tweet in 2018. You have trumped the Trump! (it's not supposed to happen) Please report this issue on github.")
        else:
            print("Your sentence is", errorMargin, "percent similar to what Donald Trump would tweet in 2018")
        return 0;

    # recursion!
    else:
        wordCount(tPhrase)

# Open up file, and save a cleaned up version in variable "tweets"
file = open("trump2018.txt", errors='ignore')
tweets = file.read()
tweets = cleanup(tweets)

# Execute command TODO make it loop through
inputStatement = input()
length = inputStatement.count(' ')+1
wordCount(inputStatement)
