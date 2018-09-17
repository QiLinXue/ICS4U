#-----------------------------------------------------------------------------
# Name: Trump Tweet Finder
# Purpose: Figures out how similar a piece of text is to something Trump would type
#
# References: 	This program uses the dataset from https://factba.se/search where the                   date parameters are from 1-Jan-2018 to 13-Sep-2018
#
# Author:      QiLin Xue
# Created:     13-Sep-2018
# Updated:     17-Sep-2018
#-----------------------------------------------------------------------------

import re # regex
import sys # interactivity

def cleanup(text):
  """
	Function to remove puncutation and clean up a string
		
	Parameters
	----------
	text : string
		The string needed to be cleaned up
  
  Returns
	-------
	string
		Cleaned up version of text with no punctuation, single spaced seperation, and all lowercase
  """

  text = text.replace("’","") # remove fancy apostrophe
  text = text.replace("\'","") # remove normal apostrophe
  text = re.sub(r'[^\w\s]',' ',text) # replace all other punctuation with a space
  text = re.sub(' +',' ',text) # remove double spaces
  text = text.lower() # change everything to lowercase
  return text

# Global Variables which are set outside the wordCount function so recursion doesn't reset them
score = 0
length = 0

def wordCount(tPhrase):
  """
	Recursive function to repeatedly look for identical phrases in trump speech database
		
	Parameters
	----------
	tPhrase : string
		The piece of text the function is looking for
  
  Prints
	-------
	if there are more unmatched words
    prints out the longest chain number for the current string
  if there are no more unmatched words
    prints out the overall score when matched to Trump
  """
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
      # problem lies within how if index is not updated at the end of the loop through trump tweets, it continues on with the next word. end the process first. tyhen continue with the next word
        # If in range AND found a matching pair of words
        if i + index < len(tempTweets) and tempTweets[i+index] == tPhrase[j]:
          print(tempTweets[i+index],tPhrase[j])
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
      print(highestIndex,tPhrase[:highestIndex+1],"hi")
      if original.count(' ') == 0:
        score = score + (1.5**highestIndex)
        highestPossibleScore = 1.5**length

        if highestIndex == 0:
          score = score - 1
        errorMargin = 100*(score/highestPossibleScore)

        if errorMargin > 100:
          print("Your sentence is", errorMargin, "percent similar to what DonaldTrump would tweet in 2018. You have trumped the Trump! (it's not supposed to happen) Please report this issue on github.")
        else:
          print("Your sentence is", errorMargin, "percent similar to what DonaldTrump would tweet in 2018")
          return 0 #Stop
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
      if highestIndex == 0:
          score = score - 1
      errorMargin = 100*(score/highestPossibleScore)

      if errorMargin > 100:
          print("Your sentence is", errorMargin, "percent similar to what DonaldTrump would tweet in 2018. You have trumped the Trump! (it's not supposed to happen) Please report this issue on github.")
      else:
          print("Your sentence is", errorMargin, "percent similar to what DonaldTrump would tweet in 2018")
      return 0; #stop

  # recursion!
  else:
      wordCount(tPhrase)

# Open up file, and save a cleaned up version in variable "tweets"
file = open("trump2018.txt", errors='ignore')
tweets = file.read()
tweets = cleanup(tweets)

# Execute command TODO make it loop through
while 1+1==2:
  inputStatement = input()
  length = inputStatement.count(' ')+1
  wordCount(inputStatement)
