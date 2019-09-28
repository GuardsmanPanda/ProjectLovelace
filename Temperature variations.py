def temperature_statistics(t):
    mean = sum(t)/len(t)
    return mean, (sum((val-mean)**2 for val in t)/len(t))**0.5

print(temperature_statistics([4.4, 4.2, 7.0, 12.9, 18.5, 23.5, 26.4, 26.3, 22.5, 16.6, 11.2, 7.3]))