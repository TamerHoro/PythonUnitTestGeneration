###################################################################
# Simple hill-climber for generating pytest-formatted Python unit tests
# Based on the random ascent algorithm (with restarts)
#
# Command-Line parameters:
# -m <metadata file location>
# -f <fitness function (choices: statement)>
# -g <search budget, the maximum number of generations before printing the best solution found>
# -t <maximum number of mutations tried before restarting the search>
# -r <maximum number of restarts>
# -c <maximum number of test cases in a randomly-generated test suite>
# -a <maxmium number of actions (variable assignments, method calls) in a randomly-generated test case>
###################################################################

import copy
import getopt
import random
import sys
from file_utilities import *
from generation_utilities import *
from fitness_functions import *

###################################################################
# Mutation functions, used in the hill climber to manipulate solutions
###################################################################

'''
Example test case:
[
[0, [1]],
[1, [5]],
[4, [6,7]],
[6, []]
]
Each step is [ index in action list , [ parameter values] ]
Actions are stored in the metadata dictionary at metadata["actions"][index]. 
Example test suite:
[[[-1, [642, 626, 53, -38]], [1, [612]], [4, [958, 46]]], [[-1, [257, 679, 337, 821]], [1, [74]], [0, [24]]], [[-1, [161, 409, 468, 675]], [1, [173]], [3, [926]]], [[-1, [870, -82, 949, 676]], [6, []], [4, [632, -88]]], [[-1, [235, 392, 366, 929]], [6, []], [6, []]], [[-1, [809, 508, 353, 706]], [6, []], [2, [72]]], [[-1, [276, 328, 691, -63]], [1, [538]], [3, [625]]], [[-1, [654, 69, 549, -1]], [3, [40]], [3, [741]]], [[-1, [147, 678, 485, 535]], [3, [321]], [6, []]], [[-1, [325, 291, 940, 169]], [6, []], [3, [484]]], [[-1, [745, 278, 232, 909]], [5, []], [0, [403]]], [[-1, [162, 993, 315, 186]], [4, [26, 980]], [1, [498]]], [[-1, [-95, 493, 68, 655]], [4, [881, 146]], [1, [295]]]]
'''

# Delete a random action from an existing test
def deleteRandomAction(test_suite):
    suite_size = len(test_suite) - 1
    test_case_selected = random.randint(0, suite_size)

    if len(test_suite[test_case_selected]) > 1:
        num_actions = len(test_suite[test_case_selected]) - 1
        action_selected = random.randint(1, num_actions)
        test_suite[test_case_selected].remove(test_suite[test_case_selected][action_selected])

    return test_suite

# Add a random action to an existing test
def addRandomAction(test_suite):
    suite_size = len(test_suite) - 1
    test_selected = random.randint(0, suite_size)
    test_suite[test_selected].append(generateAction(metadata))
    return test_suite

# Change a parameter of an existing action
def changeRandomParameter(test_suite):

    # Select a test, action, and parameter
    suite_size = len(test_suite) - 1
    test_case_selected = random.randint(0, suite_size)
    num_actions = len(test_suite[test_case_selected]) - 1
    action_selected = random.randint(0,(num_actions))

    # Increment or decrement by a random amount  
    increment = random.randint(-10, 10)

    # If the action is a constructor call
    if test_suite[test_case_selected][action_selected][0] == -1:
        # Select the parameter to modify
        num_parameters = len(test_suite[test_case_selected][action_selected][1]) - 1
        parameter_selected = random.randint(0, num_parameters)
        parameter_data = metadata["constructor"]["parameters"][parameter_selected]

        # Get the current value of that parameter
        value = test_suite[test_case_selected][action_selected][1][parameter_selected]

        if "min" in parameter_data.keys():
            if value + increment < parameter_data["min"]:
                increment = parameter_data["min"] - value 
        if "max" in parameter_data.keys():
            if value + increment > parameter_data["max"]:
                increment = parameter_data["max"] - value 

        test_suite[test_case_selected][action_selected][1][parameter_selected] += increment

    # If the parameter is an action (assignment or method call)
    elif "parameters" in metadata["actions"][test_suite[test_case_selected][action_selected][0]] and len(metadata["actions"][test_suite[test_case_selected][action_selected][0]]["parameters"]) > 0:
        # Select the parameter to modify
        num_parameters = len(test_suite[test_case_selected][action_selected][1]) - 1
        parameter_selected = random.randint(0, num_parameters)
        parameter_data = metadata["actions"][test_suite[test_case_selected][action_selected][0]]["parameters"][parameter_selected]

        # Get the current value of that parameter
        value = test_suite[test_case_selected][action_selected][1][parameter_selected]

        if "min" in parameter_data.keys():
            if value + increment < parameter_data["min"]:
                increment = parameter_data["min"] - value 
        if "max" in parameter_data.keys():
            if value + increment > parameter_data["max"]:
                increment = parameter_data["max"] - value 

        test_suite[test_case_selected][action_selected][1][parameter_selected] += increment

    return test_suite

# Add a test case to a suite
def addTestCase(test_suite):
    num_actions = random.randint(0, max_actions)
    new_test = generateTestSuite(metadata, 1, num_actions)
    test_suite.extend(new_test)
    return test_suite

