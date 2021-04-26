
# Second Order Central Finite Difference Method
def SOC_FDM(future, present, past, delta):
    approximation = (future - 2*present + past)/(delta**2)
    return approximation


def wave_equation_approx():         # Use above function to produce the next time step
    pass
