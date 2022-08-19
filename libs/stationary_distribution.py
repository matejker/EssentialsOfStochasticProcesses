import numpy as np
from copy import deepcopy


def get_stationary_distribution(p: np.ndarray, rates: bool = False) -> np.ndarray:
    n, m = p.shape
    if n != m:
        raise ValueError(f"P is not a square matrix {n}!={m}")

    # Two state markov chain
    if n == 2:
        return np.array([p[1][0], p[0][1]]) / (p[1][0] + p[0][1])
    
    # Continues Time Markov chains with rates
    if rates:
        a = deepcopy(p)
    else:
        a = deepcopy(p - np.eye(n))
    
    a[:, n - 1] = np.ones(n)

    # It will raise LinAlgError if it is Singular matrix or other problems
    return np.linalg.inv(a)[-1]


def is_symmetric(a: np.ndarray) -> bool:
    return np.round(a, 4) == np.round(a.T, 4)


def check_detailed_balance_condition(p: np.ndarray, rates: bool = False) -> bool:
    pi = get_stationary_distribution(p, rates=rates)
    return is_symmetric(pi * p.T)

