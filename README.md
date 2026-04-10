# Phase-Field Modeling

This repository contains code for numerically solving simple phase-field problems. The simulations were created to accompany an educational video on phase-field modeling.

Video link: [https://youtu.be/areJqeWc49E](https://youtu.be/areJqeWc49E)

<p align="center">
  ⚠️ The simulations are intended for educational purposes only. Parts of the code were generated with the assistance of large language models. No convergence studies or rigorous validation have been performed. ⚠️
</p>

## Allen-Cahn equation

![Allen-Cahn](/media/videos/readme/gif_Allen_Cahn.gif)

The Allen-Cahn equation is given by

$$
\frac{\partial p}{\partial t} = -M \frac{\delta E}{\delta p} ,
$$

with the energy

$$
E = \frac{1}{\varepsilon^2} \int \int F(p) dx_1 dx_2 + \int \int \frac{1}{2} \lVert \nabla p \rVert^2 dx_1 dx_2 .
$$

The Allen–Cahn equation is solved using the forward Euler method in combination with a finite difference scheme on a regular grid with periodic boundary conditions. To run a simulation, execute one of the `main_Allen_Cahn.py` scripts, which solve the equation for different initial conditions. The simulation results are converted into animations and saved in the `media/videos` directory. To better understand the model, watch the [video on phase-field modeling](https://www.youtube.com/@DrSimulate). Then, copy and paste one of the `main_Allen_Cahn.py` scripts into a large language model to get a detailed explanation of the code.

## Cahn-Hilliard equation

![Cahn-Hilliard](/media/videos/readme/gif_Cahn_Hilliard.gif)

The Cahn-Hilliard equation

$$
\frac{\partial p}{\partial t}
= M \Delta \left(  \frac{\delta E}{\delta p} \right) ,
$$

is solved using a spectral FFT-based method on a regular grid with periodic boundary conditions. To run a simulation, execute one of the `main_Cahn_Hilliard.py` scripts, which solve the equation for different initial conditions. The simulation results are converted into animations and saved in the `media/videos` directory.

## Coupled problems

![Dendrite](/media/videos/readme/gif_dendrite.gif)

For examples of coupled problems, see the [phase-field fracture example](https://github.com/nathanshauer/phasefield-jr-py) as well as the [dendritic growth example](https://pages.nist.gov/fipy/en/latest/generated/examples.phase.anisotropy.html).