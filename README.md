# Numerical Simulation of C-D Nozzle using CFD and Transient Radial Heat Conduction Analysis

###  Internship Project — DRDO (Advanced Systems Laboratory, Hyderabad)

**Author:** V. Varshitha Preetham  
**Institute:** Indian Institute of Technology Bhubaneswar  
**Supervisor:** DRDO-ASL, Hyderabad  
**Date:** May - July 2025  

---

##  Project Overview

This repository contains the Python implementations and simulation results developed as part of an internship at **Defence Research and Development Organisation (DRDO)**.  
The project focuses on **two major computational problems** in rocket propulsion and thermal analysis:

1. **Numerical Simulation of a Convergent–Divergent (C-D) Nozzle**  
   - Performed using both **CFD++** and an in-house **Python-based solver**.  
   - Objective: Compare high-fidelity CFD simulations with analytical and numerical predictions from the **Area–Mach number relation**.  
   - The Python code uses the **bisection method** to solve for Mach number along the nozzle length.

2. **Numerical Solution of Transient Radial Heat Conduction**  
   - Implemented using **Finite Volume Method (FVM)** and validated against **ANSYS APDL** results.  
   - The Python solver employs an **implicit scheme** with the **Tri-Diagonal Matrix Algorithm (TDMA)** for stable transient heat conduction calculations in a cylindrical (annular) geometry.

---

##  Topic I — Convergent–Divergent Nozzle Simulation

### Methodology
- Geometry based on realistic rocket nozzle dimensions.
- Flow conditions:  
  - Inlet Pressure = 40 bar  
  - Inlet Temperature = 2800 K  
  - Isothermal wall temperature = 300 K  
- CFD++ simulation conducted under **axisymmetric, viscous, compressible, steady-state** flow.
- Python code developed to solve the **quasi-1D isentropic flow relation**:

  \[
  \frac{A}{A^*} = \frac{1}{M} \left[\frac{2}{\gamma + 1}\left(1+\frac{\gamma - 1}{2}M^2\right)\right]^{\frac{\gamma+1}{2(\gamma-1)}}
  \]

- Solved iteratively using the **bisection method** for subsonic and supersonic regions.

### Results
- **CFD++ exit Mach number:** 3.7296  
- **Python solver exit Mach number:** 3.5676  
- **Deviation:** 4.5%  
- Demonstrates close agreement between empirical and CFD-based methods.

---

##  Topic II — Transient Radial Heat Conduction

### Problem Setup
- Inner Radius = 2.005 m, Outer Radius = 2.010 m  
- Material Properties:  
  - ρ = 1400 kg/m³  
  - Cp = 1000 J/kg·K  
  - k = 0.1 W/m·K  
- Boundary Conditions:  
  - Inner wall flux = 20,000 W/m²  
  - Outer wall flux = 0 W/m²  
  - Initial temperature = 300 K

### Numerical Method
- Discretized using **Finite Volume Method (FVM)** in cylindrical coordinates.  
- **Implicit scheme** ensures unconditional stability.  
- Solved using **Tri-Diagonal Matrix Algorithm (TDMA)**.

### Results
- **Python Solver:**  
  - Inner wall temperature ≈ 630 K  
  - Outer wall temperature ≈ 304 K  
- **Ansys APDL simulation:**  
  - Results matched closely with the Python code output.  
- Validates the accuracy and robustness of the numerical model.

---

##  Key Learning Outcomes
- Application of **compressible flow theory** and **heat transfer principles** to real-world systems.  
- Implementation of **numerical methods** such as:
  - Bisection Method  
  - Finite Volume Method  
  - Tri-Diagonal Matrix Algorithm (TDMA)  
- Cross-validation of **Python-based computational models** with **CFD++** and **ANSYS APDL** simulations.  
- Development of modular, physics-based solvers for engineering design and analysis.

---

##  Repository Structure

├── README.md
├── CD_Nozzle/
│ ├── nozzle_simulation.py
│ ├── nozzle_geometry_data.csv
│ └── results/
│ ├── mach_number_plot.png
│
├── Radial_Heat_Conduction/
│ ├── radial_heat_conduction.py
│ ├── temperature_profiles.png
│ ├── validation_ansys_overlay.png
│
└── Report.pdf ← Full internship report
