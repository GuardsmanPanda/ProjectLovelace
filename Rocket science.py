from math import exp

v_e = 2550  # rocket exhaust velocity [m/s]
M = 250000  # rocket dry mass [kg]

def rocket_fuel(v):
    return M*(exp(v/v_e)-1)

print(rocket_fuel(500.0))