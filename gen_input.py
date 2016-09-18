#!/usr/bin/python
# coding=utf-8

f = open('test.graphs', 'r')

all_lines = list(f)

for line in all_lines:
	print line

# u have the file now.

n2 = 0
n1 = 0
i = 0

while all_lines[i] != '0 0\n':
	nos = all_lines[i].split()
	n2 = max(n2,int(nos[0]), int(nos[1]))
	i += 1

i += 1

while i < len(all_lines):
	nos = all_lines[i].split()
	n1 = max(n1,int(nos[0]), int(nos[1]))
	i += 1

EdgesG2 = [[0 for i in range(n2)] for j in range(n2)]
EdgesG1 = [[0 for i in range(n1)] for j in range(n1)]

i = 0

while all_lines[i] != '0 0\n':
	nos = all_lines[i].split()
	EdgesG2[int(nos[0]) - 1][int(nos[1]) - 1] = 1
	i += 1

i += 1

while i < len(all_lines):
	nos = all_lines[i].split()
	EdgesG1[int(nos[0]) - 1][int(nos[1]) - 1] = 1
	i += 1

# matrices ready!!
# no vars for 
f1 = open('var_vals.txt', 'w')
f1.write(str(n1) + ' ' + str(n2))
f1.close()

num_vars = (n1*n2)
num_const = n1 + n1*(n2*(n2-1))/2 + n2*(n1*(n1 - 1)/2) + (n1*(n1-1)*n2*(n2-1))

f = open('test.satinput', 'w')
f.write('p cnf ' + str(num_vars) + ' ' + str(num_const) + '\n')

# edges in G1 consts:
# varno = 1
# for i in range(n1):
# 	for j in range(n1):
# 		if EdgesG1[i][j] == 0:
# 			f.write('-' + str(varno) + ' 0\n')
# 		else:
# 			f.write(str(varno) + ' 0\n')
# 		varno += 1

# for i in range(n2):
# 	for j in range(n2):
# 		if EdgesG2[i][j] == 0:
# 			f.write('-' + str(varno) + ' 0\n')
# 		else:
# 			f.write(str(varno) + ' 0\n')
# 		varno += 1

# n2^2 + n1^2 done.

def getvarno( j,  i):
	return str(n1**2 + n2**2 + n2*j + i + 1)


for i in range(n1):
	s = ''
	for j in range(n2):
		s += (getvarno(i,j) + ' ')
	s += '0\n'
	f.write(s)

f.flush()

for i in range(n1):
	for j in range(n2):
		for k in xrange(j+1,n2,1):
			f.write('-' + getvarno(i,j) + ' -' + getvarno(i,k) + ' 0\n')

f.flush()

for i in range(n2):
	for j in range(n1):
		for k in xrange(j+1,n1,1):
			f.write('-' + getvarno(j,i) + ' -' + getvarno(k,i) + ' 0\n')

f.flush()

def getvar12( x,  j,  i):
	if x == 1:
		return str(j*n1 + i + 1)
	else:
		return str(n1**2 + j*n2 + i + 1)


for i in range(n1):
	for j in range(n1):
		if i != j:
			for k in range(n2):
				for l in range(n2):
					if (k != l):
							if EdgesG2[k][l] != EdgesG1[i][j]:
								f.write('-' + getvarno(i,k) + ' -' + getvarno(j,l) + ' 0\n')
				f.flush()