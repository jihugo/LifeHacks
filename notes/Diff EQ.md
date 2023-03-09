#   Differential Equations

##  Integrating Factor
<br>

For:
$$\frac{dy}{dt} + g(t)y = b(t)$$

Solution:
$$y(t) = \frac{1}{\mu(t)} \int \mu(t) \cdot b(t)dt + C$$

where $$\mu(t) = e^{\int g(t)dt}$$


##  Laplace Transform

$$\mathcal{L}(y') = s\mathcal{L}(y) - y(0)$$
$$\mathcal{L}(y'') = s^{2} \mathcal{L}(y) - sy(0) - y'(0)$$


##  General Solution

Finding general solution:

1. Find $y_h$, keep constants
2. Find $y_p$ (Guesses may be affected by $y_h$)
3. $y = y_p + y_h$ ($y_h$ still contains constants)
4. Check with initial conditions
   
For root $a \pm jb$:

- $y_1 = e^{at} \cos{(bt)}$
- $y_2 = e^{at} \sin{(bt)}$