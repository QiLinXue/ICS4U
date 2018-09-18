#-----------------------------------------------------------------------------
# Name: Trump Tweet Finder
# Purpose: Figures out how similar a piece of text is to something Trump would type
#
# References: 	This program uses the dataset from https://factba.se/search where the date parameters are
#               1-Jan-2018 to 13-Sep-2018
#
# Author:      QiLin Xue
# Created:     13-Sep-2018
# Updated:     17-Sep-2018
#-----------------------------------------------------------------------------

# ▀▀█▀▀░█▀█░█░░█░█▄░▄█░█▀█░░
# ░░█░░░██▀░█░░█░█░▀░█░█▀▀░░
# ░░█░░░█░█░█▄▄█░█░░░█░█░░░░

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

import re # regex
import sys # interactivity

#-----------------------------------------------------------------------------
# Functions
#-----------------------------------------------------------------------------

# Global Variables which are set outside the wordCount function so recursion doesn't reset them
score = 0
length = 0

def cleanup(text: str) -> str:
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

def wordCount(tPhrase: str) -> str:
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

  # global variables so they can be accessed outside the function
  global score # the final score that is outputted
  global length # the original length of the input string

  # Occurence of word chains
  highestIndex = 0; #highest index of words possible, can only increase
  index = 0 #temporary index, can change often

  # Cleanup input text
  tPhrase = cleanup(tPhrase) # Removes punctuation and unneeded spaces
  original = tPhrase # stores a copy of the original for double checking purposes
  tPhrase = tPhrase.split() # Change input text to list
  tempTweets = tweets.split() # create new variable to store tweets in a list

  # Loop through all words in phrase
  for i in range(0,len(tPhrase)):

      # Loop through all tweets
      for j in range(0,len(tempTweets)):

          # If in range AND found a matching pair of words
          if i + index < len(tPhrase) and tempTweets[j]  == tPhrase[i+index]:
              index = index + 1

          # if no more matching pairs found
          else:
              if index > highestIndex:
                  highestIndex = index
              index = 0

      # If tweets are all looped and still no match found, break from tPhrase loop
      if highestIndex == 0:
          break;

  # Prints the longest chain found, and the number of words in the chain
  if highestIndex == 0:
      print(highestIndex,tPhrase[:highestIndex+1])

  else:
      print(highestIndex,tPhrase[:highestIndex])

  # keeps all words not found in the previous chain
  del tPhrase[:highestIndex]

  # Increments Score TODO make alg more realistic (too easy for short sentences, too hard for longer ones)
  highestPossibleScore = 1.8**length
  score = score + 1.8**highestIndex

  if highestIndex == 0: # 1.5**0 = 1 which is unfair
      score = score - 1

  # Convert back to string
  tPhrase = ' '.join(tPhrase)


  # Checks if there is no change
  if tPhrase == original:

      # Deletes first item
      tPhrase = tPhrase.split(' ')
      del tPhrase[:highestIndex+1]
      tPhrase = ' '.join(tPhrase)

  # Checks if recursion is finished
  if not tPhrase:

      # Oytputs Result
      errorMargin = 100*(score/highestPossibleScore) # Converts score to percentage
      print("Your sentence is", errorMargin, "percent similar to what DonaldTrump would tweet in 2018")
      return 0; #endpoint

  # recursion!
  wordCount(tPhrase)

#-----------------------------------------------------------------------------
# Main Code
#-----------------------------------------------------------------------------

# Open up file, and save a cleaned up version in variable "tweets"
file = open("trump2018.txt", errors='ignore')
tweets = file.read()
tweets = cleanup(tweets) # cleanup

# Execute command and loop
while True:

  # Get Input
  inputStatement = input()
  length = inputStatement.count(' ')+1

  # Run Main Function
  wordCount(inputStatement)

  # Reset Score
  score = 0
