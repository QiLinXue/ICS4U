#-----------------------------------------------------------------------------
# Name:        Mirror Palindrome
# Purpose:     To calculate the total number of mirro palindromes within a given
#              string recursively
#
# Author:      QiLin
# Created:     6-Nov-2018
# Updated:     8-Nov-2018
#-----------------------------------------------------------------------------

selfReflection = ['i', 'l', 'm', 'n', 'o', 't', 'u', 'v', 'w', 'x']
doubleReflection = [('b','d'),('p','q'),('s','z')]

def recursiveCalculate(string,index=0,size=2):
  '''
  Function to count the number of mirro palindromes within the given string
  Parameters
  ----------
  string: str
    the string to search for palindromes
  index: int
    the starting index of each substring
  size: int
    the size of each substring
  
  Returns
  -------
  int:
    the number of palindromes within the given string
  '''

  n = 0

  if size == 2 and index == 0:

    for rep in doubleReflection: string = string.replace(rep[0], rep[1])
    for letter in string:
      if letter in selfReflection:
        n = n + 1
    
  
  cutString = string.lower()[index:index+size]

  if len(string) == 1:
    return 1 # If string is only one character
  if size > len(string):
    return 0 # Base Case
  if index+size > len(string):
    return recursiveCalculate(string,0,size+1) # Reloop with greater substring size

  if isMirrorDrome(cutString):
    return recursiveCalculate(string,index+1,size) + 1 + n # Next substring if palindrome
  else:
    return recursiveCalculate(string,index+1,size) + n # Next substring if no palindrome

def isMirrorDrome(string):
  '''
  Function to check if string is a mirror drome
  ----------
  string: str
    the string to check if it's a mirror drome
  
  Returns
  -------
  bool:
    True if mirrordrome
    False if not
  '''
  length = len(string)
  if length % 2 == 0: isOdd = False 
  else: isOdd = True

  firstHalf = string[:length//2]
  secondHalf = string[1+length//2:]

  for rep in doubleReflection:
    if firstHalf == firstHalf.replace(rep[0], rep[1]):
      firstHalf = firstHalf.replace(rep[1], rep[0])
    else:
      firstHalf = firstHalf.replace(rep[0], rep[1])


  if firstHalf[::-1] == secondHalf:
    if isOdd:
      if string[length//2] in selfReflection:
        return True
      else:
        return False
    
    return True

  return False

##############################################################################
# Test Function
##############################################################################

import unittest

testCases = [
  ("dob",2),
  ("linnil",9),
  ("totally",7)
]

class TestMaxPalindrome(unittest.TestCase):
  '''
  Class to test the max palindrome function
  '''
  def test_palindrome(self):
    '''
    Procedure to check for errors in recursion calculator
    
    1. Loop through all cases of testCases and check if #of palindromes match
    ------------
    Verification
    2. Verify no errors occured
    '''
    for case in testCases:
      self.assertEqual(recursiveCalculate(case[0]),case[1])

unittest.main()
