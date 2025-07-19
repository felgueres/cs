# You are planning a science expedition, and you need to pick a base camp location.  
# The environment has open spaces (' ') and impassable mountains ('#').  
# There are several points of interest ('P') that need to be explored.  
# Each exploration takes an entire day (neglect travel time), and the 
# science team must return to camp each night after exploring a point of interest.  
# Fuel is expensive so you need to minimize total distance traveled.  
# What is the best location for the base camp?

grid = [
  ['#','#','#','#','#','#','#','#','#'],
  ['#','P','#','P',' ','#','#',' ','#'],
  ['#',' ',' ','#',' ','#','#',' ','#'],
  ['#',' ',' ','#',' ',' ','#',' ','#'],
  ['#',' ',' ',' ','#',' ','#',' ','#'],
  ['#',' ',' ',' ',' ',' ',' ',' ','#'],
  ['#','P',' ',' ',' ','#','#','#','#'],
  ['#','#','#','#','#','#','#','#','#']
]

# Scenario
# Shortest path from multiple sources 
# Undirected graph 
# Unweighted
# We can use BFS
# This would take (m*n)*(m*n)-> (V^2) but no need to run from all open spaces, you can run only from targets so p * (m*n - num_#) -> avg. (V)
# Fill up matrix with sum of distances for each source
# Pick min

from collections import deque

def find_best_location(grid):

    places_of_interest = []
    dist_grid = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'P':
                places_of_interest.append(((r,c),0,{(r,c)})) 
        row = [0] * len(grid[0]) 
        dist_grid.append(row)

    def get_neighbors(s):
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        r,c = s
        neighbors = []
        for dy,dx in directions:
            cur_r = r + dy
            cur_c = c + dx
            if 0 <= cur_r < len(grid) and 0 <= cur_c < len(grid[0]) and grid[cur_r][cur_c] == ' ':
                neighbors.append((cur_r,cur_c))
        return neighbors

    queue = deque(places_of_interest)

    while queue:
        s, dist,visited= queue.popleft()
        for v in get_neighbors(s):
            if v not in visited: 
                visited.add(v)
                queue.append((v, dist+1,visited)) 
                r,c = v
                dist_grid[r][c] += (dist+1)
    
    def get_min_dist_and_location(dist_grid):
        min_dist = 99999
        loc = None
        for r in range(len(dist_grid)):
            for c in range(len(dist_grid[0])):
                cum_dist = dist_grid[r][c]
                if cum_dist>0 and cum_dist < min_dist:
                    min_dist = cum_dist
                    loc = (r,c)
        return min_dist, loc
    
    min_dist, loc = get_min_dist_and_location(dist_grid)
    return dist_grid, min_dist, loc 

dist_grid, min_distance, location  = find_best_location(grid)

print('Distance matrix\n-------')
for r in range(len(dist_grid)): print(dist_grid[r])
print('-------')
print(f'Best location distance: {min_distance}\n-------')
print(f'Location: {location}\n-------')
