import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

def generate_sequence(r, x0, n):
    result = []
    x = x0
    for i in range(n):
        x = logistic_map(r, x)
        result.append(x)
    return result

# Parameter r dan kondisi awal x0
r = 3.8
x0 = 0.1

# Menghasilkan urutan bilangan acak
sequence = generate_sequence(r, x0, 1000)

# Membuat plot dari urutan bilangan acak
plt.plot(sequence)
plt.show()
