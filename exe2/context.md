# Before running

make shure you have R installed and the library: `expm`.

To install you can do so by pluggin `install.packages("expm")` choose some mirror you trust, i would recomend london as its widely used and close to our location.

## What are those .txt files

matrix.txt represents the adjacency matrix for the node graph

while heuristics.txt represents the heuristics to tell A* algorithm how distant the algorithm is take to reach the goal(in this case we are assuming the least amount of steps instead of an actual distance)

# Running

to run just type R in a linux with R installed and then do source(file="script.r")

# fine you win... what is the result?

on my console running the code results in:

```Loading
Loading required package: Matrix

Attaching package: ‘expm’

The following object is masked from ‘package:Matrix’:

    expm

Read 64 items
     [,1] [,2] [,3] [,4] [,5] [,6] [,7] [,8]
[1,]    0    1    1    0    0    0    0    0
[2,]    0    0    0    1    0    1    0    0
[3,]    0    0    0    0    1    0    0    0
[4,]    0    0    0    0    0    1    0    1
[5,]    0    0    0    0    0    0    1    0
[6,]    0    0    0    0    0    0    1    1
[7,]    0    0    0    0    0    0    0    1
[8,]    0    0    0    0    0    0    0    0
     [,1] [,2] [,3] [,4] [,5] [,6] [,7] [,8]
[1,]    0    1    1    1    1    2    3    6
[2,]    0    0    0    1    0    2    2    5
[3,]    0    0    0    0    1    0    1    1
[4,]    0    0    0    0    0    1    1    3
[5,]    0    0    0    0    0    0    1    1
[6,]    0    0    0    0    0    0    1    2
[7,]    0    0    0    0    0    0    0    1
[8,]    0    0    0    0    0    0    0    0
[1] "The actual solution for the number of paths is:  6"
Read 64 items
        Visiting node  1  with currently lowest priority of  3
 1 -> 2 
        Updating distance of node  2  to  1  and priority to  3 
        Visited nodes:  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE 
        Currently lowest distances:  0 1 Inf Inf Inf Inf Inf Inf 

 1 -> 3 
        Updating distance of node  3  to  1  and priority to  4 
        Visited nodes:  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE 
        Currently lowest distances:  0 1 1 Inf Inf Inf Inf Inf 
        Visiting node  2  with currently lowest priority of  3
 2 -> 4 
        Updating distance of node  4  to  2  and priority to  3 
        Visited nodes:  TRUE TRUE FALSE FALSE FALSE FALSE FALSE FALSE 
        Currently lowest distances:  0 1 1 2 Inf Inf Inf Inf 

 2 -> 6 
        Updating distance of node  6  to  2  and priority to  3 
        Visited nodes:  TRUE TRUE FALSE FALSE FALSE FALSE FALSE FALSE 
        Currently lowest distances:  0 1 1 2 Inf 2 Inf Inf 
        Visiting node  4  with currently lowest priority of  3  Visited nodes:  TRUE TRUE FALSE TRUE FALSE FALSE FALSE FALSE 
        Currently lowest distances:  0 1 1 2 Inf 2 Inf Inf 

 4 -> 8 
        Updating distance of node  8  to  3  and priority to  3 
        Visited nodes:  TRUE TRUE FALSE TRUE FALSE FALSE FALSE FALSE 
        Currently lowest distances:  0 1 1 2 Inf 2 Inf 3 
        Visiting node  6  with currently lowest priority of  3
 6 -> 7 
        Updating distance of node  7  to  3  and priority to  4 
        Visited nodes:  TRUE TRUE FALSE TRUE FALSE TRUE FALSE FALSE 
        Currently lowest distances:  0 1 1 2 Inf 2 3 3 
        Visited nodes:  TRUE TRUE FALSE TRUE FALSE TRUE FALSE FALSE 
        Currently lowest distances:  0 1 1 2 Inf 2 3 3 
[1]   0   1   1   2 Inf   2   3   3
[[1]]
[1] "1 -> 2"

[[2]]
[1] "1 -> 3"

[[3]]
[1] "2 -> 4"

[[4]]
[1] "2 -> 6"

[[5]]
[1] "4 -> 8"

[[6]]
[1] "6 -> 7"

[1] "Goal node found!"
[1] 3
```

Which says pretty much that the number of possible path to reach the v8 is 6, the path which least amount of steps is 3, and that path is v1 -> v2 -> v4 -> v8

I couldnt get it to just print out the path neetly as im kinda new to R scriptting

Also the A* algorithm implementation is not mine i just changed it a little because it was barely understandable before

I couldnt think of a good way of developing the heuristics matrix thats why i manually typed it in, although from testing i have an idea that the adjacency matrix will also work(although i imagine it wont give  excelent results due to the heuristics being pretty much 0 all the time)

## we said PYTHON!!

;) check the pdf, on the second exercise theres nothing mentioned for it
