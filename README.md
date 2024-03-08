## Calculating fixation probability in a graph-structured meta-population

This project aims to calculate the fixation probability in a graph-structured metapopulation.
The subpopulations are connected through a network. Each subpopulation is occupied by individuals. The number of individuals can vary from one to any arbitrary number. 
The migration between subpopulations is indicated by the adjacency matrix.

Initially, the whole population is occupied by wild-type (type 1). All of a sudden one of the wild-types goes through mutation randomly. We are interested to see with what probability this mutant takes over the whole network assuming that the mutation rate is small enough such that before the mutant reaches fixation or extinction, no other mutant arises. 

## Code

The code for calculating the fixation probability can be found in .vscode/src/fixation_probability_function.py.
The documentation on how we calculate fixation probability can be found in .vscode/src/algorithm.md.

## Manuscript

Also you can find the paper published based on this project [here](https://www.nature.com/articles/s41598-021-97187-6) or under .vscode/docs/manuscript.

