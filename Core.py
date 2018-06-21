
# Added logging

import Population
import string
import logging

# TODO Create Documentation and clean up

LOG_FORMAT = "%(filename)s %(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="./DebugLog.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()


class Engine:
    def __init__(self, target, mutation_rate, pop_max):
        self.target = target
        self.mutationRate = mutation_rate
        self.pop_max = pop_max
        self.accepted = string.ascii_letters + " " + string.digits
        self.population = None
        self.most_fit_entity = 0
        self.currentFittest = 0
        self.fittest_this_evolution = 0
        self.fittest_yet = 0
        self.currentGen = 0
        self.gen_till_complete = None
        self.most_fit = None

    def gen_population(self):
        self.population = Population.Population(self.target, self.mutationRate, self.pop_max, self.accepted)

    def run_once(self):
        self.population.calc_fitness()
        self.population.natural_selection()
        self.population.generate()

        fittest_level_one_time = int(self.population.evaluate() * 100)

        self.most_fit_entity = self.population.fittest_element()

        logger.debug("Fittest from population {currentGen} is {mostFit} with a fitness of {fittest}%".format(
                    currentGen=self.currentGen,
                    mostFit=self.most_fit_entity,
                    fittest=fittest_level_one_time
                    ))

        print("Fittest from population " +
              str(self.currentGen) + ' is "' + str(self.most_fit_entity) +
              '" with a fitness of ' + str(fittest_level_one_time) + "%")

        if fittest_level_one_time > self.fittest_yet:
            self.fittest_yet = fittest_level_one_time

        self.currentGen += 1
        self.fittest_this_evolution = fittest_level_one_time

    def run_simulation(self):

        self.gen_population()

        index = 1
        highest = 0
        while highest < 100:
            # print(index)
            logger.debug("Starting main fitness_cal")
            # print("Starting main fitness_cal")
            self.population.calc_fitness()
            logger.debug("Finished main fitness_cal")
            # print("Finished main fitness_cal")

            logger.debug("Starting natural section")
            # print("Starting natural section")
            self.population.natural_selection()
            logger.debug("Finishing natural section")
            # print("Finishing natural section")

            logger.debug("Generating next Population")
            # print("Generating next Population")
            self.population.generate()
            logger.debug("Finished generating next Population")
            # print("Finished generating next Population")

            logger.debug("Evaluating population")
            # print("Evaluating population")
            loop = int(self.population.evaluate()*100)

            self.most_fit = self.population.fittest_element()

            logger.debug("Fittest from population {index} is {mostFit} with a fitness of {loop}%".format(
                        index=index,
                        mostFit=self.most_fit,
                        loop=loop
                        ))

            print("Fittest from population " +
                  str(index) + ' is "' + str(self.most_fit) +
                  '" with a fitness of ' + str(loop) + "%")

            if loop > highest:
                highest = loop
            # print("Evaluation "+ str(highest))
            # print(" ")
            index = index + 1

            self.gen_till_complete = index
