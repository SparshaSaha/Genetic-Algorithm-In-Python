from Chromosome import Chromosome
from Config import Config

import random

class RouletteWheel(object):
    
    def __init__(self, chromosomes, config):
        self.chromosomes = chromosomes
        self.config = config
    
    def RouletteWheelSelection(self):

        self.__createCumulativeProbabilities__()

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

config = Config()
c1 = Chromosome(config)
c2 = Chromosome(config)
c3 = Chromosome(config)

c1.fitness = 23
c2.fitness = 43
c3.fitness = 5

chromosomes = [c1, c2, c3]
r = RouletteWheel(chromosomes, config)
print("Genes", c1.genes, c2.genes, c3.genes)

c11 = 0
c12 = 0
c13 = 0

for i in range(0, 10):
    cx, cz = r.RouletteWheelSelection()
    if cx.genes == c1.genes or cz.genes == c1.genes:
        c11+=1
    
    if cx.genes == c2.genes or cz.genes == c2.genes:
        c12+=1

    if cx.genes == c3.genes or cz.genes == c3.genes:
        c13+=1

print(c11,c12,c13)