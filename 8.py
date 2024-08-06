import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the differential equation
def dydt(t, y):
    return 2 * np.cos(2 * t) - 4 * y

# Initial condition
y0 = [2]

# Time span for the solution
t_span = (0, 15)

# Time points where the solution is computed
t_eval = np.linspace(t_span[0], t_span[1], 500)

# Solve the differential equation
solution = solve_ivp(dydt, t_span, y0, t_eval=t_eval)

# Plot the solution
plt.figure(figsize=(10, 6))
plt.plot(solution.t, solution.y[0], label='y(t)', color='b')
plt.title('Solution to the Differential Equation $\dfrac{dy}{dt} + 4y(t) = 2 \cos(2t)$')
plt.xlabel('Time (t) [seconds]')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()
plt.show()
