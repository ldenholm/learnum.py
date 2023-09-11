###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Lochie
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always an egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    """
    I'm just going to rewrite the problem statement because honestly the text above ^ is confusing.
    We must return the smallest set of eggs whose weight sum equals the total weight given. 
   
    How can we tackle this problem and model it mathematically? The question is asking us to find a solution which
    optimizes for the least number of eggs required to meet the weight constraint. I am considering representing 
    the problem with a binary search tree but examples I have seen use a recursive function instead.

    The issue with using a binary tree for this problem is finding the right way to represent decisions. 
    In the 0/    1 knapsack problem each decision to add or ignore an item was a boolean choice. 

    What if we take a step back and consider more generally applying a graph to this problem. What would it look
    like? Well we could begin with a root node. The root node has: egg weights, weight to achieve. Our graph
    G = (V, E) has Vertices with information and Edges represent the associated cost (in weight) of following a 
    path. If the path costs more than the desired weight then that path is not chosen.

    Or do you start at the root node and then divide by the egg weight and choose the path with the highest
    number? Doing it this way means you go down to the bottom left of the graph and this represents taking
    the most multiples n of the egg weight w such that (n*w <= desired_weight).  

    Each node performs the following calculation: for each weight w in the list: divide desired_weight by 
    w. Choose the smallest factor f, f represents the largest factor. and therefore if we build the sum
    using the largest to smallest weights in order we will arrive at the optimal solution. Note the assumption
    in the last sentence is incorrect. To arrive at an optimal solution we must compute every combination of
    eggs such that they reach the total weight then return the set with the least eggs.

    We can implement a solution by constructing a binary tree then using depth first search to find
    all the possible combinations of eggs which satisfy the weight constraint. Then we can choose the set
    with the minimum size. We can create memos for each computed set so we avoid unecessary recomputation.

    We will implement a recursive function which computes combinations of eggs that equal the provided 
    weight then return the set with least length. We will use a dictionary to store memos to avoid unecessary 
    recomputations. 
    """
    pass

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
