import simpleBMI
import os
from xml.dom import minidom
import random
import string
from file_utilities import *
from generation_utilities import *

###### Import metadata

metadata = parseMetadata('BMICalc_metadata.json')

# For each constructor, note number of parameters.
# All parameters are assumed to be integers

# Actions
# Format is [name of action, type of action (assign, method), number of parameters
# All parameters are assumed to be integers
actions = [['gender', 'assign', 1], ['height', 'assign', 1], ['weight', 'assign', 1], ['age', 'assign', 1], ['calculateBMI', 'method', 2], ['classifyBMI_teensAndChildren', 'method', 0], ['classifyBMI_adults', 'method', 0]]

''' Example test case:
[
[0, [1]],
[1, [5]],
[4, [6,7]],
[6, []]
]
Each step is [ index in action list , [ parameter values] ]
'''


##### Prints genotype to a file (pytest code) and measures code coverage
#TODO: GET COVERAGE VALUE FROM SCRIPT INSTEAD OF A XML FILE ---- Some times this process bugs when in a loop.
#temporary workaround: Delay between creating and reading the XML file
import time
def getCoverage(test_suite):
    writeToFile(metadata, test_suite)
    os.system('pytest --cov=' + metadata["file"] + ' --cov-report term-missing --cov-report xml')
    #time.sleep(0.05*len(test_suite))
    try:
        xmldoc = minidom.parse('coverage.xml')
        tag = xmldoc.getElementsByTagName('coverage')
    except:
        time.sleep(0.05*len(test_suite))
        try:
            xmldoc = minidom.parse('coverage.xml')
            tag = xmldoc.getElementsByTagName('coverage')
        except:
            time.sleep(0.2)
            xmldoc = minidom.parse('coverage.xml')
            tag = xmldoc.getElementsByTagName('coverage')
    return (tag[0].attributes['line-rate'].value)


#ADDED A SMALL PENALTY FOR NUMBER OF TEST CASES USED. 
def fitness(test_suite):
    #fitness = coverage percentage - a small penalty for the number of tests
    a =  float(getCoverage(test_suite))
    b = float(len(test_suite))/10
    return a*100 - b

'''
Action library:
actions = [['gender', 'assign', 1], ['height', 'assign', 1], ['weight', 'assign', 1], ['age', 'assign', 1], ['calculateBMI', 'method', 2], ['classifyBMI_teensAndChildren', 'method', 0], ['classifyBMI_adults', 'method', 0]]

Example test case:
[
[0, [1]],
[1, [5]],
[4, [6,7]],
[6, []]
]
Each step is [ index in action list , [ parameter values] ]

Example test suite:
[[[-1, [642, 626, 53, -38]], [1, [612]], [4, [958, 46]]], [[-1, [257, 679, 337, 821]], [1, [74]], [0, [24]]], [[-1, [161, 409, 468, 675]], [1, [173]], [3, [926]]], [[-1, [870, -82, 949, 676]], [6, []], [4, [632, -88]]], [[-1, [235, 392, 366, 929]], [6, []], [6, []]], [[-1, [809, 508, 353, 706]], [6, []], [2, [72]]], [[-1, [276, 328, 691, -63]], [1, [538]], [3, [625]]], [[-1, [654, 69, 549, -1]], [3, [40]], [3, [741]]], [[-1, [147, 678, 485, 535]], [3, [321]], [6, []]], [[-1, [325, 291, 940, 169]], [6, []], [3, [484]]], [[-1, [745, 278, 232, 909]], [5, []], [0, [403]]], [[-1, [162, 993, 315, 186]], [4, [26, 980]], [1, [498]]], [[-1, [-95, 493, 68, 655]], [4, [881, 146]], [1, [295]]]]
'''

def deleteRandomAction(test_suite):
    nTestCases = len(test_suite) - 1
    testCaseSelected = random.randint(0,nTestCases)
    if len(test_suite[testCaseSelected]) > 1:
        nActions = len(test_suite[testCaseSelected]) - 1
        actionSelected = random.randint(1,(nActions))
        test_suite[testCaseSelected].remove(test_suite[testCaseSelected][actionSelected])
    return test_suite

def addRandomAction(test_suite):
    nTestCases = len(test_suite) - 1
    testSelected = random.randint(0,nTestCases)
    #print(testSelected)
    test_suite[testSelected].append(generateAction())
    return test_suite
    
