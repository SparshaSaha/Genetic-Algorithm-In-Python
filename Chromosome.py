from Config import Config

class Chromosome(object):
    
    def __init__(self, config):
        self.config = config
        self.genes = [0 for i in range(0, self.config.NO_OF_GENES)]
    
    def main(self):
        print(self.genes)