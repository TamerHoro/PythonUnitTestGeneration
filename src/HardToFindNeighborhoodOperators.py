import time
import subprocess

# Standard neightbor operator
for x in range(0,20):
    # Record the start time
    start_time = time.time()
    subprocess.run(['python', 'src/annealing_algorithm.py', '-c 1', '-a 1'])
    # Record the end time
    end_time = time.time()
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    f = open("AnneealingFitnnesslog.txt", "a")
    f.write(' | Time passed: '+str(elapsed_time)+ '\n')
    f.close()
    
# Close neighbor Operator    
for x in range(0,20):
    # Record the start time
    start_time = time.time()
    subprocess.run(['python', 'src/annealing_algorithm.py', '-c 1', '-a 1','-o 1'])
    # Record the end time
    end_time = time.time()
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    f = open("AnneealingFitnnesslog.txt", "a")
    f.write(' | Time passed: '+str(elapsed_time)+ '\n')
    f.close()