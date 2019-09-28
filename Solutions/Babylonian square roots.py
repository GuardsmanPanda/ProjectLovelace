def babylonian_sqrt(S):
    guess = S
    while guess > 0 and (guess**2 - S)/S > 0.000000000001:
        guess = (guess+S/guess)/2
    return guess if guess >= 0 else "undefined"