def almost_pi(n):
    return sum((-1 if k % 2 == 1 else 1) * 1/(2*k+1) for k in range(n)) * 4
