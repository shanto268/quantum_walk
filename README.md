# Quantum Walk: Discrete Time

##Concept

U^t unitary matrix resembled the dynamics of a qunatum walk. U is the evolution operator and t is the number of steps.

There is nothing random about Quantum Walks since the evolution of the system is deterministic for completely isolated systems. It is natural to use the term “quantum walk” for unitary evolution and the term “quantum random walk” for non-unitary evolution. Measurement process introduces the probability distributions.
In discrete time, the quantum walk has three steps.
1. Coin operator on the coin state.
2. Shift operator on the particle.
3. Measurement in the computaional basis
Position of particle at each step is a superposition of the possible positions. The state of the particle is the result of the first two step operators mentioned abover.

If we apply the coin operator followed by the shift operator over and over without intermediary measurements, the quantum correlations between different positions generate constructive or destructive interference, creating a behaviorcharacteristic of quantum walks that is different from the classical behavior. In this case, the probability distribution is not the normal distribution and the standard deviation is not sqrt(t).

##Probability Distribution of Quantum Walk 
![Screenshot](plot.png)

