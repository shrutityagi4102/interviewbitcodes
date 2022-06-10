#Word Count

"""Given a string A. The string contains some words separated by spaces.
Return the number of words in the given string."""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        l = A.split(' ')
        l1 = [i for i in l if i!=""]
        return len(l1)
