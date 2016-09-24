#!/usr/bin/python
# coding=utf-8
import sys
import copy
import math
import random
# import argparse

"""
Adjust these parameters by hand.  
  the argparse package will not run on attu.cs.washington.edu
"""

G1nodes = int(sys.argv[1]) # number of nodes in larger graph
G1edges = int(sys.argv[2]) # number of edges in larger graph
G2nodes = int(sys.argv[3]) # number of nodes in smaller graph
G2edges = int(sys.argv[4]) # number of edges in smaller graph

guarantee_subgraph = True  # whether to deliberately make G2 a subgraph of G1
allow_self_edges = False  # if true, a node can have an edge to itself
print_digraph = False # if True, print in graphviz format for visualization

def makeGraph(nodeCount, edgeCount):
  if edgeCount > pow(nodeCount,2):
    print "Can't get ", edgeCount, " edges on ", nodeCount, " nodes."
    raise Exception
  if (not allow_self_edges) and edgeCount > math.factorial(nodeCount):
    print "Can't get ", edgeCount, " edges on ", nodeCount, " nodes without edges to self."
    raise Exception
  nodeList = range(1,nodeCount+1) 
  edges = []
  for e in range(edgeCount):
    done = False
    while not done:
      N1 = random.choice(nodeList)
      N2 = random.choice(nodeList)
      done = (N1,N2) not in edges and ( allow_self_edges or N1 != N2)
    edges.append( (N1,N2) )
  return edges

def makeSuperGraph(G1nodes,G1edges,G2nodes,G2edges,G2):
  if G1nodes < G2nodes or G1edges < G2edges:
     print "First Graph should have more nodes than second graph"
     raise Exception
  oldNodes = range(1, G2nodes+1)
  newNodes = range(G2nodes+1, G1nodes+1)
  allNodes = range(1,G1nodes+1)

  newEdges = []
  for i in range( G1edges - G2edges ):
    done = False
    while not done:
      n1 = random.choice(newNodes)
      n2 = random.choice(allNodes)
      if random.choice([True,False]):
        e = (n1,n2)
      else:
        e = (n2,n1)
      done = e not in newEdges and ( allow_self_edges or n1 != n2)
    newEdges.append(e)
    superGraph = newEdges+G2
    # superGraph.sort() # if you want to obfuscate the subgraph
  return superGraph
  SubGraph = copy.copy(Graph)
  for i in range( len(Graph) - n ):
    e = random.choice(SubGraph)
    SubGraph.remove(e)
  return SubGraph

def renameGraph(N, Graph):
  NewGraph = []
  Nodes = range(1,N+1)
  random.shuffle(Nodes)
  translator = {}
  for e in Graph:
    n1 = Nodes[e[0]-1] 
    n2 = Nodes[e[1]-1]
    NewGraph.append( (n1,n2) )
  return NewGraph

def printSubgraphs(G1,G2):
  print "digraph {"

  print '\tsubgraph clusterG1 { graph [label="G"]'
  for e in G1:
    print "\t\t",  "G"+str(e[0]), "->", "G"+str(e[1])
  print "\t}"

  print '\tsubgraph clusterG2 { graph [label="g"]'
  for e in G2:
    print "\t\t",  "g"+str(e[0]), "->", "g"+str(e[1])
  print "\t}"

  print "}"


def printDigraph():
  print "digraph {"
  for e in edges:
    print "\t",  e[0], "->", e[1]
  print "}"

def printGraph(edges):
  for e in edges:
    print e[0], e[1]

def main():

  G2 = makeGraph(G2nodes,G2edges)
  if guarantee_subgraph:
    G1 = makeSuperGraph(G1nodes,G1edges,G2nodes,G2edges,G2)
    G2 = renameGraph(G2nodes,G2)
  else:   # G1 and G2 are both random graphs
    G1 = makeGraph(G1nodes,G1edges)
  if print_digraph:
    printSubgraphs(G1,G2)
  else:
    printGraph( G1 )
    print "0 0"
    printGraph( G2 )

if __name__ == "__main__":
    main()
