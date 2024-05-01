import subprocess
from file_utilities import *


# Measures STATEMENT coverage of a test suite.
# Fitness is on scale 1-100. 
# The goal is to maximize the fitness
# Example Command line call statement coverage: 
# $ pytest --cov=bmi_calculator C:/Users/jonat/Desktop/Python/PythonUnitTestGeneration/src/example/test_bmi_calculator_annealing.py
def statement_fitness(metadata, solution):
    fitness = 0.0
    write_to_file(metadata, solution.test_suite)
    process = subprocess.Popen(["pytest", "--cov=" + metadata["file"],
                                metadata["location"] + "/test_" + metadata[
                                    "file"] + "_.py"], stdout=subprocess.PIPE)
    stdout = str(process.communicate()[0])
    lines = stdout.split("\\n")
    for line in lines:
        # Line we want starts with TOTAL
        if "TOTAL" in line:
            words = line.split(" ")
            coverage = words[len(words) - 1]
            fitness = coverage[0]+coverage[1]
            if fitness == "10":
                if coverage[2]== "0":
                    fitness += coverage[2]
    
    print("Coverage: "+fitness)
    return float(fitness)

# Measures BRANCH coverage of a test suite.
# Fitness is on scale 1-100. 
# The goal is to maximize the fitness
# Example command line call for BRANCH coverage
# $ pytest --cov=bmi_calculator C:/Users/jonat/Desktop/Python/PythonUnitTestGeneration/src/example/test_bmi_calculator_annealing.py --cov-branch
def branch_fitness(metadata, solution):
    fitness = 0.0
    write_to_file(metadata, solution.test_suite)
    process = subprocess.Popen(["pytest", "--cov=" + metadata["file"],
                                metadata["location"] + "/test_" + metadata[
                                    "file"] + "_.py","--cov-branch"], stdout=subprocess.PIPE)
    stdout = str(process.communicate()[0])
    lines = stdout.split("\\n")
    for line in lines:
        # Line we want starts with TOTAL
        if "TOTAL" in line:
            words = line.split(" ")
            coverage = words[len(words) - 1]
            fitness = coverage[0]+coverage[1]
            if fitness == "10":
                if coverage[2]== "0":
                    fitness += coverage[2]
    
    print("Coverage: "+fitness)
    return float(fitness)


def calculate_fitness(metadata, fitness_function, num_tests_penalty,
                      length_test_penalty, solution):
    fitness = 0.0

    if fitness_function == "statement":
        fitness += statement_fitness(metadata, solution)
    elif fitness_function == "branch":
        fitness += branch_fitness(metadata, solution)    
    else:
        raise Exception("Not a valid fitness function.")

    # Add a penalty to control test suite size
    fitness -= float(len(solution.test_suite) / num_tests_penalty)

    # Add a penalty to control the length of individual test cases
    # Get the average test suite length)
    avarage_length = sum([len(test) for test in solution.test_suite]) / len(
        solution.test_suite)
    fitness -= float(avarage_length / length_test_penalty)

    solution.fitness = fitness