def changeRandomParameter(test_suite, increment):
    nTestCases = len(test_suite) - 1
    testCaseSelected = random.randint(0,nTestCases)
    #print("test selected = %d" % testCaseSelected)
    nActions = len(test_suite[testCaseSelected]) - 1
    actionSelected = random.randint(0,(nActions))
    #print("actionSelected = %d" % actionSelected)
    #print(test_suite[testCaseSelected][actionSelected])

    if  test_suite[testCaseSelected][actionSelected][0] == -1:
        nParameters = len(test_suite[testCaseSelected][actionSelected][1]) - 1
        #print("nParameters = %d" % nParameters)
        parmeterSelected = random.randint(0,nParameters)
        #print("parmeterSelected = %d" % parmeterSelected)
        #print(test_suite[testCaseSelected][actionSelected][1][parmeterSelected])
        test_suite[testCaseSelected][actionSelected][1][parmeterSelected] = test_suite[testCaseSelected][actionSelected][1][parmeterSelected] + increment
    elif actions[test_suite[testCaseSelected][actionSelected][0]][2] > 0:
        nParameters = len(test_suite[testCaseSelected][actionSelected][1]) - 1
        parmeterSelected = random.randint(0,nParameters)
        #print(parmeterSelected)
        #print(test_suite[testCaseSelected][actionSelected][1][parmeterSelected])
        test_suite[testCaseSelected][actionSelected][1][parmeterSelected] = test_suite[testCaseSelected][actionSelected][1][parmeterSelected] + increment
    return test_suite

def addTestCase(test_suite):
    nActions = random.randint(0, 20)
    new_testCase = generateTestSuite(metadata,1,nActions)
    test_suite.extend(new_testCase)
    return test_suite

def removeTestCase(test_suite):
    nTestCases = len(test_suite) - 1
    if nTestCases > 1:
        testCaseSelected = random.randint(0,nTestCases)
        test_suite.remove(test_suite[testCaseSelected])
    return test_suite

def mutate(test_suite, action):
    '''
    Mutation - constrain possible actions - Pick one test case, make one change to actions in that test case:
        — Add an action
        — Delete an action
        — Change parameters of an action (limited range of values, increment or decrement integer a fixed amount)
        — Add a new test case with a constructor
        — Remove a test case
    '''
    
    try:
        assert action > 0 and action < 7
    except:
        raise RuntimeError('Function mutate receives two parameters. mutate(test_suite, action). Where action must be an integer from 1 to 6.')
        
    #SHOULD WE DELETE AND ADD TEST CASES INSTEAD OF ACTIONS? -------
    
    if action == 1: #1 delete an action
        test_suite = deleteRandomAction(test_suite)
    elif action == 2: #add an action
        test_suite = addRandomAction(test_suite)
    elif action == 3: #change random parameter - increment by 1
        test_suite = changeRandomParameter(test_suite, 1)    
    elif action == 4: #change random parameter - decrement by 1
        test_suite = changeRandomParameter(test_suite, -1)
    elif action == 5: #add a test case
        test_suite = addTestCase(test_suite)
    elif action == 6: #delete a test case
        test_suite = removeTestCase(test_suite)
    return test_suite


#Hill Climbing, using random ascent

maxTestsCases = 20
maxActions = 20

# Generate an initial solution.
# This is a random test suite (1-20 tests), each with 1-20 actions

solution_current = generateTestSuite(metadata,maxTestsCases, maxActions)
fitness_current = fitness(solution_current)
solution_best = solution_current
fitness_best = fitness_current
solution_soft = solution_current

print('Initial fitness: ' + str(fitness_current))

gen = 1
maxGen = 0
nSoftResets = 0

while (gen < maxGen):
    
    fitness_new = fitness_current
    tries = 30
    changed = False
    #SHOULD WE KEEP MUTATING THE MUTATED VERSION INSTEAD OF THE BEST? --------------------
    for i in range(tries):
        action = random.randint(1,6)
        solution_new = mutate(solution_current, action)
        fitness_new = fitness(solution_new)
        print(fitness_new)
        solution_current = solution_new
        
        if fitness_new > fitness_best:
            changed = True
            solution_best = solution_current
            fitness_best = fitness_new
    
    #Because we keep mutating the mutated version, solution_current might get to an irreversible state. I thought of a way to make a "soft" and a "hard" reset. 
    if not changed:
        if nSoftResets < 10:
            #get solution_current to what it was before mutating
            solution_current = solution_soft
            nSoftResets = nSoftResets + 1
        else:
            #if 3 soft resets doesn't work, time to generate a completely new solution_current
            maxTestsCases = 20
            maxActions = 20
            newTestSuite = generateTestSuite(metadata,maxTestsCases, maxActions)
            solution_current = newTestSuite
            solution_soft = solution_current
            nSoftResets = 0

    # Increment generation
    gen += 1

print("Best Test Suite: %d" %solution_best)
print("Best Fitness: %d" %fitness_best)
print("Number of generations used: %d" %gen)        
