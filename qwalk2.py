from numpy import *
from matplotlib.pyplot import *

#spatial parameters: graph set up
N = 100      # number of random steps
P = 2*N+1    # number of positions

#coin state
coin0 = array([1, 0])  # |0>
coin1 = array([0, 1])  # |1>

#computing outer products for Hadamard coin operator
C00 = outer(coin0, coin0)  # |0><0|
C01 = outer(coin0, coin1)  # |0><1|
C10 = outer(coin1, coin0)  # |1><0|
C11 = outer(coin1, coin1)  # |1><1|

#Hadamard coin operator
C_hat = (C00 + C01 + C10 - C11)/sqrt(2.)

#Shift operators
ShiftPlus = roll(eye(P), 1, axis=0)
ShiftMinus = roll(eye(P), -1, axis=0)
S_hat = kron(ShiftPlus, C00) + kron(ShiftMinus, C11)

#The walk dynamic
U = S_hat.dot(kron(eye(P), C_hat))

#initial state
posn0 = zeros(P)
posn0[N] = 1     # array indexing starts from 0, so index N is the central posn
psi0 = kron(posn0,(coin0+coin1*1j)/sqrt(2.))

#state after N steps
psiN = linalg.matrix_power(U, N).dot(psi0)

#Measurement operator
prob = empty(P)
for k in range(P):
    posn = zeros(P)
    posn[k] = 1
    M_hat_k = kron( outer(posn,posn), eye(2))
    proj = M_hat_k.dot(psiN)
    prob[k] = proj.dot(proj.conjugate()).real #storing the probabilities


#Creating the plots
fig = figure()
ax = fig.add_subplot(111)
plot(arange(P), prob)
scatter(arange(P), prob, s=2.5, c='red')
xlim(0, P)
grid()
title("Quantum Walk: Discrete time")
ylabel("Probability")
xlabel("N")
show()


