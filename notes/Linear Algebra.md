# Linear Algebra

## Least Squares Solution

For $A [m\times n]$ and $b \in \mathbb{R}^m$, when we want $Ax = b$ but $x$ DNE,
$$A^{T}A\hat{x} = A^{T}b$$

## Eigendecomposition & Matrix Power

For $A [n\times n]$:
$$A = QDQ^{-1}$$

$$A^m = QD^mQ^{-1}$$

where 

$$Q = \begin{bmatrix} | & | & | \\ v_{1} & \ldots & v_n \\ | & | & | \end{bmatrix}$$ 

and 

$$D =\begin{bmatrix}\lambda_1&0&\ldots&0 \\ 0&\lambda_2&&0\\ \vdots&\vdots&\ddots&\vdots\\ 0&0&\ldots&\lambda_n\end{bmatrix}$$