# Delete a random test case from a suite
def removeTestCase(test_suite):
    suite_size = len(test_suite) - 1

    if suite_size > 1:
        test_case_selected = random.randint(0, suite_size)
        test_suite.remove(test_suite[test_case_selected])

    return test_suite

def mutate(solution):
    '''
    When we mutate a solution, we make one small change to it. That change can include:
        — Add an action to a test case
        — Delete an action from a test case
        — Change parameters of an action (limited range of values, increment value by [-10, +10])
        — Add a new test case to the suite
        — Remove a test case from the suite
    '''

    new_solution = Solution()
    suite = copy.deepcopy(solution.test_suite)
    action = random.randint(1,5)
    
    if action == 1: # delete an action
        new_solution.test_suite = deleteRandomAction(suite)
    elif action == 2: # add an action
        new_solution.test_suite = addRandomAction(suite)
    elif action == 3: # change random parameter 
        new_solution.test_suite = changeRandomParameter(suite)    
    elif action == 4: # add a test case
        new_solution.test_suite = addTestCase(suite)
    elif action == 5: # delete a test case
        new_solution.test_suite = removeTestCase(suite)

    return new_solution

###################################################################
#Hill Climbing, using random ascent
###################################################################

# Default parameters

# Location of the metadata on the CUT
metadata_location = "example/BMICalc_metadata.json" 

# Fitness function
fitness_function = "statement" 

# Maximum number of test cases in a generated suite
max_test_cases = 20 

# Maximum number of actions in a generated test case
max_actions = 20 

# Maximum number of generations
max_gen = 200

# Maximum number of restarts
max_restarts = 5

# Maximum number of mutations to try before restarting
max_tries = 500

# Get command-line arguments
try:
    opts, args = getopt.getopt(sys.argv[1:],"hm:f:c:a:g:r:t:")
except getopt.GetoptError:
        print("hill_climber.py -m <metadata file location> -f <fitness function> -c <maximum number of test cases> -a <maximum number of actions> -g <maximum number of generations> -r <maximum number of restarts> -t <maximum number of mutations before restarting>")
        sys.exit(2)
													  		
for opt, arg in opts:
    if opt == "-h":
        print("hill_climber.py -m <metadata file location> -f <fitness function> -c <maximum number of test cases> -a <maximum number of actions> -g <maximum number of generations> -r <maximum number of restarts> -t <maximum number of mutations before restarting>")
        sys.exit()
    elif opt == "-m":
        metadata_location = arg
    elif opt == "-f":
        fitness_function = arg
    elif opt == "-c":
        max_test_cases = int(arg)

        if max_test_cases < 1:
            raise Exception("max_test_cases cannot be < 1.")
    elif opt == "-a":
        max_actions = int(arg)

        if max_actions < 1:
            raise Exception("max_actions cannot be < 1.")
    elif opt == "-g":
        max_gen = int(arg)

        if max_gen < 1:
            raise Exception("max_gen cannot be < 1.")
    elif opt == "-r":
        max_restarts = int(arg)

        if max_restarts < 0:
            raise Exception("max_restarts cannot be < 0.")
    elif opt == "-t":
        max_tries = int(arg)

        if max_tries < 1:
            raise Exception("max_tries cannot be < 1.")

# Import metadata
metadata = parseMetadata(metadata_location)

# Generate an initial solution.
solution_current = Solution()
solution_current.test_suite = generateTestSuite(metadata, max_test_cases, max_actions)
calculateFitness(metadata, fitness_function, solution_current)

solution_best = copy.deepcopy(solution_current)

print('Initial fitness: ' + str(solution_current.fitness))


# Continue to evolve until the generation budget is exhausted or the number of restarts is exhausted.

gen = 1
restarts = 0

while gen <= max_gen and restarts <= max_restarts: 
    tries = 1
    changed = False

    # Try random mutations until we see a better solutions, or until we exhaust the number of tries.
    while tries < max_tries and changed != True:
        solution_new = mutate(solution_current)
        calculateFitness(metadata, fitness_function, solution_new)

        # If the solution is an improvement, make it the new solution.
        if solution_new.fitness > solution_current.fitness:
            print("Gen: " + str(gen) + ", new fitness: " + str(solution_new.fitness))
            print("Tries before finding new solution: " + str(tries))
            solution_current = copy.deepcopy(solution_new)
            changed = True
       
            # If it is the best solution seen so far, then store it.
            if solution_new.fitness > solution_best.fitness:
                solution_best = copy.deepcopy(solution_current)

        tries += 1

    # Reset the search if no better mutant is found within a set number of attempts.
    if changed == False:
        restarts += 1
        solution_current = Solution()
        solution_current.test_suite = generateTestSuite(metadata, max_test_cases, max_actions)
        calculateFitness(metadata, fitness_function, solution_current)
        print("Gen: " + str(gen) + ", RESET, new fitness: " + str(solution_current.fitness))

    # Increment generation
    gen += 1

# Print information about the best test suite seen

print("Best Test Suite:")
print(solution_best.test_suite)
print("Best Fitness: " + str(solution_best.fitness))
print("Number of generations used: " + str(gen))

# Print the best test suite to a file

writeToFile(metadata, solution_best.test_suite)
