from Chromosome import Chromosome
from Config import Config

import random

class RouletteWheel(object):
    
    def __init__(self, chromosomes, config):
        self.chromosomes = chromosomes
        self.config = config
        self.__createCumulativeProbabilities__()
    
    def RouletteWheelSelection(self):
        # Select first chromosome
        random1 = random.uniform(0, 1)
        chromosome1 = None
        for chromosome in self.chromosomes:
            if random1 <= chromosome.endRange:
                chromosome1 = Chromosome(self.config)
                chromosome1.genes = chromosome.genes
                break
        
        # Select second chromosome
        chromosome2 = None
        while True:
            random2 = random.uniform(0, 1)
            for chromosome in self.chromosomes:
                if random2 <= chromosome.endRange:
                    chromosome2 = Chromosome(self.config)
                    chromosome2.genes = chromosome.genes
                    
                    if chromosome1.genes != chromosome2.genes:
                        return chromosome1, chromosome2

    def __createCumulativeProbabilities__(self):
        self.__calculateCumulativeSum__()
        self.__getNomalizedFitness__()
        currentSum = 0
        for chromosome in self.chromosomes:
            currentSum += chromosome.normalizedFitness
            chromosome.endRange = currentSum
    
    def __calculateCumulativeSum__(self):
        cumSum = 0
        for chromosome in self.chromosomes:
            cumSum += chromosome.fitness
        self.cumSum = cumSum
    
    def __getNomalizedFitness__(self):
        for chromosome in self.chromosomes:
            chromosome.normalizedFitness = chromosome.fitness / self.cumSum
