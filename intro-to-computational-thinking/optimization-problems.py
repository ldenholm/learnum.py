# Optimization problems.
# Two components: Objective function for which we want to max or min.
# And a set of constraints for which we bound the problem (no constraints is acceptable).

# Knapsack Problem:
# Suppose we have a vector I of items which have associated weight and value.

# We want to pack a knapsack with such items so that we maximize the total value
# of items packed.

# We are constrained by a total weight no greater than 20kg.
# totalWeight = 20kg.
# Let's describe a symbolic expression representing this mathematically.

# Take a vector V of length n such that V[i] = 1 or 0 which corresponds
# to item I[i] being packed (1 for true, 0 for false).

# We want to maximize the sum of V[i]*I[i].value() <-- that's the dot product
# of the value of each item we packed.

# Constrained in such a way that the sum of weights within the knapsack
# do not exceed the total weight:
# SUM V[i]*I[i].weight() <= totalWeight