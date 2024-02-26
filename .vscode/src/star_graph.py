import numpy as np
def star(number_of_patches):
    """
    Return the adjacency matrix of a star graph with a given number of patches.

    Parameters
    ----------
    number_of_patches : int
        The number of patches in the star graph.

    Returns
    -------
    numpy.ndarray
        The adjacency matrix of the star graph.
    """
    S = np.zeros([number_of_patches, number_of_patches])
    S[:, number_of_patches - 1] = 1
    S[number_of_patches - 1, :] = 1
    S[number_of_patches - 1, number_of_patches - 1] = 0
    return S
