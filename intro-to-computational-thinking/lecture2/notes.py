# Implementing a brute force optimization algorithm
# with a search tree.

#    *
#   / \
#  /   \
# *     *

# Start with the root.
# Look at our list of elements to consider.
# Inspect first element.
# Draw a left branch describing consequences of taking this element.
# Draw a right branch describing consequences of NOT taking this element.

# Finally chose the node with the highest value that meets
# our constraints.

# Consider our knapsack problem of a backpack that may hold
# a certain number of foods (bounded by a calories limit).

# First choices: [beer, pizza, burger]
# Go left take the beer.
# Go left take the pizza.
# Go left take the burger.

 #      *          <--- # nodes = 2^0 = 1
 #     / \
 #   [beer]             # nodes += 2^1 = 3
 #   /
 # [pizza, beer]        # nodes += 2^2 = 7
 # /
 #[burger, pizza, beer] # nodes += 2^3 = 15

# Depth first search = go deep on the left to the bottom of the tree.
# Backtrack to n-1 level and consider not taking the element.

# The rightmost branch of this tree contains the path to no items since it always
# chooses not to take the current item. Conversely the leftmost leaf
# of this tree contains all of the items.
# After traversing this tree we may choose the optimal leaf meeting the constraints.

# Computational complexity of this algorithm. To know the asymptotic complexity we
# must know the number of nodes within the tree. The levels in the tree correspond
# to the number of items in our problem. For example with the burger, pizza, and
# beer we have n+1 levels (incl root).

# How many nodes at each level. 2**n levels. Number of nodes at level i = 2**i.
# Total number of nodes in the tree = SUM(2^i) for i in [0, n].

# Now we can optimize this search by prematurely exiting a depth first search
# when we exceed the bounding constraint.

# The worst case computational complexity of this search is 2^n+1 = 2^n * 2^1 = O(2^n).


# Use cases for dynamic programming and memoization:

# Problems with optimal substructure. A globally optimal
# solution may be found by combining optimal solutions to local
# subproblems. Think fibonnaci function which solves two
# smaller problems independently of eachother then combine the
# solutions.

# Overlapping subproblems. The subproblems must be computed
# multiple times. Otherwise if we create a memo for every
# problem but never require the solutions to those problems
# again, there is no benefit to memoization.