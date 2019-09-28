def mean(a): return sum(a)/len(a)

def std(a):
    m = mean(a)
    return (sum((x - m)**2 for x in a)/len(a))**0.5

def correlation_coefficient(x, y):
    xm, ym = mean(x), mean(y)
    return sum((x[i]-xm)*(y[i]-ym) for i in range(len(x)))/std(x)/std(y)/len(x)

print(correlation_coefficient([  5427,   5688,   6198,   6462,   6635,   7336,   7248,   7491,   8161,   8578,   9000], [18.079, 18.594, 19.753, 20.734, 20.831, 23.029, 23.597, 23.584, 22.525, 27.731, 29.449]))