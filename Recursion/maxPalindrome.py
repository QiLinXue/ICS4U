
#-----------------------------------------------------------------------------
# Name:        Max Palindrome
# Purpose:     To calculate the total number of palindromes within a given
#              string recursively
#
# Author:      QiLin
# Created:     6-Nov-2018
# Updated:     6-Nov-2018
#-----------------------------------------------------------------------------

def recursiveCalculate(string,index=0,size=2):
  '''
  Function to count the number of palindromes within the given string

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
    the number of palindromes within yjr given string

  '''
  cutString = string.lower()[index:index+size]

  if len(string) == 1:
    return 1 # If string is only one character
  if size > len(string):
    return 0 # Base Case
  if index+size > len(string):
    return recursiveCalculate(string,0,size+1) # Reloop with greater substring size
  if cutString == cutString[::-1]:
    return recursiveCalculate(string,index+1,size) + 1 # Next substring if palindrome
  else:
    return recursiveCalculate(string,index+1,size) # Next substring if no palindrome

##############################################################################
# Test Function
##############################################################################

import unittest

testCases = [
  ("hello",1),
  ("racecar",3),
  ("raceCar",3),
  ("abracadabra",2),
  ("a",1),
  ("aa",1),
  ("abcdefg",0)
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
    for case in testCases: self.assertEqual(recursiveCalculate(case[0]),case[1])

unittest.main()
