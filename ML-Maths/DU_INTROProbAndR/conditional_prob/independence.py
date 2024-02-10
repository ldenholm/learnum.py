"""
I pick a random number from {1,2,3,⋯,10}, and call it N. 
Suppose that all outcomes are equally likely. Let A be the event that N 
is less than 7 , and let B be the event that N is an even number. 
Are A and B independent?
"""
# If A & B are independent then:
# P(A n B) = P(A)P(B)
# A = {1, 2, 3, 4, 5, 6}, P(A) = 6/10 = 0.6
# B = {2, 4, 6, 8, 10} = 5/10 = 0.5
# P(A n B) = {2, 4, 6} = 3/10 = P(A)P(B) = 6/10 * 3/10 = 18/100 = 0.3
# P(A n B) = P(A)P(B) is true so yes they are independent.

"""
Let us generalize this phenomenon to n events. For n events to be
independent the following condition must hold true:
- P(A_1 n A_2 n A_3 n ... n A_m) = P(A_1)P(A_2)P(A_3)...P(A_m)
"""

# Example 1.2.1
# I toss a coin repeatedly until I observe the first tails at which point I stop. Let X
# be the total number of coin tosses. Find P(X=5).

# P(X=5) is the probability we toss the coin five times and land heads.
# Let A_1 be the event the first toss is heads, ... A_5 be the event 5th toss is heads.
# We wish to solve P(A_1 n A_2 n A_3 n A_4 n A_5) = P(A_1)P(A_2)P(A_3)P(A_4)P(A_5)
# Note it's also just n^r with n = 2, r = 5, since 1/2 * 1/2 * 1/2 * 1/2 * 1/2 is the 
# outcome we are interested in.

# P(X=5) = 1/32
# Note the encoded string describing this outcome looks like this: {HHHHT}