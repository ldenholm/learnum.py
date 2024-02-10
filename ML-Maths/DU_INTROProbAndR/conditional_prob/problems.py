from math import comb
""" Example 
In a factory there are 100 units of a certain product, 5 of which are defective. 
We pick three units from the 100 units at random. What is the probability that 
none of them are defective? """

# 1/20 are defective. 1 - 1/20 = p(not defective) = 19/20.
# Let A be the event the first pick is not defective: P(A) = 19/20
# Let B be the even the second pick is not defective. Given that A has occurred
# the sample space has changed. There are now 99 units, 5 of which are defective,
# leaving 94 not defective. 

# P(A) = 1/20
# P(B|A) = 94/99
# P(A n B) = 0.9
# P(A n B n C) = P(A)*P(B|A)*P(C|B,A)
#              = 95/100 * 94/99 * 93/98

# The probability the first and second picks correspond to the set (A n B).
# P(A n B) = P(B|A)P(A). P(B|A) = 94/99. P(A n B) = 94/99 * 95/100 ~ 0.9

# Note the general formula for this is: P(A n B n C n N...) = P(A)*P(B|A)*P(C|A,B)*P(N|A,B,C,..)

# Let C be the event the third pick is also not defective.
# P(A n B n C) = P(A)*P(B|A)*P(C|A n B)
# P(C|A n B) = 93/98 * P(A n B) = 0.85%

# Now how do we solve this using counting?
# Well getting 3 non defective units out of 100 is the same thing as
# 1 - all the ways to choose 3 defective units

# So P(no defective units chosen) = 1 - P(only defective units chosen)

# Total units to pick from = 100
# There are 5 defective units, and our experiment involves picking 3.
ans = 1 - ((comb(5,3)/100) + (comb(4,2)/99)) + (comb(3,1)/98)
print('probability of all 3 choices not having defects = ', ans)