###################################################################
# Simple simulated annealing algorithm for generating pytest-formatted Python unit tests
#
#   Vorgehen: 
#       -Generate Random State
#       -Calculate Costs
#       -Select starting Temperature
#       -Calculate Iterations per T
#       -Chose a cooling rate
#
#
# 
# Command-Line parameters:
# -m <metadata file location>
# -g <search budget, the maximum number of generations before printing the best
#     solution found>
# -t <maximum number of mutations tried before restarting the search>
# -r <maximum number of restarts>
# -c <maximum number of test cases in a randomly-generated test suite>
# -a <maxmium number of actions (variable assignments, method calls) in a
#     randomly-generated test case>
# -z <test suite size penalty>
# -l <test length penalty>
###################################################################

import copy
import getopt
import sys
import statistics 
import numpy as np
import math 
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
[
[[-1, [642, 626, 53, -38]], [1, [612]], [4, [958, 46]]], 
[[-1, [257, 679, 337, 821]], [1, [74]], [0, [24]]], 
[[-1, [161, 409, 468, 675]], [1, [173]], [3, [926]]], 
[[-1, [870, -82, 949, 676]], [6, []], [4, [632, -88]]], 
[[-1, [235, 392, 366, 929]], [6, []], [6, []]], 
[[-1, [809, 508, 353, 706]], [6, []], [2, [72]]], 
[[-1, [276, 328, 691, -63]], [1, [538]], [3, [625]]], 
[[-1, [654, 69, 549, -1]], [3, [40]], [3, [741]]], 
[[-1, [147, 678, 485, 535]], [3, [321]], [6, []]], 
[[-1, [325, 291, 940, 169]], [6, []], [3, [484]]], 
[[-1, [745, 278, 232, 909]], [5, []], [0, [403]]], 
[[-1, [162, 993, 315, 186]], [4, [26, 980]], [1, [498]]], 
[[-1, [-95, 493, 68, 655]], [4, [881, 146]], [1, [295]]]
]
'''


# Delete a random action from an existing test
def delete_random_action(test_suite):
    suite_size = len(test_suite) - 1
    test_case_selected = random.randint(0, suite_size)

    if len(test_suite[test_case_selected]) > 1:
        num_actions = len(test_suite[test_case_selected]) - 1
        action_selected = random.randint(1, num_actions)
        test_suite[test_case_selected].remove(
            test_suite[test_case_selected][action_selected])

    return test_suite


def replace_random_action(test_suite):
    suite_size = len(test_suite) -1
    test_case_selected = random.randint(0, suite_size)

    if len(test_suite[test_case_selected]) > 1:
        num_actions = len(test_suite[test_case_selected]) - 1
        action_selected = random.randint(1, num_actions)
        test_suite[test_case_selected].remove(
            test_suite[test_case_selected][action_selected])
        test_suite[test_case_selected].append(generate_action(metadata))
    return test_suite

# Add a random action to an existing test
def add_random_action(test_suite):
    suite_size = len(test_suite) - 1
    test_selected = random.randint(0, suite_size)
    test_suite[test_selected].append(generate_action(metadata))
    return test_suite


# Change a parameter of an existing action
def change_random_parameter(test_suite):
    # Select a test, action, and parameter
    suite_size = len(test_suite) - 1
    test_case_selected = random.randint(0, suite_size)
    num_actions = len(test_suite[test_case_selected]) - 1
    action_selected = random.randint(0, num_actions)

    # Increment or decrement by a random amount  
    increment = random.randint(-10, 10)

    # If the action is a constructor call
    if test_suite[test_case_selected][action_selected][0] == -1:
        # Select the parameter to modify
        if len(metadata["constructor"])>0: 
            num_parameters = len(
                test_suite[test_case_selected][action_selected][1]) - 1        
            parameter_selected = random.randint(0, num_parameters)
            parameter_data = metadata["constructor"]["parameters"][parameter_selected]

            # Get the current value of that parameter
            value = test_suite[test_case_selected][action_selected][1][
                parameter_selected]

            if "min" in parameter_data.keys():
                if value + increment < parameter_data["min"]:
                    increment = parameter_data["min"] - value
            if "max" in parameter_data.keys():
                if value + increment > parameter_data["max"]:
                    increment = parameter_data["max"] - value

            test_suite[test_case_selected][action_selected][1][
                parameter_selected] += increment

    # If the parameter is an action (assignment or method call)
    elif "parameters" in metadata["actions"][
        test_suite[test_case_selected][action_selected][0]] and \
            len(metadata["actions"][
                    test_suite[test_case_selected][action_selected][0]][
                    "parameters"]) > 0:
        # Select the parameter to modify
        num_parameters = len(
            test_suite[test_case_selected][action_selected][1]) - 1
        parameter_selected = random.randint(0, num_parameters)
        parameter_data = \
            metadata["actions"][
                test_suite[test_case_selected][action_selected][0]][
                "parameters"][parameter_selected]

        # Get the current value of that parameter
        value = test_suite[test_case_selected][action_selected][1][
            parameter_selected]

        if "min" in parameter_data.keys():
            if value + increment < parameter_data["min"]:
                increment = parameter_data["min"] - value
        if "max" in parameter_data.keys():
            if value + increment > parameter_data["max"]:
                increment = parameter_data["max"] - value

        test_suite[test_case_selected][action_selected][1][
            parameter_selected] += increment

    return test_suite


# Add a test case to a suite
def add_test_case(test_suite):
    num_actions = random.randint(0, max_actions)
    new_test = generate_test_suite(metadata, 1, num_actions)
    test_suite.extend(new_test)
    return test_suite


# Delete a random test case from a suite
def remove_test_case(test_suite):
    suite_size = len(test_suite) - 1

    if suite_size > 1:
        test_case_selected = random.randint(0, suite_size)
        test_suite.remove(test_suite[test_case_selected])

    return test_suite


def mutate(solution):
    """
    When we mutate a solution, we make one small change to it. That change can
    include: — Add an action to a test case — Delete an action from a test case
    — Change parameters of an action (limited range of values, increment value
    by [-10, +10]) — Add a new test case to the suite — Remove a test case from
    the suite
    """

    new_solution = Solution()
    suite = copy.deepcopy(solution.test_suite)
    action = random.randint(1, 5)

    if action == 1:  # delete an action
        totallength = solution.total_length()
        if(totallength>1):
            new_solution.test_suite = delete_random_action(suite)
            #print("Deleted action")
    elif action == 2:  # add an action
        totallength = solution.total_length()
        if(totallength<max_actions):
            new_solution.test_suite = add_random_action(suite)
            #print("Added action")
    elif action == 3:  # change random parameter
        new_solution.test_suite = change_random_parameter(suite)
        #print("Changed random parameter")        
    elif action == 4:  # add a test case
        numberOfCases= solution.numberofCases()
        if(numberOfCases<max_test_cases):
            new_solution.test_suite = add_test_case(suite)
            #print("Added test case")  
    elif action == 5:  # delete a test case
        numberOfCases= solution.numberofCases()
        if(numberOfCases>1):        
            new_solution.test_suite = remove_test_case(suite)
            #print("Removed test case")  
    if new_solution.total_length() == 0:
        print("No changes could be made")  
        return solution

    return new_solution

def closeNeighborMutation(solution):
    """
    When we make a close neighbor mutatio, we make one small change to the test suite. That change can
    is either replacing an action with another or changing a random parameter.
    """

    new_solution = Solution()
    suite = copy.deepcopy(solution.test_suite)
    action = random.randint(1, 2)

    if action == 1:  # replace an action
        new_solution.test_suite = replace_random_action(suite)
        #print("Replaced action")
        
    elif action == 2:  # change random parameter
        new_solution.test_suite = change_random_parameter(suite)
        #print("Changed random parameter")        


    return new_solution

def bestPossibleFitness():  
   num_of_action = len(metadata['actions'])
   return float(100 - num_of_action/length_test_penalty)

def CalculateInitialTemperature(max_test_cases, max_actions, metadata):
    #listOfDifferentFitness = []
    #tmpSolution = Solution()
    #tmpSolution = solution   
    avarage_length = (max_actions*max_test_cases)/2
    avarage_fitness = 50 - float(avarage_length / length_test_penalty)
    num_of_action = 0
    #num_of_params = 0
    for action in metadata['actions']:
        num_of_action += 1
        #for param in action['parameters']:
        #    num_of_params += 1
    best_fitness = bestPossibleFitness()
    #listOfDifferentFitness.append(tmpSolution.fitness)
    #listOfDifferentFitness.append(100)
    #listOfDifferentFitness.append(0)
    return (statistics.pstdev([0,avarage_fitness,best_fitness]))

def CalculateInitialTemperature2(solution):
    listOfDifferentFitness = []
    #tmpSolution = Solution()
    tmpSolution = solution
    for i in range(1,10):
        #tmpSolution.test_suite = generate_test_suite(metadata, max_test_cases,
        #                                          max_actions)
        tmpSolution = mutate(solution)
        calculate_fitness(metadata, fitness_function, num_tests_penalty,            
                  length_test_penalty, tmpSolution)
        listOfDifferentFitness.append(tmpSolution.fitness)
    #listOfDifferentFitness.append(100)
    #listOfDifferentFitness.append(0)
    return (statistics.pstdev(listOfDifferentFitness))

def CalculateInitialTemperature3(solution):
    listOfDifferentFitness = []
    #tmpSolution = copy.deepcopy(solution)
    improvedTransition = 0
    notImproved = 0
    sumDeltaFitness = 0
    for i in range(1,10):
        tmpSolution = mutate(solution)
        calculate_fitness(metadata, fitness_function, num_tests_penalty,            
                  length_test_penalty, tmpSolution)
        listOfDifferentFitness.append(tmpSolution.fitness)
        
        if(solution.fitness >listOfDifferentFitness[-1]):
            improvedTransition += 1
            sumDeltaFitness += abs(tmpSolution.fitness - solution.fitness)
        else:
            notImproved += 1
    
    if(improvedTransition!= 0):        
        avarageFitnessDif = sumDeltaFitness/improvedTransition  
        initialTemp = avarageFitnessDif/(math.log(notImproved/(notImproved*0.8 - improvedTransition*(1-0.8))))
    else:
        initialTemp = 0
    return (initialTemp)

#region Parameter
###################################################################
# Annealing parameters
###################################################################

# Default parameters

# Location of the metadata on the CUT
metadata_location = "C:/Users/jonat/Desktop/Python/PythonUnitTestGeneration/src/example_hard_to_find/hard_to_find_metadata.json"

# Fitness function i.e "branch" or "statement"
fitness_function = "statement"

# Maximum number of test cases in a generated suite
max_test_cases = 20

# Maximum number of actions in a generated test case
max_actions = 20

# Maximum number of generations == length of the Markov-Chain
max_gen = 10

# Maximum number of restarts
max_restarts = 10

# Maximum number of mutations to try before restarting
max_tries = 10

# Cooling rate Alpha
cooling_rate = 0.95

# Test suite size penalty
num_tests_penalty = 10

# Test length penalty
length_test_penalty = 30

# Choice of Neighborhood operator
nbOperator = 0

# Get command-line arguments
try:
    opts, args = getopt.getopt(sys.argv[1:], "hm:c:a:g:r:t:z:l:o:")
except getopt.GetoptError:
    print(
        "hill_climber.py -m <metadata file location> -c <maximum number of test "
        "cases> -a <maximum number of actions> -g <maximum number of "
        "generations> -r <maximum number of restarts> -t <maximum number of "
        "mutations before restarting> -z <test suite size penalty> -l <test "
        "length penalty> -o <Neighborhood Operator>")
    sys.exit(2)

for opt, arg in opts:
    if opt == "-ann":
        print(
            "annealing_algorithm.py -m <metadata file location> -c <maximum number of "
            "test cases> -a <maximum number of actions> -g <maximum number of "
            "generations> -r <maximum number of restarts> -t <maximum number of "
            "mutations before restarting> -z <test suite size penalty> -l <test "
            "length penalty> -cool <Cooling rate> -o <Neighborhood Operator>")
        sys.exit()
    elif opt == "-m":
        metadata_location = arg
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
    elif opt == "-z":
        num_tests_penalty = int(arg)

        if num_tests_penalty < 1:
            raise Exception("num_tests_penalty cannot be < 1.")
    elif opt == "-l":
        length_test_penalty = int(arg)

        if length_test_penalty < 1:
            raise Exception("length_test_penalty cannot be < 1.")
    # elif opt == "-cool":
    #     cooling_rate = int(arg)
    #     if cooling_rate < 0.5:
    #         raise Exception("cooling_rate cannot be < 0.5")
    elif opt == "-o":        
        nbOperator = int(arg)
   
#endregion

# Import metadata
metadata = parse_metadata(metadata_location)

# Generate an initial random solution, and calculate its fitness
solution_current = Solution()
solution_current.test_suite = generate_test_suite(metadata, max_test_cases,
                                                  max_actions)
calculate_fitness(metadata, fitness_function, num_tests_penalty,            
                  length_test_penalty, solution_current)

# The initial solution is the best we have seen to date
solution_best = copy.deepcopy(solution_current)
print('Initial fitness: ' + str(solution_current.fitness))

# Continue to evolve until the generation budget is exhausted or the number of
# restarts is exhausted.
gen = 1
restarts = 0

proposedworseSolutions = 0
acceptedworseSolutions = 0
bestFitness = bestPossibleFitness()
acceptancerate = 0
acceptenceRateList = []

#sigma = CalculateInitialTemperature(max_test_cases, max_actions, metadata)
sigma = CalculateInitialTemperature3(solution_best)


while gen <= max_gen and restarts <= max_restarts:
    tries = 1
    changed = False
    solutionFound = False    

    if solution_best.fitness >= bestFitness :
            solutionFound = True
    
    # Try random mutations until we see a solutions that is accepted by probabilty rho or better
    while tries < max_tries and sigma > 0.01 and not changed and not solutionFound:
        
        if(nbOperator == 1):
            solution_new = closeNeighborMutation(solution_current)
            #print('close neighbor')
        else:
            solution_new = mutate(solution_current)
        
        calculate_fitness(metadata, fitness_function, num_tests_penalty,
                          length_test_penalty, solution_new)
       
       
        # If the solution is worse, maybe accept it.
        if solution_new.fitness < solution_current.fitness:
             #calculate acceptance criteria for Solutions
            fitnessDifference = solution_current.fitness - solution_new.fitness
            rho = math.exp(-fitnessDifference/sigma)
            proposedworseSolutions += 1
             #roll for accepting the worse Solution
            uniformDist = np.random.uniform(1,0,1)
            if(uniformDist  < rho):
                solution_current = copy.deepcopy(solution_new)
                changed = True
                print("worse solution accepted")
                acceptedworseSolutions += 1
            else:
                print("worse solution declined")
            
            acceptancerate = acceptedworseSolutions/proposedworseSolutions   
        # If the solution is an improvement, make it the new solution.
        elif solution_new.fitness > solution_current.fitness:
            solution_current = copy.deepcopy(solution_new)
            changed = True

            # If it is the best solution seen so far, then store it.
            if solution_new.fitness > solution_best.fitness:
                solution_best = copy.deepcopy(solution_current)


         
          
        print(
            "Best fitness at generation %d: %.8f, number of tests: %d, "
            "average test length: %d, mutation attempts: %d, acceptance rate: %.8f" % (
                gen, solution_best.fitness, len(solution_best.test_suite),
                solution_best.average_length(), tries, acceptancerate)
            )
        
        acceptenceRateList.append(acceptancerate)   
            
        sigma *= cooling_rate        
        tries += 1

    # Reset the search if no better mutant is found within a set number of
    # attempts.
    if not changed:
        restarts += 1
        solution_current = Solution()
        solution_current.test_suite = generate_test_suite(metadata,
                                                          max_test_cases,
                                                          max_actions)
        calculate_fitness(metadata, fitness_function, num_tests_penalty,
                          length_test_penalty, solution_current)
        print("Gen: " + str(gen) + ", RESET, new fitness: " + str(
            solution_current.fitness))
        #
        # sigma = CalculateInitialTemperature3(solution_best)

    # Increment generation
    gen += 1

#Log past results    
coverage = statement_fitness(metadata, solution_best)
totalSuiteLength = solution_best.total_length()
f = open("AnneealingFitnnesslog.txt", "a")
if not acceptenceRateList:
    f.write('Coverage: '+str(coverage)+' | Fitness: '+str(solution_best.fitness)+ ' | Avarage acceptance for each iteration: no worse solution was proposed')
else:
    f.write('Coverage: '+str(coverage)+' | Fitness: '+str(solution_best.fitness)+ ' | Avarage acceptance for each iteration: ' + str(sum(acceptenceRateList)/len(acceptenceRateList))) # + '\n'
    
f.close()

# Print information about the best test suite seen
print("Best Test Suite:")
print(solution_best.test_suite)
print("Best Fitness: " + str(solution_best.fitness))
print("Number of generations used: " + str(gen))
print("Number of tests: " + str(len(solution_best.test_suite)))
print("Total test length: " + str(solution_best.total_length()))
print("Acceptance for each iteration: " + str(acceptenceRateList))
# Print the best test suite to a file
write_to_file(metadata, solution_best.test_suite, "annealing")
