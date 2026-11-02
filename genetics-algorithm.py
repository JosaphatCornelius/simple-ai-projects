import random
import copy
import time


class Individual:
    def __init__(self, chromosome=None, diff=0, fitness=0.0):
        self.chromosome = chromosome if chromosome is not None else []
        self.diff = diff
        self.fitness = fitness


def random_alphabet():
    return random.randint(1, 26)


def count_fitness(target, ind: Individual):
    diff_sum = 0
    for i in range(len(target)):
        diff_sum += abs(ind.chromosome[i] - target[i])
    ind.diff = diff_sum
    ind.fitness = 1 / (1 + diff_sum)


def select_one(population_arg):
    maximum = sum([c.fitness for c in population_arg])
    pick = random.uniform(0, maximum)
    current = 0
    for individual in population_arg:
        current += individual.fitness
        if current > pick:
            return copy.deepcopy(individual)
    return copy.deepcopy(population_arg[-1])


def crossover(individual1: Individual, individual2: Individual, crossover_prob=0.75):
    crossover_point = random.uniform(0, 1)
    if crossover_point < crossover_prob:
        intersection = random.randint(0, len(individual1.chromosome) - 1)
        for i in range(intersection, len(individual1.chromosome)):
            temp = individual1.chromosome[i]
            individual1.chromosome[i] = individual2.chromosome[i]
            individual2.chromosome[i] = temp


def mutation(individual: Individual, mutation_prob=0.01):
    mutation_point = random.uniform(0, 1)
    if mutation_point < mutation_prob:
        mutation_index = random.randint(0, len(individual.chromosome) - 1)
        individual.chromosome[mutation_index] = random_alphabet()


def main_algorithm(target_individual, population_amount=10, crossover_prob=0.75, mutation_prob=0.01):
    # initialize
    population = []
    match_found = False
    generation = 0

    for i in range(population_amount):
        ind = Individual(random.sample(range(1, 26), len(target_individual)))
        population.append(ind)

    # count fitness
    for i in range(len(population)):
        count_fitness(target_individual, population[i])

    while not match_found:
        generation += 1

        for i in range(len(population)):
            if population[i].diff == 0:
                match_found = True
                print(
                    f"\nSuccess! Perfect match found in Generation {generation}.")
                print(f"Chromosome: {population[i].chromosome}")
                break

        if match_found:
            break

        # selection in population amount
        new_population = []
        for i in range(len(population)):
            new_population.append(select_one(population))

        print("\nThe Chosen Ones (Pre-Crossover/Mutation)")
        for i in range(len(new_population)):
            print(i, new_population[i].chromosome,
                  new_population[i].diff, new_population[i].fitness)

        for i in range(0, len(new_population) - 1, 2):
            crossover(new_population[i], new_population[i + 1], crossover_prob)
            mutation(new_population[i], mutation_prob)
            mutation(new_population[i + 1], mutation_prob)

        # Recalculate fitness after mutations/crossover so accurate data is printed
        for i in range(len(new_population)):
            count_fitness(target_individual, new_population[i])

        print("\nThe Chosen Ones (Post-Crossover/Mutation)")
        for i in range(len(new_population)):
            print(i, new_population[i].chromosome,
                  new_population[i].diff, new_population[i].fitness)

        population = new_population
        best_fitness = max([ind.fitness for ind in population])
        print(
            f"Generation {generation} complete. Best fitness: {best_fitness:.4f}")


if __name__ == "__main__":
    target_individual = [2, 1, 19, 21, 11, 9]

    main_algorithm(target_individual, 100, 0.9, 0.1)
    print("Test 1 done.")
    time.sleep(5)

    main_algorithm(target_individual, 50, 0.5, 0.3)
    print("Test 2 done.")
    time.sleep(5)

    main_algorithm(target_individual, 25, 0.7, 0.01)
    print("Test 3 done.")
