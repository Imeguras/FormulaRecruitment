library(expm) 

mat <- scan('matrix.txt')
mat <- matrix(mat, ncol = 8, byrow = TRUE)
print(mat)


# number of paths possible to reach the node 8 from node 1
# is the sum of the powered matrixes of lenght n 
# (A^n)_ij gives us the number of paths of lenght n from i to j
#so summing all powers until n = 8 gives us the number of possible paths between two points, in this case i will be 1 j will be 8 giving us the result
# krat is equals to zeros matrix of size 8x8
krat <- matrix(0, ncol = 8, nrow = 8)
#loop 8 times
for (i in 1:8) {
  #sum the powers of the matrix
  krat <- krat + (mat %^% i )
}
print(krat)
# nao sei como formatar no R, acho que e primeira vez que sequer tou a escrever um script(nao consegui abrir o Rcomander)
print(paste("The actual solution for the number of paths is: ",krat[1,8]))

# A* copiado( https://www.algorithms-and-technologies.com/a_star/r)
a_star <- function(graph, heuristic, start, goal) {
  #' Finds the shortest distance between two nodes using the A-star (A*) algorithm
  #' @param graph an adjacency-matrix-representation of the graph where (x,y) is the weight of the edge or 0 if there is no edge.
  #' @param heuristic an estimation of distance from node x to y that is guaranteed to be lower than the actual distance. E.g. straight-line distance
  #' @param start the node to start from.
  #' @param goal the node we're searching for
  #' @return The shortest distance to the goal node. Can be easily modified to return the path.

  # This contains the distances from the start node to all other nodes, initialized with a distance of "Infinity"
  distances = rep(Inf, nrow(graph))
  
  # The distance from the start node to itself is of course 0
  distances[start] = 0
  
  # This contains the priorities with which to visit the nodes, calculated using the heuristic.
  priorities = rep(Inf, nrow(graph))
  
  # start node has a priority equal to straight line distance to goal. It will be the first to be expanded.
  priorities[start] = heuristic[start,goal]
  
  # This contains whether a node was already visited
  visited = rep(FALSE, nrow(graph))
  best_path = list()
  # While there are nodes left to visit...
  repeat {
    # ... find the node with the currently lowest priority...
    lowest_priority = Inf
    lowest_priority_index = -1
    for(i in seq_along(priorities)) {
      # ... by going through all nodes that haven't been visited yet
      if(priorities[i] < lowest_priority && !visited[i]){
        lowest_priority = priorities[i]
        lowest_priority_index = i
      }
    }
    if (lowest_priority_index == -1){
      # There was no node not yet visited --> Node not found
      return (-1)
    } else if (lowest_priority_index == goal){
	  print(distances)
	  low<-distances[lowest_priority_index]
	  #this kinda sucks but i barely have any experience working with R script
	  print(best_path)
      # Goal node found
      print("Goal node found!")
      return(low)
    }
    cat("\tVisiting node ", lowest_priority_index, " with currently lowest priority of ", lowest_priority)
    # list for the best path
	



    # ...then, for all neighboring nodes that haven't been visited yet....
    for(i in seq_along(graph[lowest_priority_index,])) {
      if(graph[lowest_priority_index,i] != 0 && !visited[i]){
        # ...if the path over this edge is shorter...
        if(distances[lowest_priority_index] + graph[lowest_priority_index,i] < distances[i]){
          # ...save this path as new shortest path
          distances[i] = distances[lowest_priority_index] + graph[lowest_priority_index,i]
		  #print path till now

		  cat("\n",lowest_priority_index,"->",i, "\n")
		  #append to list
		  best_path <- c(best_path, paste(lowest_priority_index,"->",i))

          # ...and set the priority with which we should continue with this node
          priorities[i] = distances[i] + heuristic[i,goal]
          cat("\tUpdating distance of node ", i, " to ", distances[i], " and priority to ", priorities[i], "\n")
        }
        # Lastly, note that we are finished with this node.
        visited[lowest_priority_index] = TRUE
        cat("\tVisited nodes: ", visited, "\n")
        cat("\tCurrently lowest distances: ", distances, "\n")
      }
    }
  }
}
# nao estudei o suficiente para saber como calcular a heuristica
heuristics <- scan('heuristics.txt')
heuristics <- matrix(heuristics, ncol = 8, byrow = TRUE)

print(a_star(mat, heuristics, 1, 8))