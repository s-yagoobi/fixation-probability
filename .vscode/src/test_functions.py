import unittest

import fixation_probability_function

import numpy as np

class Mytest(unittest.TestCase):
    def test_convert_to_base(self):
        self.assertEqual( fixation_probability_function.convert_to_base( decimal_number=5, base=3, number_of_patches=2), [2,1])

    def test_transition_matrix(self):
        self.assertEqual(fixation_probability_function.transition_matrix(adjacency_matrix=np.array([[0.5, 0.5],[0.5, 0.5]]), fitness=2, number_of_states=4, number_of_patches=2, local_size=1).all(), np.array([[1,0,0,0],[1/6,1/2,0,1/3],[1/6,0,1/2,1/3],[0,0,0,1]]).all())

    def test_fixation_probability(self):
        self.assertEqual( '{:.5f}'.format(fixation_probability_function.fixation_probability(adjacency_matrix=np.array([[0,0.5,0.5],[0.5,0,0.5],[0.5,0.5,0]]), fitness=1, number_of_states=8, number_of_patches=3, local_size=1)), '{:.5f}'.format(1/3))
        self.assertEqual( '{:.5f}'.format(fixation_probability_function.fixation_probability(adjacency_matrix=np.array([[0,0.5],[0.5,0]]), fitness=1, number_of_states=4, number_of_patches=2, local_size=1)), '{:.5f}'.format(1/2))
unittest.main()        