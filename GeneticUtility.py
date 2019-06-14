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

config = Config()
g = GeneticUtility(config)
c1 = Chromosome(config)
c2 = Chromosome(config)

c1, c2 = g.crossover(c1, c2)
print(c1.genes, c2.genes)
