import numpy as np

def get_stationary_distribution(p: np.ndarray) -> np.ndarray:
    n, m = p.shape
    if n != m:
        raise ValueError(f"P is not a square matrix {n}!={m}")

    # Two state markov chain
    if n == 2:
        return np.array([p[1][0], p[0][1]]) / (p[1][0] + p[0][1])

    a = p - np.eye(n)
    a[:, n - 1] = np.ones(n)

    # It will raise LinAlgError if it is Singular matrix or other
    return np.linalg.inv(a)[-1]


def is_symmetric(a: np.ndarray) -> bool:
    return a == a.T


def check_detailed_balance_condition(p: np.ndarray) -> bool:
    pi = get_stationary_distribution(p)
    return is_symmetric(pi * p.T)
