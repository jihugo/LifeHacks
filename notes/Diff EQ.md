#   Differential Equations

##  Integrating Factor
<br>

For:
$$  \frac{dy}{dt} + g(t)y = b(t)  $$

Solution:
$$  y(t) = \frac{1}{\mu(t)} \int \mu(t) \cdot b(t)dt + C  $$

where $$\mu(t) = e^{\int g(t)dt}$$

---

##  Laplace Transform

$$ \mathcal{L}(y') = s\mathcal{L}(y) - y(0)  $$
$$ \mathcal{L}(y'') = s^{2} \mathcal{L}(y) - sy(0) - y'(0)
