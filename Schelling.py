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
    grid = np.char.upper(grid) #change to uppercase for multi-t problem
    np.savetxt(path,grid,fmt='%s', encoding='utf-8')
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
    return np.count_nonzero(np.char.upper(subgrid) == np.array2string(np.char.upper(x)).replace("'",'')) > t
def is_corner(point, grid):
    y,x = point
    return x == grid.shape[1]-1 or x == 0 or y == grid.shape[0]-1 or y == 0
def random_jump(empty_space,occupied,grid,ref,x,t,r,c,empty_string):
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
                grid[r][c] = empty_string
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 1: upper non corner 
        elif new_empty_y == 0 and new_empty_x != grid.shape[1]-1 and new_empty_x != 0:
            empty_neighbor = ref[new_empty_y:new_empty_y +2,new_empty_x-1:new_empty_x+2]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = empty_string
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 2: lower non corner
        elif new_empty_y == grid.shape[0]-1 and new_empty_x != grid.shape[1]-1 and new_empty_x != 0:
            empty_neighbor = ref[new_empty_y-1:new_empty_y+1,new_empty_x-1:new_empty_x+2]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = empty_string
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 3: right non corner
        elif new_empty_x == grid.shape[1]-1 and new_empty_y != grid.shape[0]-1 and new_empty_y != 0:
            empty_neighbor = ref[new_empty_y-1:new_empty_y+2,new_empty_x-1:new_empty_x+1]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = empty_string
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 4: left non corner
        elif new_empty_x == 0 and new_empty_y != grid.shape[0]-1 and new_empty_y != 0:
            empty_neighbor = ref[new_empty_y-1:new_empty_y+2,new_empty_x:new_empty_x+2]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = empty_string
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 5: left top
        elif new_empty_x == 0 and new_empty_y == 0:
            empty_neighbor = ref[new_empty_y:new_empty_y+2,new_empty_x:new_empty_x+2]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = empty_string
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 6: right top
        elif new_empty_x == grid.shape[1]-1 and new_empty_y == 0:
            empty_neighbor = ref[new_empty_y:new_empty_y+2,new_empty_x-1:new_empty_x+1]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = empty_string
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 7: left buttom
        elif new_empty_y == grid.shape[0]-1 and new_empty_x == 0:
            empty_neighbor = ref[new_empty_y-1:new_empty_y+1,new_empty_x:new_empty_x+2]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = empty_string
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        #corner case 8: right buttom
        else:
            empty_neighbor = ref[new_empty_y-1:new_empty_y+1,new_empty_x-1:new_empty_x+1]
            if is_satisfy(empty_neighbor,x,t) and (new_empty_y,new_empty_x) not in occupied:
                grid[new_empty_y][new_empty_x] = x
                grid[r][c] = empty_string
                occupied.append((new_empty_y,new_empty_x))
                break
            else:
                pass
        i = i + 1
        if i > len(empty_space):
            break
    return occupied, grid
def schelling_process(grid, agents, T,empty_string):
    '''
    This function will simulate the schelling process from grid with one threshold and 2 agents.

    Input: 
            grid     :  a grid, matrix with the size s containing all agents (two) and empty space
            agents   :  agent array, for multiple T problem, the different ratio of T can be produce by using lowercase i.e.
                        agents = ['-','X','O','x','o']
                                     t = t_X  t=t_x but X and x are the same agent group      
            T        :  tolerate threshold array, this array indicate the least number of the same type of agent to make itself satisfies.
                        i.e. (with the agents as example) T = [0,3,3,5,5]
                        in this case, agent X will have t = 3, agent x will have t = 5 (their distribution can be adjusted by function generate_grid)     
    Output: The grid that is updated by schelling process for 1 iteration
    '''
    occupied = []
    #define the reference matrix for the grid
    ref = np.copy(grid)
    empty_space = find_empty(ref,empty_string)
    #check the satifaction of each agents
    for (r, c), a in np.ndenumerate(grid): #for (row,column), agent
        x = grid[r][c] #get the value
        t = T[agents.index(x)] #find the corresponding t
        if x == empty_string:
            pass
        elif not is_corner((r,c),grid) : #check that it is not empty and not the corner one.
            #check around for their neighbors
            neighbor = ref[r - 1:r +2,c-1:c+2]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c,empty_string)
        #case 1: top row non corner    
        elif r == 0 and c != 0 and c != grid.shape[1]-1:
            neighbor = ref[r:r +2,c-1:c+2]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c,empty_string)
        #case 2: bottom row non corner    
        elif r == grid.shape[0]-1 and c != 0 and c != grid.shape[1]-1:
            neighbor = ref[r-1:r +1,c-1:c+2]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c,empty_string)
        #case 3: left column non corner    
        elif c == 0 and r != 0 and r != grid.shape[0]-1:
            neighbor = ref[r-1:r +2,c:c+2]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c,empty_string)
        #case 4: right column non corner    
        elif c == grid.shape[1]-1 and r != 0 and r != grid.shape[0]-1:
            neighbor = ref[r-1:r +2,c-1:c+1]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c,empty_string)
        elif c == 0 and r == 0:
            neighbor = ref[r:r +2,c:c+2]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c,empty_string)
        elif c == 0 and r == grid.shape[0]-1:
            neighbor = ref[r-1:r+1,c:c+2]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c,empty_string)
        elif c == grid.shape[1]-1 and r == 0:
            neighbor = ref[r:r+2,c-1:c+1]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c,empty_string)
        else:
            neighbor = ref[r-1:r+1,c-1:c+1]
            #if satisfy
            if is_satisfy(neighbor,x,t):
                pass #do nothing
            #if not satisfy
            else:
                occupied, grid = random_jump(empty_space,occupied,grid,ref,x,t,r,c,empty_string)
    return grid

