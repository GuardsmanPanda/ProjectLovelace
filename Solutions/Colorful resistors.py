digits = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

multiplier = {
    'pink': 0.001,
    'silver': 0.01,
    'gold': 0.1,
    'black': 1,
    'brown': 10,
    'red': 100,
    'orange': 10 ** 3,
    'yellow': 10 ** 4,
    'green': 10 ** 5,
    'blue': 10 ** 6,
    'violet': 10 ** 7,
    'grey': 10 ** 8,
    'white': 10 ** 9
}

tolerance = {
    'none': 0.2,
    'silver': 0.1,
    'gold': 0.05,
    'brown': 0.01,
    'red': 0.02,
    'green': 0.005,
    'blue': 0.0025,
    'violet': 0.001,
    'grey': 0.0005,
    'black':0
}


def resistance(b):
    nom = 0 if len(b) < 4 else (digits[b[0]]*10 + digits[b[1]] if len(b) == 4 else digits[b[0]]*100 + digits[b[1]]*10 + digits[b[2]])*multiplier[b[-2]]
    return nom, nom*(1-tolerance[b[-1]]), nom*(1+tolerance[b[-1]])

print(resistance(["green"]))