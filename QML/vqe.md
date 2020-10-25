# Variational Quantum Eigensolvers

VQE allows us to find an upper bound of the lowest eigenvalue of a given Hamiltonian. It is a hybrid, quantum-classical algorithm. 

## Hamiltonian:

Hamiltonian — the Hamiltonian is a matrix which describes the possible energies of a physical system. If we know the Hamiltonian, we can calculate the behaviour of the system, learn what the physical states of the system are etc. It’s a central piece of quantum mechanics.

## Eigenvalue:

A given physical system can be in various states. Each state has a corresponding energy. These states are described by the eigenvectors and their energies are equal to the corresponding eigenvalues. In particular, the lowest eigenvalue corresponds to the ground state energy.

## Ground state:

This is the state of the system with the lowest energy, which means it’s the “most natural” state — i.e. a given system always tend to get there, and if it is in the ground state and is left alone, it will stay there forever.

## Conditions needed for VQE to work:

-[] Hamiltonian for system is known

## The Variational Principle:
```math
< Psi_{lamda} | H | Psi_{lamda} > >= E_{0}
```

## VQE Circuit:

It consists of three parts:

* Ansatz -  it prepares the state we need in order to apply variational principle.
* Hamiltonian - Hamiltonians constructed as a sum of Pauli operators (X, Y, Z) and their tensor products.
    *  We don’t actually put any of the corresponding X, Y, Z gates into the circuit. We use them to choose in which basis we want to do a measurement.
* Measurement

## Hybrid Model:
 So the idea is that we use a quantum computer (sometimes called QPU — quantum processing unit) for one thing only — to get the energy value for a given set of parameters. Everything else — so the whole optimization part — happens on a regular computer.

The parameters to optimize the Ansatz is classical and the rest of the procedure is quantum.

## Quantum Processing Unit (QPU):
Role of a QPU:

* Given a set of parameters, returns us a set of measurements.
* What a classical computer does:
* Given a set of measurements calculates the energy value (it’s usually some kind of averaging)
* Performs optimization procedure
* Calculates what a new set of parameters should be
* Checks whether we have reached the minimum
* Makes sure we don’t make more iterations than we should have done


## VQE Algorithm

![vqe](/Users/sshanto/Downloads/image7.jpg)

You can read “Quantum state preparation” as “ansatz” and “quantum module” as “adding rotations to enable measurements in the right basis”.
