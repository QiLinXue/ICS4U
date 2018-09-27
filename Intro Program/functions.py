import re # regex
print("hi")
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

  text = text.replace("’","") # remove fancy apostrophe with no space
  text = text.replace("\'","") # remove normal apostrophe with no space
  text = text.replace("_"," ") # remove underscore with space (regex doesn't catch it)
  text = re.sub(r'[^\w\s]',' ',text) # replace all other punctuation with a space
  text = text.replace("  ", " ") # remove double spaces
  text = text.lower() # change everything to lowercase
  if text[-1:] == ' ': text = text[:-1] # Remove last character if whitespace

  return text