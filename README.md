# Visualisation of predator-prey system dynamics
based on the Lotka–Volterra equations. Using python.

## GUI
Project uses PyQt and matplotlib. <br>
Users can modify ODE parameters and starting conditions via interactive sliders.

## Solved ODE
Visualised predator-pray system dynamics are based on slightly modified Lotka–Volterra equations [Lotka–Volterra equations](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations)

### Original equations
<img src="https://latex.codecogs.com/svg.image?%5Cfrac%7B%5Cpartial%20x%7D%7B%5Cpartial%20t%7D%20=%20(a%20-%20by)x">
<img src="https://latex.codecogs.com/svg.image?%5Cfrac%7B%5Cpartial%20y%7D%7B%5Cpartial%20t%7D%20=%20(cx%20-%20d)y%5C">

where: <br>
x - prey population <br>
y - predator population <br>
a - prey population growth <br>
b - prey mortality rate due to predation <br>
c - predator growth rate due to predation <br>
d - predator mortality rate <br>


### Modified equations
<img src="https://latex.codecogs.com/svg.image?%5Cfrac%7B%5Cpartial%20x%7D%7B%5Cpartial%20t%7D%20=%20(a%20-%20by)x">
<img src="https://latex.codecogs.com/svg.image?%5Cfrac%7B%5Cpartial%20y%7D%7B%5Cpartial%20t%7D%20=%20(bcx%20-%20d)y">

where: <br>
x - prey population <br>
y - predator population <br>
a - prey population growth <br>
b - prey mortality rate due to predation <br>
c - conversion rate of hunted prey to descendants <br>
d - predator mortality rate <br>

### Solwing method
ODE are solved  using the Runge Kutta 2nd order method.

## Result
![image](screenshots/prey-predator-screenshot.PNG)
![image](screenshots/prey-predator-screenshot_2.PNG)
