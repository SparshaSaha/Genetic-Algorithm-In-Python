import random
import copy

from Chromosome import Chromosome
from Config import Config
from SelectionAlgorithms.RouletteWheel import RouletteWheel

class GeneticUtility(object):

    def __init__(self):
        self.config = Config()
        self.GENERATION_COUNT = 0
        self.selectedChromosomes = {}
    
    def __crossover__(self, chromosome1, chromosome2):
        
        # Randomly create a crossover point
        crossoverPoint = random.randint(1, len(chromosome1.genes) - 1)

        # Prepare child genes
        child1Genes = chromosome1.genes[0 : crossoverPoint] + chromosome2.genes[crossoverPoint : ]
        child2Genes = chromosome2.genes[0 : crossoverPoint] + chromosome1.genes[crossoverPoint : ]

        chromosomeToConsider1 = Chromosome(self.config)
        chromosomeToConsider2 = Chromosome(self.config)

        if random.uniform(0, 1) <= self.config.CROSSOVER_PROBABILITY:
            chromosomeToConsider1.genes = child1Genes
        else:
            chromosomeToConsider1.genes = chromosome1.genes.copy()
        
        if random.uniform(0, 1) <= self.config.CROSSOVER_PROBABILITY:
            chromosomeToConsider2.genes = child2Genes
        else:
            chromosomeToConsider2.genes = chromosome2.genes.copy()

        return chromosomeToConsider1, chromosomeToConsider2
    
    def __originShiftIfNegativeFitnesses__(self, chromosomes):
        # Find minimum fitness
        minimumFitness = min(chromosome.fitness for chromosome in chromosomes)

        if minimumFitness >= 0:
            return
        
        for chromosome in chromosomes:
            chromosome.fitness += minimumFitness * -1
    
    def simulateEvolution(self, noOfGeneration, fitnessFunction, stepExecution = None):
        chromosomes = [Chromosome(self.config) for i in range(0, self.config.POPULATION_SIZE)]
        bestIndividual = Chromosome(self.config)
        bestIndividual.fitness = -1
        
        for generation in range(0, noOfGeneration):
            print("Running for Generation " + str(self.GENERATION_COUNT))
            self.selectedChromosomes = {}
            # Calculate Fitnesses
            for chromosome in chromosomes:
                fitnessValue = fitnessFunction(chromosome)
                chromosome.originalFitness = fitnessValue

                if self.config.FITNESS_CATEGORY == 'minimize':

                    # Reverse fitness in case of reverse category
                    fitnessValue *= -1
                chromosome.fitness = fitnessValue
            
            # Origin shift chromosomes in case of negative fitness values
            self.__originShiftIfNegativeFitnesses__(chromosomes)

            rouletteWheel = RouletteWheel(chromosomes, self.config)
            nextGenChromosomes = []

            # Create next Generation
            for i in range(0, int(self.config.POPULATION_SIZE / 2)):
                # Select two chromosomes from roulette wheel
                chromosome1, chromosome2 = rouletteWheel.RouletteWheelSelection()

                # Cross Over the chromosomes
                chromosome1, chromosome2 = self.__crossover__(chromosome1, chromosome2)
                
                # Mutate the new chromosomes
                chromosome1.mutate()
                chromosome2.mutate()

                # Add them to the New Generation Pool if genes are unique
                if (str(chromosome1.genes) not in self.selectedChromosomes):
                    nextGenChromosomes.append(chromosome1)
                    self.selectedChromosomes[str(chromosome1.genes)] = 1

                if (str(chromosome2.genes) not in self.selectedChromosomes):
                    nextGenChromosomes.append(chromosome2)
                    self.selectedChromosomes[str(chromosome2.genes)] = 1
            
            # Add Elites to next Generation
            
            # Sort Chromosomes based on fitness values
            chromosomes.sort(key = lambda x : x.fitness, reverse = True)
            
            # Save best individual
            bestIndividual = copy.deepcopy(chromosomes[0])
            
            # Check if Ideal fitness has been reached
            # If so, then return
            if bestIndividual.originalFitness == self.config.IDEAL_FITNESS:
                return bestIndividual
            
            # Carry over Elites to next Generation if they donot already exist
            for i in range(0, self.config.ELITE_CARRY_OVER):
                if (str(chromosomes[i].genes) not in self.selectedChromosomes):
                    nextGenChromosomes[len(nextGenChromosomes) - i - 1] = copy.deepcopy(chromosomes[i])
            
            # Execute Stepper
            if stepExecution != None:
                stepExecution(generationNumber = self.GENERATION_COUNT, bestIndividual = chromosomes[0])

            self.GENERATION_COUNT += 1
            print("best " + str(chromosomes[0].originalFitness))
            chromosomes = nextGenChromosomes
        return bestIndividual
