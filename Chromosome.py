from Config import Config
import random

class Chromosome(object):
    
    def __init__(self, config):
        self.config = config
        self.genes = [random.randint(0, 1) for i in range(0, self.config.NO_OF_GENES)]
        self.fitness = 0
        self.normalizedFitness = 0.0
        self.endRange = 0.0
    
    def mutate(self):
        for i in range(0, len(self.genes)):
            if random.uniform(0, 1) <= self.config.MUTATION_PROBABILITY:
                self.genes[i] = self.__flipGene__(self.genes[i])
    
    def __flip__(self, geneValue):
        if geneValue == 0:
            return 1
        return 0
