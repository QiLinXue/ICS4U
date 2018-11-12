#-----------------------------------------------------------------------------
# Name:        Mirror Palindrome
# Purpose:     To calculate the total number of mirro palindromes within a given
#              string recursively
#
# Author:      QiLin
# Created:     6-Nov-2018
# Updated:     12-Nov-2018
#-----------------------------------------------------------------------------

m = lambda s,i=0,z=2: 0 if(z>len(s) and not len(s)==1) else 1 if s in list("ilmnotuvwx") else 0 if len(s)==1 else m(s,0,z+1) if i+z > len(s) else m(s,i+1,z)+1+(len(__import__('re').findall("(i|[l-o]|[t-x])",s)) if(z==2 and i==0) else 0) if(s.lower()[i:i+z][:len(s.lower()[i:i+z])//2].translate(str.maketrans("bdpqsz","dbqpzs"))[::-1]==s.lower()[i:i+z][__import__('math').ceil(len(s.lower()[i:i+z])/2):] and (len(s.lower()[i:i+z])%2==1 or s.lower()[i:i+z][len(s.lower()[i:i+z])//2] in list("ilmnotuvwx"))) else m(s,i+1,z)+(len(__import__('re').findall("(i|[l-o]|[t-x])",s)) if(z==2 and i==0) else 0)

import math
def recursiveCalculate(s,original="",taken=None):
  '''
  Function to count the number of mirrordrome within the given string

  Parameters
  ----------
  s: str
    the substring of the original to test if it is a palindrome
  original: str
    the original string
  taken: str list
    a list of substrings that have successfully been tested as a mirrordrome
  
  Returns
  -------
  int:
    the number of palindromes within the given string

  '''
  if taken == None: taken, original = [], s # Run first time
  if len(s) == 0: return 0 # Base Case

  # Flip First Half
  firstHalf = s[:len(s)//2].translate(str.maketrans("bdpqsz","dbqpzs"))[::-1]
  secondHalf = s[math.ceil(len(s)/2):]

  n = 0
  if not original.count(s) <= taken.count(s) and firstHalf == secondHalf:
    n = 1
    if len(s) % 2 == 1 and s[len(s)//2] not in list("ilmnotuvwx"):
      n = 0
    else:
      taken.append(s)
  
  return recursiveCalculate(s[:len(s)-1],original,taken) + recursiveCalculate(s[1:],original,taken) + n

##############################################################################
# Test Function
##############################################################################

import unittest

testCases = [
  ("dob",2),
  ("linnil",9),
  ("totally",7),
  ("sxz",2)
]

class TestMaxPalindrome(unittest.TestCase):
  '''
  Class to test the mirror palindrome function
  '''
  def test_palindrome(self):
    '''
    Procedure to check for errors in proper recursion calculator
    '''
    for case in testCases:
      self.assertEqual(recursiveCalculate(case[0]),case[1])

  def test_oneliner(self):
    '''
    Procedure to check for errors in one liner mirror palindrome
    '''
    for case in testCases:
      self.assertEqual(m(case[0]),case[1])
unittest.main()
