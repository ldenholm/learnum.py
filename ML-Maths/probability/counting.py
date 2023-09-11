A deck of 52 cards has 13 ranks (2, 3, . . . , 9, 10, J, Q, K, A) and 4 suits (♥, ♠, ♦, ♣,). A poker hand consists of 5 cards. A one-pair hand consists of two cards having one rank and three cards having three other ranks, e.g., {2♥, 2♠, 5♥, 8♣, K♦}.

What is the probability of drawing a one-hand pair? We can use the naive definition of probability to arrive at an answer. We can count the total number of favourable outcomes and divide by the total number of outcomes.

In this case favourable outcomes correspond to the total number of one-hand pairs possible to draw in a deck. We can count the total number of one-hand pairs in a deck using the following formula:

We need to count total ways to choose 3 distinct ranks (of card) from a total of 13. Multiplied by the total number of ways to choose 2 (of the same) ranks from the remaining 10 ranks. The 2 identical ranks can be treated as one so the second term becomes 10Choose2.

Verify De Morgan's Laws for S = {1, 2, 3, 4, 5}. A = {1, 2, 3}. B = {3, 4}.
Theorem: (A union B)'s complement is equal to the intersection of A's complement and B's complement.

A's compl = {4, 5}. B's compl = {1, 2, 5}.
(AuB)'s compl = {5}.
(A compl intersect B's compl) = {5}.
Notice (AuB)'s compl == (A compl intersect B's compl) = {5}.

Second theorem:
(A intersect B)'s compl == A's compl union B's compl.
(A intersect B)'s compl = {1, 2, 4, 5}.
A's compl union B's compl = {1, 2, 4, 5}.
The equality holds:
(A intersect B)'s compl == A's compl union B's compl = {1, 2, 4, 5}.
