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