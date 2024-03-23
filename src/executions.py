import time
import subprocess

# Record the start time
start_time = time.time()

for x in range(0,20):
    # Record the start time
    start_time = time.time()
    subprocess.run(['python', 'src/annealing_algorithm.py'])
    # Record the end time
    end_time = time.time()
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    f = open("AnneealingFitnnesslog.txt", "a")
    f.write(' | ime passed: '+str(elapsed_time)+ '\n')
    f.close()
    
for x in range(0,20):
    # Record the start time
    start_time = time.time()
    subprocess.run(['python', 'src/hill_climber.py'])
    # Record the end time
    end_time = time.time()
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    f = open("HillClimberFitnnesslog.txt", "a")
    f.write(' | Time passed: '+str(elapsed_time)+ '\n')
    f.close()
    
for x in range(0,20):
    # Record the start time
    start_time = time.time()
    subprocess.run(['python', 'src/genetic_algorithm.py'])
    # Record the end time
    end_time = time.time()
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    f = open("GeneticFitnnesslog.txt", "a")
    f.write(' | Time passed: '+str(elapsed_time)+ '\n')
    f.close()

