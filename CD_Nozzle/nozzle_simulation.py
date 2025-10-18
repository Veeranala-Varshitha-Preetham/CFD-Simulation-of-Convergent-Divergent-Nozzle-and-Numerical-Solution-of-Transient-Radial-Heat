# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

# Initialisation
r_inner = 2.005
r_outer = 2.01
k = 0.1  # W/mK
Cp = 1000.0  # J/kgK
rho = 1400.0  # kg/m^3
T0 = 300.0  # K

d_theta = 0.1  # rad
L = 1.0  # m
Nr = 100

# Providing flux at inner and outer wall
q_inner = +20000  # W/m^2
q_outer = +00000  # W/m^2

# Radius of cells
r = np.linspace(r_inner, r_outer, Nr)
dr = r[1] - r[0]

# Radius of the wall of the cell
r_edge = np.empty(Nr + 1)
r_edge[0] = r_inner
r_edge[-1] = r_outer
for j in range(1, Nr):
    r_edge[j] = 0.5 * (r[j - 1] + r[j])

# Area of the wall of the cell
A = r_edge * d_theta * L

# Volume of each cell
Vol = np.zeros(Nr)
for i in range(Nr):
    Vol[i] = d_theta * L * (r_edge[i + 1] ** 2 - r_edge[i] ** 2) / 2

a_S = np.zeros(Nr)
a_N = np.zeros(Nr)

for i in range(1, Nr):
    a_S[i] = k * A[i] / dr
for i in range(Nr - 1):
    a_N[i] = k * A[i + 1] / dr

a_P = a_S + a_N

# Initialisation of Time
time_total = 30  # s
dt = 0.1
Nt = 300

# Defining inner and outer cell Temperature array
time = np.zeros(Nt + 1)
T_inner = np.zeros(Nt + 1)
T_outer = np.zeros(Nt + 1)
time_step = 300
T_time_step = np.zeros(Nr)

T_new = np.zeros(Nr)

# Function for solving Tri-diagonal matrix
def TDMA(a, b, c, d):
    N = len(b)
    c_prime = np.zeros(N - 1)
    d_prime = np.zeros(N)
    T_new = np.zeros(N)
    c_prime[0] = c[0] / b[0]
    d_prime[0] = d[0] / b[0]

    for i in range(1, N - 1):
        c_prime[i] = c[i] / (b[i] - a[i] * c_prime[i - 1])
        d_prime[i] = (d[i] - a[i] * d_prime[i - 1]) / (b[i] - a[i] * c_prime[i - 1])

    d_prime[-1] = (d[-1] - a[-1] * d_prime[-2]) / (b[-1] - a[-1] * c_prime[-2])
    T_new[-1] = d_prime[-1]

    for i in range(N - 2, -1, -1):
        T_new[i] = d_prime[i] - c_prime[i] * T_new[i + 1]

    return T_new


T = np.full(Nr, T0, dtype=float)

# Solving for Temperature from the matrix equation, AX = B
for step in range(1, Nt + 1):
    T_old = T.copy()

    alpha_S = dt * a_S / (Vol * rho * Cp)
    alpha_N = dt * a_N / (Vol * rho * Cp)

    a = -alpha_S.copy()
    c = -alpha_N.copy()
    a[0] = 0.0
    c[-1] = 0.0
    b = 1.0 + alpha_S + alpha_N

    T_new = T_old.copy()
    T_new[0] = T_new[0] + ((dt * q_inner * A[0]) / (Vol[0] * rho * Cp))
    T_new[-1] = T_new[-1] + ((dt * q_outer * A[-1]) / (Vol[-1] * rho * Cp))

    T = TDMA(a, b, c, T_new)

    time[0] = 0.0
    T_inner[0] = T0
    T_outer[0] = T0
    time[step] = step * dt
    T_inner[step] = T[0]
    T_outer[step] = T[-1]

    # Plotting
    if step == 300:
        # Temperature variation with respect to radius at the final time step
        plt.figure(figsize=(8, 6))
        plt.plot(r, T, label=f'step{step} t = {step * dt:.3f}s')
        plt.title('T(r)')
        plt.xlabel('Radius r')
        plt.ylabel('Temperature T')
        plt.grid(True)
        plt.legend()
        plt.show()

# Temperature variation in first cell (inner cell) with respect to time
plt.figure(figsize=(8, 6))
plt.plot(time, T_inner)
plt.title('T_inner T (t)')
plt.xlabel('Time t (s)')
plt.ylabel('Temperature T (K)')
plt.grid(True)
plt.show()

# Temperature variation in outer cell with respect to time
plt.figure(figsize=(8, 6))
plt.plot(time, T_outer)
plt.title('T_outer T (t)')
plt.xlabel('Time t (s)')
plt.ylabel('Temperature T (K)')
plt.grid(True)
plt.show()
