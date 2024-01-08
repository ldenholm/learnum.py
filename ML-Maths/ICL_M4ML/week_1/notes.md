# Solving DS challenges with mathematics

---
Big ideas: ML is a set of powerful mathematical tools for analyzing the world around by harnessing power of machines. Open source libraries abstract the underlying mathematical operations from the user, in today's ML toolchain landscape we don't need to know what happens under the hood to use it but this comes at the cost of having no idea what to do when things go wrong.

This week we will dive in to vectors and some core lin alg concepts such as vector spaces, linear independence, rank, othorgonality, inner products, woo fun!

## Motivations for Linear Algebra

Types of problems we may want to solve using LA.
- Price discovery, using LA techniques to solve linear systems. Modelling problems with Ax=b and using Gaussian-Jordan elimination to solve.
- Fitting an equation to data and deciding which equation to use. How to find the optimal value for the parameters in the equation describing a Gaussian distribution. Then using this equation we have a portable representation of the population without requiring the original data (good for privacy concerns).

So two key problems we observe: solving systems of linear equations and optimisation problem of fitting data within an equation with some fitting parameters.

## Getting a handle on Vectors

In this video the teacher is presenting a normal distribution function of mu (mean) and sigma (std deviation) e.g. f(mu, sigma) and drawing a contour plot of the sum of the squares of differences between our estimation and the observed distribution. We then test subtle nudges up/down or left/right to optimize for the best fit by aiming for a contour nearest the origin. We store the ideal parameters sigma and mu in a vector which exist in the parameter space. Essentially buttering us up for learning about vectors and doing calculus on vectors (gradient will be the main one i'm guessing for gradient descent).

Simple exercise for solving simultaneous linear equations:

6x - 4y = 8

-7y = -7 => y = 1

6x + 3 = 15
6x = 12 => x = 2

---

Solve for x, y:
(-2x + 2y = 20) / 2
-x + y = 10
y = 10 + x

5x + 3(10 + x) = 6

5x + 30 + 3x = 6
8x = -24
x = -3

---

Solve for x, y, z:

3x −2y + z = 7

x + y + z = 2

3x - 2y -z = 3

subtract eq2 from eq1:

2x -3y = 5, => 2x = 5 + 3y

add eq2 to eq3:

4x - y = 5, now sub in our eq for x

4x = 2(2x = 5 + 3y)
4x = 4x = 10 + 6y

10 + 6y - y = 5
(10 + 5y = 5) / 5
2 + y = 1
y = -1

Now solve for x:
4x = 10 + 6(-1)
4x = 10 -6
4x = 4
x = 1

Now solve for z:
x + y + z = 2
1 -1 + z = 2
0 + z = 2
z = 2


Construct a matrix and use Ax = b to solve:
[3, -2, 1]   [x] = [7]
[1, 1, 1]    [y]   [2]
[3, -2, -1]  [z]   [3]

---

# Introduction to Vectors

Our lovely constituents of vector spaces. The teacher is emphasizing to consider vectors as collection of information rather than merely euclidean vectors. Vector addition is commutative as is scalar multiplication. He is also introducing unit vectors spanning R^2 and using them to construct random examples. Vector addition is associative. Take some u, v, w from V a vector space. (u + v) + w == u + (v + w). It's interesting to think about more abstract vector spaces for example take the space of second order polynomials and consider scaling them or performing other vector operations like projection. Anyway this video is pretty straight forward just basically you can scale vectors and add them.

## Summary of module 1

The problem of data and how we can analyze and use it. Mathematical techniques for extrapolating information from data.

Using linear algebra to analyze data e.g. price discovery, fitting a model with fitting parameters. Both these problems involve vectors and calculus.

Introduction to vectors, associativity of vector addition, commutativity
of vector addition and scalar multiplication.

Next week intro to vector spaces and their corresponding coordinate systems (basis).