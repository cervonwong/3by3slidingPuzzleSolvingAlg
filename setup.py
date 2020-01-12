from itertools import permutations
import numpy as np

def create(string):
    ans = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        ans[0][i] = int(string[i])
    for i in range(3,6):
        ans[1][i-3] = int(string[i])
    for i in range(6,9):
        ans[2][i-6] = int(string[i])
    return ans
def breaky(array):
    string = ''
    for i in range(3):
        for j in range(3):
            string += str(array[i][j])
    return string

da = [1,0,-1,0]
db = [0,-1,0,1]
perms = sorted(''.join(chars) for chars in permutations('012345678'))
adjList = dict()
visited = dict()

for i in perms:
    visited[i] = ''
    values = []
    built_array = create(i)
    for k in range(3):
        for l in range(3):
            if built_array[k][l] == 0:
                a,b = k,l
    for k in range(4):
        aa = a + da[k]
        bb = b + db[k]
        if 0 <= aa and aa < 3 and 0 <= bb and bb < 3:
            built_array[a][b], built_array[aa][bb] = built_array[aa][bb], built_array[a][b]
            values.append([built_array[a][b], breaky(built_array)])
            built_array[a][b], built_array[aa][bb] = built_array[aa][bb], built_array[a][b]
    adjList[i] = values
np.save("adjList.npy", adjList)
np.save("visited.npy", visited)
