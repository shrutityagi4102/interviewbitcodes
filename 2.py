#Integers in Strings

"""Given a string A, consisting of comma-separated positive integers.
Extract the given integers from the string and return an integer array consisting of the integers present in the string.

Note: All given integers will fit in a 32-bit signed integer."""

class Solution:
    def solve(self, A):
        x = A.split(',')
        x1 = [int(i) for i in x]
        return x1
