class Config(object):

    def __init__(self):
        self.NO_OF_GENES = 400
        self.MUTATION_PROBABILITY = 0.002
        self.POPULATION_SIZE = 600
        self.IDEAL_FITNESS = 0
        self.ELITE_CARRY_OVER = 20
        self.FITNESS_CATEGORY = "minimize"
        self.CROSSOVER_PROBABILITY = 0.95
        self.GENE_TYPE = "binary"