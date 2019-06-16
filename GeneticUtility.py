import random

from Chromosome import Chromosome
from Config import Config

class GeneticUtility(object):

    def __init__(self, config):
        self.config = config
    
    def crossover(self, chromosome1, chromosome2):
        
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

        # print(chromosome1.genes)
        # print(chromosome2.genes)
        # print(crossoverPoint)
        return chromosomeToConsider1, chromosomeToConsider2
    
    def originShiftIfNegativeFitnesses(self, chromosomes):
        # Find minimum fitness
        minimumFitness = min(chromosome.fitness for chromosome in chromosomes)

        if minimumFitness >= 0:
            return
        
        for chromosome in chromosomes:
            chromosome.fitness += minimumFitness * -1
    

config = Config()
g = GeneticUtility(config)
c1 = Chromosome(config)
c2 = Chromosome(config)
c1.fitness = -10
c2.fitness = -20
g.originShiftIfNegativeFitnesses([c1, c2])
print(c1.fitness, c2.fitness)
