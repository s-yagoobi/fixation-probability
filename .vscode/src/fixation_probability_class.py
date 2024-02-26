import numpy as np

class FixationProbabilityCalculator:
    def __init__(self, migration_probability, fitness, number_of_states, number_of_patches, local_size):
        self.migration_probability = migration_probability
        self.fitness = fitness
        self.number_of_states = number_of_states
        self.number_of_patches = number_of_patches
        self.local_size = local_size

    def convert_to_base(self, decimal_number, base):
        """
        Convert a decimal number to a number with arbitrary base.

        Parameters
        ----------
        decimal_number : int
            The decimal number to be converted.

        base : int
            The base to which the decimal number will be converted.

        Returns
        -------
        list
            A list representing the converted number in the specified base.
        """
        remainder_stack = []
        while decimal_number > 0:
            remainder = decimal_number % base
            remainder_stack.append(remainder)
            decimal_number = decimal_number // base
        # Pad the remainder stack with zeros to match the number of patches
        remainder_stack += [0] * self.number_of_patches
        # Trim the remainder stack to the desired length
        remainder_stack = remainder_stack[:self.number_of_patches]
        return remainder_stack

    def transition_matrix(self, adjacency_matrix):
        """
        Compute the transition matrix of an evolutionary network-structured metapopulation
        when local population size is identical in all the patches.

        Parameters
        ----------
        adjacency_matrix : numpy.ndarray
            The adjacency matrix representing connectivity between patches.

        Returns
        -------
        numpy.ndarray
            The transition matrix of the metapopulation.
        """
        T = np.zeros([self.number_of_states, self.number_of_states])
        for i in range(self.number_of_states):
            # Convert i to the base of local_size to get the configuration on the graph as a list
            i_config = self.convert_to_base(i, self.local_size + 1)
            # Calculate the total fitness
            total_fitness = self.fitness * sum(i_config) + self.number_of_patches * self.local_size - sum(i_config)

            for n in range(self.number_of_patches):
                # The probability that the number of mutants in patch n increases by one
                if i + (self.local_size + 1) ** n < self.number_of_states:
                    for k in range(self.number_of_patches):
                        T[i, i + (self.local_size + 1) ** n] += self.fitness * adjacency_matrix[k, n] * i_config[k]
                    T[i, i + (self.local_size + 1) ** n] *= (self.local_size - i_config[n]) / (self.local_size * total_fitness)

                # The probability that the number of mutants in patch n decreases by one
                if i - (self.local_size + 1) ** n >= 0:
                    for k in range(self.number_of_patches):
                         T[i, i - (self.local_size + 1) ** n] += adjacency_matrix[k, n] * (self.local_size - i_config[k])
                    T[i, i - (self.local_size + 1) ** n] *= i_config[n] / (self.local_size * total_fitness)

        # Calculate the diagonal elements of the transition matrix
        for i in range(self.number_of_states):
            T[i, i] = 1 - T[i].sum()

        return T

    def fixation_probability(self, adjacency_matrix):
        """
        Calculate the fixation probability of mutants in a metapopulation.

        Parameters
        ----------
        adjacency_matrix : numpy.ndarray
            The adjacency matrix representing connectivity between patches.

        Returns
        -------
        float
            The fixation probability of mutants.
        """
        # Compute the transition matrix
        TM = self.transition_matrix(adjacency_matrix)
        
        # Extract submatrices
        # Q is the transition matrix between transient states
        Q = TM[1:self.number_of_states-1, 1:self.number_of_states-1]

        # R is the probability of transition from any transient states to absorbing states
        a = TM[1:self.number_of_states-1, 0]
        b = TM[1:self.number_of_states-1, self.number_of_states-1]
        R = np.concatenate((a, b), axis=0)
        R = np.transpose(R.reshape((2, self.number_of_states-2)))
        
        # Identity matrix
        Identity = np.identity(self.number_of_states-2)

        inverse = np.linalg.inv(Identity - Q)
        
        # calculate $\phi= (Q-I)^{-1}R$ where $\phi$ is the absorption probability from any state to one of the absorbing points.
        Probability = np.dot(inverse, R)
        
        # Calculate fixation probability
        fix_prob = 0
        for n in range(self.number_of_patches):
            fix_prob += Probability[(self.local_size+1)**n - 1, 1]
        
        return fix_prob