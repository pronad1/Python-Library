import math


# Function for dy/dx
def f(x, y):
    return 0.1 * y  # population growth model


# Milne's Method implementation
def milne_method(x0, y0, h, steps):
    # Store results
    xs = [x0]
    ys = [y0]

    # Use RK4 for first 3 values (Milne needs 4 starting points)
    def rk4(x, y, h):
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    # Generate first 3 points
    for i in range(3):
        y0 = rk4(x0, y0, h)
        x0 += h
        xs.append(x0)
        ys.append(y0)

    # Now apply Milne’s predictor–corrector
    for i in range(3, steps):
        # Predictor
        yp = ys[i - 3] + (4 * h / 3) * (2 * f(xs[i], ys[i]) - f(xs[i - 1], ys[i - 1]) + 2 * f(xs[i - 2], ys[i - 2]))

        xp = xs[i] + h
        # Corrector
        yc = ys[i - 1] + (h / 3) * (f(xs[i - 1], ys[i - 1]) + 4 * f(xs[i], ys[i]) + f(xp, yp))

        xs.append(xp)
        ys.append(yc)

    return xs, ys


# Parameters
x0 = 0
y0 = 100  # initial population
h = 1  # step size = 1 year
steps = 10  # compute 10 years

xs, ys = milne_method(x0, y0, h, steps)

# Display results
print("Year\tPopulation (Milne’s Method)\tExact Solution")
for i in range(len(xs)):
    exact = 100 * math.exp(0.1 * xs[i])
    print(f"{xs[i]:.0f}\t{ys[i]:.4f}\t\t\t{exact:.4f}")
