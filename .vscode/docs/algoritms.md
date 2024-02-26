**The transition matrix**

Each state is represented by a list $[i_1, i_2, i_3, ...]$ where $i_n$ is the number of mutants on the patch $n$. $i_n$ can vary between 0 and local_size (here shown as $M$). The number of mutants at the whole graph can only increase or decrease by one at each transition and the transition stops until all the network is either occupied by mutants (fixation state) or by wild-types (extinction step). An increase in the number of mutants occures when a mutant is chosen to give birth and replaces a wild-type either on the same patch or on an adjacent patch. 
As an example the number of mutants in patch 1, i.e. $i_1$ transitions to $i_1 + 1$ with the following probability:

$ T[(i_1, i_2,...), (i_1+1, i_2,...)] = \sum_n A[n, 1]\dfrac{ri_n}{ F_t} \dfrac{M - i_1}{M} $

where $A$ is the adjacent matrix of the network, $r$ is the relative fitness of the mutant, $M$ is the local population size, and $F_t$ is the total fitness of the population.

#### calculating the fixation probability
In order to calculate the mean fixation probability strating from one mutant on the network, we make use of the following formula:

$\phi= (Q-I)^{-1}R$. 

In this relation $\phi$ is the absorption probability from any state to one of the absorbing points (either extinction or fixation).
$Q$ is the transition matrix between transient states. $I$ is the identity matrix and $R$ represent the probability of transition from any transient states to absorbing states. 

In order to compute the fixation probability from this formula we sum over the entries of the matrix which determine the probability going from one mutant to the fixation state.