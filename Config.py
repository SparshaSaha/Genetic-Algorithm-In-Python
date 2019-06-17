class Config(object):

    def __init__(self):
        self.NO_OF_GENES = 14
        self.MUTATION_PROBABILITY = 0.1
        self.POPULATION_SIZE = 200
        self.IDEAL_FITNESS = 0
        self.ELITE_CARRY_OVER = 2
        self.FITNESS_CATEGORY = "minimize"
        self.CROSSOVER_PROBABILITY = 0.6
        self.GENE_TYPE = "binary"