from Config import Config
import random

class Chromosome(object):
    
    def __init__(self, config):
        self.config = config
        self.genes = [0 for i in range(0, self.config.NO_OF_GENES)]
    
    def mutate(self):
        for i in range(0, len(self.genes)):
            if random.uniform(0, 1) <= self.config.MUTATION_PROBABILITY:
                self.genes[i] = self.flipGene(self.genes[i])
    
    def flip(self, geneValue):
        if geneValue == 0:
            return 1
        return 0
