#Pangram Check
"""Given a sentence represented as an array A of strings.
Chech if it is a pangram or not.
A pangram is a unique sentence in which every letter of the alphabet is used at least once."""

class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        a = ''.join(A)
        l = [i.lower() for i in a]
        s = list(set(l))
        if len(s) == 26:
            return 1
        else:
            return 0
