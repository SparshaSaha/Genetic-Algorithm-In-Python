class Config(object):

    def __init__(self):
        self.NO_OF_GENES = 4
        self.MUTATION_PROBABILITY = 0.1
        self.POPULATION_SIZE = 16
        self.IDEAL_FITNESS = 4
        self.ELITE_CARRY_OVER = 2
        self.FITNESS_CATEGORY = "maximize"
        self.CROSSOVER_PROBABILITY = 0.9