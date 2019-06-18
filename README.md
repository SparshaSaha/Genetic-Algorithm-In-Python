# Genetic Algorithm Library in Python3

## What is Genetic Algorithm
Genetic algorithm is essentially an Artificial Intelligence algorithm designed to mimic the process of evolution at a particular level.
It is largely inspired by Darwin's theory of evolution and the concept of survival of the fittest.

Genetic algorithms can be used for optimization problems and they provide one off the fastest convergence rates provided that the parameters have been set right.

Here we create a random population of **N** individuals and then start to change them according to the need of the optimization problem.

There is an awesome [article](https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3) about Genetic Algorithm. Make sure to have a look at it.

## About the Project
I found out that there are a number of different Genetic Algorithm libraries available for pyhton inlucing **PYEVOLVE** etc. But I found it hard to get them installed on my system.
Besides they probably run inly for Python2.x. I wanted a relatively simple Genetic Algorithm Library for Python3.x with minimum dependencies.

Thus I decided to make one on my own. Besides I thought this would help me with an indepth understanding of the Algorithm if I can implement it.
And here we are.. :grin:

## Project Description

### Config.py
This file consists of the configuration variables that the user needs to set or modify. These configuration variables define the basis of the algorithm and can make all the difference.

```
self.NO_OF_GENES = 400
self.MUTATION_PROBABILITY = 0.002
self.POPULATION_SIZE = 600
self.IDEAL_FITNESS = 0
self.ELITE_CARRY_OVER = 20
self.FITNESS_CATEGORY = "minimize"
self.CROSSOVER_PROBABILITY = 0.95
self.GENE_TYPE = "binary"
```
