import numpy as np
def generate_grid(P,a = ['-','X','O'],s = (50,50)):
    '''
    This function will generate the grid for schelling process
    Input: P : Probability distribution array with the size as the same as the agent array. Each elements represent the probability of having the agent.
               Example: a = ['X','Y'], P = [0.4,0.6] will fill out the fill with agent X and Y with probability 0.4 and 0.6 accordingly.
           a : [Optional]agent array containing all of agents (including empty space if have one). Default is ['-', 'X','O']
           s : [Optional]size tuple (x,y) where x is number of row and y is number of column. Default is 50x50 for the assignment
    Output: The matrix with the size s containing the agents and the empty space in random position with probability P
    '''
    grid = np.random.choice(a, size=s, p=P)
    return grid
def export(path,grid):
    '''
    This function will export grid to path
    '''
    np.savetxt(path,grid,fmt='%s', encoding='Latin')
def find_empty(m,x):
    t = []
    p,q = np.where(m == x)
    for i in range(len(p)):
        t.append((p[i],q[i]))
    return t
def is_satisfy(subgrid,x,t):
    '''
    X,-,X
    O,[O],O
    -,X,-
    '''
    return np.count_nonzero(subgrid == x) >= t
def is_corner(point, grid):
    y,x = point
    return x == grid.shape[1]-1 or x == 0 or y == grid.shape[0]-1 or y == 0
def random_jump(empty_space,occupied,grid,ref,x,t,r,c):
    '''
    This function will choose the empty space to occupied and check that whether the target grid is satisfy or not.
    '''
    i = 0
    while(True):
        new_empty_y, new_empty_x = empty_space[np.random.choice(len(empty_space),1)[0]]
        #normal case
        if not is_corner((new_empty_y,new_empty_x),grid):
            empty_neighbor = ref[new_empty_y - 1:new_empty_y +2,new_empty_x-1:new_empty_x+2]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = '-'
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 1: upper non corner 
        elif new_empty_y == 0 and new_empty_x != grid.shape[1]-1 and new_empty_x != 0:
            empty_neighbor = ref[new_empty_y:new_empty_y +2,new_empty_x-1:new_empty_x+2]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = '-'
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 2: lower non corner
        elif new_empty_y == grid.shape[0]-1 and new_empty_x != grid.shape[1]-1 and new_empty_x != 0:
            empty_neighbor = ref[new_empty_y-1:new_empty_y+1,new_empty_x-1:new_empty_x+2]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = '-'
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 3: right non corner
        elif new_empty_x == grid.shape[1]-1 and new_empty_y != grid.shape[0]-1 and new_empty_y != 0:
            empty_neighbor = ref[new_empty_y-1:new_empty_y+2,new_empty_x-1:new_empty_x+1]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = '-'
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 4: left non corner
        elif new_empty_x == 0 and new_empty_y != grid.shape[0]-1 and new_empty_y != 0:
            empty_neighbor = ref[new_empty_y-1:new_empty_y+2,new_empty_x:new_empty_x+2]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = '-'
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 5: left top
        elif new_empty_x == 0 and new_empty_y == 0:
            empty_neighbor = ref[new_empty_y:new_empty_y+2,new_empty_x:new_empty_x+2]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = '-'
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 6: right top
        elif new_empty_x == grid.shape[1]-1 and new_empty_y == 0:
            empty_neighbor = ref[new_empty_y:new_empty_y+2,new_empty_x-1:new_empty_x+1]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = '-'
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 7: left buttom
        elif new_empty_y == grid.shape[0]-1 and new_empty_x == 0:
            empty_neighbor = ref[new_empty_y-1:new_empty_y+1,new_empty_x:new_empty_x+2]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = '-'
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 8: right buttom
        else:
            empty_neighbor = ref[new_empty_y-1:new_empty_y+1,new_empty_x-1:new_empty_x+1]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = '-'
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        i = i + 1
        if i > len(empty_space):
            break
    return occupied, grid
def schelling_process(grid, t):
    '''
    This function will simulate the schelling process from grid with one threshold and 2 agents. 
    Input: grid : a grid, matrix with the size s containing all agents (two) and empty space
           t    : torelate threshold, this number indicate the least number of the same type of agent to make itself satisfies. 
    Output: The grid that is updated by schelling process for 1 iteration
    '''
    occupied = []
    #define the reference matrix for the grid
    ref = grid
    empty_space = find_empty(ref,'-')
    #check the satifaction of each agents
    for (r, c), a in np.ndenumerate(grid): #for (row,column), agent
        x = grid[r][c] #get the value
        if x == '-':
            pass
        elif not is_corner((r,c),grid) : #check that it is not empty and not the corner one.
            #check around for their neighbors
            neighbor = ref[r - 1:r +2,c-1:c+2]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c)
        #case 1: top row non corner    
        elif r == 0 and c != 0 and c != grid.shape[1]-1:
            neighbor = ref[r:r +2,c-1:c+2]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c)
        #case 2: bottom row non corner    
        elif r == grid.shape[0]-1 and c != 0 and c != grid.shape[1]-1:
            neighbor = ref[r-1:r +1,c-1:c+2]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c)
        #case 3: left column non corner    
        elif c == 0 and r != 0 and r != grid.shape[0]-1:
            neighbor = ref[r-1:r +2,c:c+2]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c)
        #case 4: right column non corner    
        elif c == grid.shape[1]-1 and r != 0 and r != grid.shape[0]-1:
            neighbor = ref[r-1:r +2,c-1:c+1]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c)
        elif c == 0 and r == 0:
            neighbor = ref[r:r +2,c:c+2]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c)
        elif c == 0 and r == grid.shape[0]-1:
            neighbor = ref[r-1:r+1,c:c+2]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c)
        elif c == grid.shape[1]-1 and r == 0:
            neighbor = ref[r:r+2,c-1:c+1]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c)
        else:
            neighbor = ref[r-1:r+1,c-1:c+1]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c)
    return grid       
#1st problem
grid = generate_grid([0.4,0.3,0.3])
export('grid1_0.txt',grid)
for i in range(10):
    grid = schelling_process(grid, 3)
    export('grid1_{}'.format(i+1),grid)