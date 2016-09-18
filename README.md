# graph_subset

ASSIGNMENT 2: GRAPH SUBSET MAPPING

Problem Statement: 
There are two directed graphs G and G’. The graphs do not have self-edges. Find a
one-one mapping M from nodes in G to nodes in G’ such that there is an edge from v1 to v2 in G if and
only if there is an edge from M(v1) to M(v2) in G'. Sample cases are shown here.
We will use miniSAT, a complete SAT solver for this problem. Your code will read two graphs in the given
input format. You will then convert the mapping problem into a CNF SAT formula. Your SAT formula will
be the input to miniSAT, which will return with a variable assignment that satisfies the formula (or an
answer "no", signifying that the problem is unsatisfiable). You will then take the SAT assignment and
convert it into a mapping from nodes of G to nodes of G'. You will output this mapping in the given
output format.
You are being provided a problem generator that takes inputs of the sizes of G and G’ and generates
random problems with those parameters. 

Input format:
Nodes are represented by positive integers starting from 1. Each line represents an edge from the first
node to the second. Both graphs are presented in the single file, the larger first. The line with "0 0" is the
boundary between the two. The input file that represents the last example in the slide is:
1 2
1 3
1 4
2 4
3 4
0 0
1 2
3 2

Output format:
The mapping will map each node of G into a node id for G’. The first numbers on each line represent a
node as numbered in the smaller graph G, and the second number represents the node of the larger
graph G’ to which it is mapped. The output of the same problem is
1 2
2 4
3 3
If the problem is unsatisfiable output a 0.
