import random

""" Suppose you roll a fair six-sided die two times. 
Let A be the event "the sum of the throws equals 5 
and B be the event "at least one of the throws is a  4 """

# A = (1,4), (2,3), (3,2), (4, 1)
# B = (4,1) ... (4,6), (1,4) ... (6, 4)
# By hand, solve for the probability that the sum of the throws equals 5, 
# given that at least one of the throws is a 4. That is, solve P(A|B).

# P(A|B) = P(A n B)/P(B) = 2/36/(12/36) = (2*36)/(12*36) = 2/12 = 1/6.

# S I M U L A T I O N

rolls = []
roll_count = 10000000
for i in range(roll_count):
    rolls.append((random.randint(1, 6), random.randint(1, 6)))
#print(rolls)
print('len of rolls', len(rolls))
# Now find how many ratio of those being a 4 summing to 5.
#likelihood = len([x for x in rolls if 4 in x]) / len(rolls)
fours = [x for x in rolls if 4 in x]
print('len of pairs containing 4: ', len(fours))
sum_to_5 = [x for x in fours if sum(x) is 5]
print(len(sum_to_5))
num = float(len(sum_to_5))
ratio = num / float(len(fours))
print('likelihood: ', ratio)

# Warning incredibly inefficient simulation lol.