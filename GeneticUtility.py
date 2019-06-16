import random

from Chromosome import Chromosome
from Config import Config
from RouletteWheel import RouletteWheel

class GeneticUtility(object):

    def __init__(self, config):
        self.config = config
        self.GENERATION_COUNT = 0
    
    def __crossover__(self, chromosome1, chromosome2):
        
        # Randomly create a crossover point
        crossoverPoint = random.randint(1, len(chromosome1.genes) - 1)

        # Prepare child genes
        child1Genes = chromosome1.genes[0 : crossoverPoint] + chromosome2.genes[crossoverPoint : ]
        child2Genes = chromosome2.genes[0 : crossoverPoint] + chromosome1.genes[crossoverPoint : ]

        chromosomeToConsider1 = Chromosome(self.config)
        chromosomeToConsider2 = Chromosome(self.config)

        if random.uniform(0, 1) <= config.CROSSOVER_PROBABILITY:
            chromosomeToConsider1.genes = child1Genes
        else:
            chromosomeToConsider1 = chromosome1
        
        if random.uniform(0, 1) <= config.CROSSOVER_PROBABILITY:
            chromosomeToConsider2.genes = child2Genes
        else:
            chromosomeToConsider2 = chromosome2

        return chromosomeToConsider1, chromosomeToConsider2
    
    def __originShiftIfNegativeFitnesses__(self, chromosomes):
        # Find minimum fitness
        minimumFitness = min(chromosome.fitness for chromosome in chromosomes)

        if minimumFitness >= 0:
            return
        
        for chromosome in chromosomes:
            chromosome.fitness += minimumFitness * -1
    
    def simulateEvolution(self):
        chromosomes = [Chromosome(self.config) for i in range(0, self.config.POPULATION_SIZE)]
        
        # Calculate Fitnesses
        for chromosome in chromosomes:
            fitnessValue = self.fitness(chromosome)
            chromosome.fitness = fitnessValue
            print(chromosome.genes, chromosome.fitness)
        
        # Origin shift chromosomes in case of negative fitness values
        self.__originShiftIfNegativeFitnesses__(chromosomes)

        rouletteWheel = RouletteWheel(chromosomes)
        nextGenChromosomes = []

        for i in range(0, self.config.POPULATION_SIZE):
            # Select two chromosomes from roulette wheel
            chromosome1, chromosome2 = rouletteWheel.RouletteWheelSelection()

            # Cross Over the chromosomes
            chromosome1, chromosome2 = self.__crossover__(chromosome1, chromosome2)
            
            # Mutate the new chromosomes
            chromosome1.mutate()
            chromosome2.mutate()

            # Add them to the New Generation Pool
            






    def fitness(self, chromosome):
        testChrom = Chromosome(self.config)
        testChrom.gene = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        fitness = -1 * sum((chromosome.genes[i] - testChrom.genes[i]) ** 2 for i in range(0, len(chromosome.genes)))
        return fitness
    

config = Config()
g = GeneticUtility(config)
c1 = Chromosome(config)
c2 = Chromosome(config)
c1.fitness = -10
c2.fitness = -20
g.simulateEvolution()
