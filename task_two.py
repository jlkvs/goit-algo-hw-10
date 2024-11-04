import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0  
b = 2  

N = 100000

x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N) 
under_curve = y_random < f(x_random)
area_estimate = (b - a) * f(b) * np.mean(under_curve)  
result, error = spi.quad(f, a, b)

print("Інтеграл: ", result, error)
