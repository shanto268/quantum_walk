import math
import pylab


def probabilities(posn):
    """Returns a list of the probabilies for each place."""
    return [sum([abs(amp) ** 2 for amp in place]) for place in posn]


def normalise(posn):
    """Normalise function to normalise an input 1D line."""
    N = math.sqrt(sum(probabilities(posn)))
    return [[amp / N for amp in place] for place in posn]


def timestep(posn):
    """Defines action of a timestep, i.e. a Hadamard gate on each element."""
    return normalise([[x[0] + x[1], x[0] - x[1]] for x in posn])


def shift(coin):
    """Shift the up elements leftwards and the down elements rightwards."""
    newposn = [[0, 0] for i in range(len(coin))]
    for j in range(1, len(posn) - 1):
        newposn[j + 1][0] += coin[j][0]
        newposn[j - 1][1] += coin[j][1]
    return normalise(newposn)


# Initialise lists.
min, max = -500, 501
posn = [[0, 0] for i in range(min, max)]
posn[-min] = [1 / math.sqrt(2), 1j / math.sqrt(2)]

# Run for some steps...
for time in range(-min):
    posn = shift(timestep(posn))

# Plot.
pylab.plot(range(min, max), probabilities(posn))
pylab.show()
