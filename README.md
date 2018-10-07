## Sub-Graph Isomorphism

### Problem Statement
* There are two directed graphs G and G’. The graphs do not have self-edges. 
* The task is to find a one-one mapping M from nodes in G to nodes in G’ such that there is an edge from v1 to v2 in G if and
only if there is an edge from M(v1) to M(v2) in G'.
* We use [miniSAT](http://minisat.se/), a complete SAT solver for this problem. 
* The code reads two graphs in the given input format and converts the mapping problem into a CNF SAT formula. 
* The SAT formula will is input to miniSAT, which returns a variable assignment that satisfies the formula (or an
answer "no", signifying that the problem is unsatisfiable). 
* The SAT assignment is then converted into a mapping from nodes of G to nodes of G' and output in the given output format.

### Input format
* Nodes are represented by positive integers starting from 1. Each line represents an edge from the first node to the second. 
* Both graphs are presented in the single file, the larger first. 
* The line with "0 0" is the boundary between the two. 
* Sample input:
```
1 2
1 3
1 4
2 4
3 4
0 0
1 2
3 2
```

### Output format
* The mapping should map each node of G into a node id for G’. 
* The first numbers on each line represent a node as numbered in the smaller graph G, and the second number represents the node of the larger graph G’ to which it is mapped. 
* Output for the sample input:
```
1 2
2 4
3 3
```
* If the problem is unsatisfiable output a 0.
