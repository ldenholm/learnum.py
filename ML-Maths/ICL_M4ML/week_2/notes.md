# Vector Operations

## Modulus & Inner Product

- Irrespective of the coordinate system we want to define
the notion of length (modulus) and angle (dot product) of
a vector.

Start with unit vecors i,j for x,y axes. We define some vector in 2d
using ai + bj, where a,b in *field* of scalars under the vector space.
Pythagorus tells us the length of this vector v is equal to the square root of the sum of the squares.

|v| = sqrt(ai^2 + bj^2). Here we have just defined the eucliean norm.

And we can define the dot product, a . b yields |a||b|cos(theta)
Dot product = linear combination of the product of each operands components. Dot product is commutative and distributive over addition:
v . (u + w) = v . u + v . w.
The dot product is also associative over scalar multiplication:
r . (au) = a * (r . u) where a is from the field of scalars under the vector space.

We can dot a vector v with itself to produce its norm squared: v . v = |v|^2