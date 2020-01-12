# 3by3slidingPuzzleSolvingAlg
An algorithm for solving **3 by 3 sliding puzzle** in python
## Algorithm
The program uses **breath first search** to find the **optimal** solution to the **3 by 3 sliding puzzle**
### How it works
First run *setup.py* to create two files *adjList.npy* and *visited.npy*
Then run *solver.py* and input the scrambled puzzle into the program in flattened form. flattened form is the three layers of numbers concatenated together from top to bottom. The value of the empty position is 0. i.e. The solved state in flattened form would be 1234567890