if __name__ == '__main__':
    a = []
    P = []
    string = '''
    How to use?
    1. Initialize the agent array by given the number of agents (include empty space and same agent with different threshold)
    i.e. I want to simulate 2 agents X and O with probability of X have t = 3 0.8 and t = 5 0.2, the same goes for O
    I should define it with 5 agents [' ','X','O','x','o'] where x and o is the same with X and O respectively (the output
    will auto capitalize it)
    Please enter how many agent you want to have:
    '''
    n = int(input(string))
    for i in range(n):
        a.append(input('Please enter agent (single character, empty space must include): '))
    string2 = '''
    How to use?
    2. We will initialize the size of the grid in which we want it to generate
    Please enter the vertical length of the grid:
    '''
    y = int(input(string2))
    x = int(input('Please enter the horizontal length of the grid: '))
    string3 = '''
    How to use?
    3. We will initialize the probability of generation of each agents (and empty space). The order of it will
    corresponding to the agent order you just put. For example, if you put -,X,O the first probability would be
    the probability that - is on the grid (or the proportion on the grid per se) 
    '''
    print(string3)
    for i in range(n):
        P.append(float(input('Please enter the probability of agent {}: '.format(a[i]))))
    grid = generate_grid(P,a = a, s=(y,x))
    string4='''
    How to use?
    4. Right now the grid is generated.
    Please enter the export filename you want to generate (it will be in the form of <yourname>_[iteration].txt): 
    '''
    name = input(string4)
    string5='''
    How to use?
    5. We still not sure and want to make sure that what is your empty space agent?
    Please enter the empty space agent that you've enter: 
    '''
    empty_string = input(string5)
    string6='''
    How to use?
    6. So now we will start the simulation! The point is that we forget to ask you the threshold of each agents.
    We need that to determine how agent should perform. For example, we put threshold of agent X = 3, that is X requires
    another 3 agents with the same kind (X or x for multi-t) near itself. To illustrate that, please look at the diagram
    below

    - - X - - 
    - X - X -
    - X X X - 
    - O O O -
    O - O - O

    In this case, if we let X,O have threshold = 3, the unsatisfied agents would highlighted with star

    - - X - - 
    - X X X -
    - X X X - 
    - O O O -
    O* - O - O* 

    Note that the empty space will always have T = 0
    '''
    print(string6)
    T = []
    for i in range(n):
        T.append(int(input('Please enter the threshold of agent {}: '.format(a[i]))))
    string7='''
    How to use?
    7. Now the last part begin, we will simulate it but how many time we want to simulate it?
    '''
    iter_ = int(input(string7))
    for j in range(iter_):
        export(name+'_{}.txt'.format(j),grid)
        grid = schelling_process(grid,agents= a, T = T, empty_string=empty_string)
    if iter_ < 20:
        for j in range(iter_):
            print('Here is the result for iteration {}: '.format(j))
            read = open(name+'_{}.txt'.format(j))
            lines = read.readlines()
            for line in lines:
                print(line)
            read.close()
    else:
        pass
        