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
These variables can be modified at the start of the program as well as during runtime for added flexibility.

### Chromosome.py
```
def mutate():
# Helps to mutate a Gene
```

```
def __flipGene__():
# Helps to flip a Gene
```

### Roulette Wheel
This is a selection algorithm that I have implemented which helps in selection of individuals for reproduction

```
def __createCumulativeProabilities___():
# creates cumulative probabilities for the chromsomes passed as an argument
```

```
def __getNomalizedFitness__():
# Get nirmalized fitness values for each chromosome
```

```
def __calculateCumulativeSum__():
# Calculate cumulative sum for the batch of chromosomes
```

```
def RouletteWheelSelection():
# Returns two chromosomes from the current Pool based on their probability of selections
```

### GeneticUtility.py
 
 ```
 def __crossover__():
 # Returns two children from crossover between two parents
 ```
 
 ```
 def __originShiftIfNegativeFitnesses__():
 # If fitnesses are negative then origin shift them so that they are all positives
 ```
 
 ```
def simulateEvolution():
# Runs the simulation for 'n' generations(supplied as an argument).
# Fitness function passed to it as an argument
# Returns best individual
```
## How to Use the Library
Using the library is pretty simple and straight forward.

I have formulated some examples in the **/Examples** folder.

Additionally, lets have a look here:

**Step 1 :**
Import GeneticUtility and Config

```
from GeneticUtility import GeneticUtility
from Config import Config
```

**Step 2 :**
Define the Fitness Function

```
def fitnessFunction(chromosome):
```

**Step 3 :**
Define step Executor Function.

This fucntion will be called by the main module after every generation.

Can be used for logging ec.

```
def stepExecutor():
# Called with generation number and best Individual for that generation
```
**Step 4 :**
Create GeneticUtility Object

```
util = GeneticUtility(Config())
```

**Step 5 :**
Call simulateEvolution Method with number of generations, fitness function and stepExecutor

```
bestIndividual = util.simulateEvolution(300, fitnessFunction, stepExecution = stepExecutorMethod)
```

This method returns the bestIndividual Object
