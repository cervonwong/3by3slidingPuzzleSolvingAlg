import numpy as np
adjList = np.load("adjList.npy", allow_pickle = True)[()]
visited = np.load("visited.npy", allow_pickle = True)[()]
from queue import Queue
q = Queue()
impt = input("solveit")
q.put(impt)
while not q.empty():
    state = q.get()
    solveString = visited[state]
    if state == '123456780':
        print(solveString)
        break
    for i in adjList[state]:
        move = i[0]
        newState = i[1]
        if not visited[newState]:
            visited[newState] = solveString + str(move)
            q.put(newState)
if not visited[state]:
    print("impossible")
