#Collatz Conjecture

"""Given two integers A and B, where A is the first element of the sequence then find Bth element of the sequence.
If the kth element of the sequence is X then k+1th element calculated as:
if X is even then next element is X/2.
else next element is 3×X + 1."""

class Solution:
    def solve(self, A, B):
        for i in range(1,B):
            if A%2==0:
                A = A/2
            else:
                A = (3*A) + 1
        return A
