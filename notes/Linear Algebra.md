# Linear Algebra

## Least Squares Solution

For $A [m\times n]$ and $b \in \mathbb{R}^m$, when we want $Ax = b$ but $x$ DNE,
$$A^{T}A\hat{x} = A^{T}b$$

## Diagonalization, Matrix Power, and Spectral Thorem

For $A [n\times n]$:
$$A = PDP^{-1}$$

$$A^m = PD^mP^{-1}$$

where 

$$P = \left\lbrack \matrix{| & & | \cr v_1 & \ldots & v_n \cr | & & |} \right\rbrack$$


and 

$$D = \left\lbrack \matrix{\lambda_1 & 0 & \ldots & 0 \cr 0 & \lambda_2 & & 0 \cr \vdots & \vdots & \ddots & \vdots \cr 0 & 0 & \ldots & \lambda_n} \right\rbrack$$

If $A$ is symmetric ($A^{T} = A$), then $A$ has orthonormal eigenvector columns in $P$. In which case, convention is $A = QDQ^{-1}$