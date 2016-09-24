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

gFile = str(sys.argv[1]) # test input graphs
mapFile = str(sys.argv[2]) # output mapping

def AddNode(G,a):
	if(a[0] in G):
		G[a[0]].append(a[1]);
	else:
		G[a[0]]=[a[1]];
	if(not(a[1] in G)):
		G[a[1]]=[];

def readGraph(fname):
	f=open(fname);
	G1=dict();
	G2=dict();
	chk=-1;
	for lin in f.readlines():
		l=lin.lstrip().rstrip();		
		l=l.split();
		l=[int(a) for a in l];
		if((l[0]==0) and (l[1]==0)):
			chk=1;
			continue;
		if(chk<0):
			AddNode(G1,l);
		else:
			AddNode(G2,l);
	f.close();
	return [G1,G2];

def readMap(fname):
	f=open(fname);
	Map=dict();
	for lin in f.readlines():
		l=lin.lstrip().rstrip();		
		l=l.split();
		l=[int(a) for a in l];
		Map[l[0]]=l[1];
	f.close();
	return Map;

def CheckMap(M,G1,G2):
	try:
		n	=	M.keys();
		n1	=	[M[a] for a in n];
		if(not(len(n1) == len(set(n1)))):
			return False;
		for i in n:
			for j in n:
				if(not (i==j)):
					if(not((j in G2[i]))==(M[j] in G1[M[i]])):
						return False;
		return True;
	except KeyError:
		print("Bad Input: Invalid Node Id");
		return False;

def main():

  	Res=readGraph(gFile);
  	Map=readMap(mapFile);	
  	print(CheckMap(Map,Res[0],Res[1]));
	

if __name__ == "__main__":
    main()
