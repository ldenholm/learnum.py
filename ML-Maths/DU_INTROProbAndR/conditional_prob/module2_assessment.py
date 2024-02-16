import math

""" The CU Boulder triathlon team has 12 women and 9 men. The team is going to a race and can only enter 5 participants. What is the probability of randomly selecting a race squad of 5 participants with exactly 3 women? Round your answer to three decimal places. Enter your solution into variable """

(12choose3 * 9choose2) / 21choose5 = correct answer, yay!

""" Problem 2
Suppose a particular crime is committed in Jerry’s apartment. We’d like to know whether Newman is guilty of the crime. We are torn as to whether we think he is guilty: we think it’s equally likely that he is guilty or not guilty. Suppose that, in similar situations, we know that if a suspect is guilty,  85%
  of the time their finger prints are found at the scene, and, we know that if a suspect is not guilty,  30%
  of the time their finger prints are found at the scene.
  """

  Let G be the event someone is guilty of a crime, and F be the event their finger prints are found at the scene of the crime.

  P(F|G) = 0.85
  P(F|G^C) = 0.30

  Let N be the event Newman's finger prints are found at the scene of the crime.

  a) What is the probability that Newman’s finger prints are found at the scene?

  Note the statement in the problem: "we think it’s equally likely that he is guilty or not guilty", we deduce:

  P(G) = P(G^C) = 0.5

  We wish to solve for P(F).

  P(F) = P(F|G)P(G) + P(F|G^C)P(G^C)
  P(F) = 0.85 * 0.5 + 0.3 * 0.5
  P(F) = 0.575

  b) If Newman’s finger prints are found at the scene, how likely is it that he is guilty?

  P(G|F) = ?

  Well now we assume his finger prints are found at the scene so we need to use Bayes Theorem to go from prior to posterior:
  
  P(A|B) = P(B|A)P(A)/P(B)
  
  P(G|F) = P(F|G)P(G)/P(F)
  P(G|F) = (0.85 * 0.5) / 0.575
  P(G|F) = 0.739

  c) If Newman’s finger prints are not found at the scene, how likely is it that he is guilty?

  P(G|F^C) = P(F^C|G)P(G)/P(F^C)

  P(F^C) = 1 - P(F)
  P(F^C) = 0.425

  What about P(F^C|G). P(F^C|G) = P(F^C n G) / P(G).
  We can get this value if we draw a tree representing the outcomes. But let's just imagine it.

  P(F|G) = 0.85
  1 - P(F|G) = P(F^C|G)
  P(F^C|G) = 0.15

  And similarly:
  P(F|G^C) = 0.3
  P(F^C|G^C) = 0.7

  So back to solving P(G|F^C):
  P(G|F^C) = P(F^C|G)P(G)/P(F^C)
  P(G|F^C) = (0.15*0.5)/0.425
  P(G|F^C) = 0.176


  """ Problem 3
The game of Yahtzee is played with five fair dice. The goal is to roll certain ‘hands’, such as Yahtzee (all five dice showing the same number) or a full house (three of a kind and two of a kind). In the first round of a player’s turn, the player rolls all five dice. Based on the outcome of that roll, the player has a second and third round, where he/she can then choose to re-roll any subset of the dice to get a desired hand.
  """

  a) What is the probability of rolling a Yahtzee (all 5 dice showing the same number) on the first round? Round your answer to 4 decimal places.

  How many ways to have a success? Well you can have 6 successes.
  How many total ways to roll the dice? 6^5.
  Ans = 6/6^5 = 6^-4

  b) Suppose that, on the second round, the dice are {2, 3, 4, 6, 6}. You decide to re-roll both sixes in the third round. What is the probability that you roll either a small straight (exactly four dice are in a row) or a large straight (exactly five dice are in a row)?

  Split problem into 2 parts, first is how many ways to roll a straight
  given the current dice we already have. P(AuB) = P(A)+P(B)-P(AnB)

  3 possible ways to get a small straight:

  (1,2,3,4) or (2,3,4,5) or (3,4,5,6)

  so we have (2,3,4) already

  (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6) = 6 successes for small straight, plus 5 more for the other way round = 11 total ways for this small

  (5, 2), (5, 3), (5, 4), (5, 5), (5, 6) = 5 + 4 = 9 ways for this small straight.

  successes/total = 20/36 = 0.556

  NOW FOR PART 2 - total ways to roll a large straight
  (1,2,3,4,5) and (2,3,4,5,6)

  Note these rolls are already included in the counting above.
  We need (5,1), (1,5) and (6,5), (5,6).
  P(all 5) = 4/36 = 1/9

  P(small straight OR large straight) = P(s) + P(l) - P(s n l)
  P(small straight OR large straight) = 20/36 + 4/36 - 4/36 = 20/36
  20/36 =  0.556, yay well done!