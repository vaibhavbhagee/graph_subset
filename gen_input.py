#!/usr/bin/python
# coding=utf-8
import time

start_time = time.time();

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

AdjG2_in = [[] for j in range(n2)]
AdjG2_out = [[] for j in range(n2)]
AdjG1_in = [[] for j in range(n1)]
AdjG1_out = [[] for j in range(n1)]

i = 0

while all_lines[i] != '0 0\n':
	nos = all_lines[i].split()
	x = int(nos[0]) - 1
	y = int(nos[1]) - 1
	EdgesG2[x][y] = 1
	AdjG2_in[y].append(x)
	AdjG2_out[x].append(y)
	i += 1

i += 1

while i < len(all_lines):
	nos = all_lines[i].split()
	x = int(nos[0]) - 1
	y = int(nos[1]) - 1
	EdgesG1[x][y] = 1
	AdjG1_in[y].append(x)
	AdjG1_out[x].append(y)
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
	return str(n2*j + i + 1)




# def getvar12( x,  j,  i):
# 	if x == 1:
# 		return str(j*n1 + i + 1)
# 	else:
# 		return str(n1**2 + j*n2 + i + 1)



# put some vals of 
NotPoss = {}

for i in range(n1):
	for j in range(n2):
		if len(AdjG2_out[j]) < len(AdjG1_out[i]) or len(AdjG2_in[j]) < len(AdjG1_in[i]) :
			NotPoss[(i,j)] = True;

# now we know the ones that are not possible.

for i in range(n1):
	s = ''
	for j in range(n2):
		if (i,j) not in NotPoss:
			s += (getvarno(i,j) + ' ')
	s += '0\n'
	f.write(s)

# f.flush()

for i in range(n1):
	for j in range(n2):
		for k in xrange(j+1,n2,1):
			if (i,j) not in NotPoss and (i,k) not in NotPoss:
				f.write('-' + getvarno(i,j) + ' -' + getvarno(i,k) + ' 0\n')

# f.flush()

for i in range(n2):
	for j in range(n1):
		for k in xrange(j+1,n1,1):
			if (j,i) not in NotPoss and (k,i) not in NotPoss:
				f.write(getvarno(j,i) + ' ' + getvarno(k,i) + ' 0\n')

# f.flush()

for i in range(n1):
	for j in range(n1):
		if i != j:
			for k in range(n2):
	# print time.time() - start_time
	# print "Loop for i finished"
	# print i
				if (i,k) not in NotPoss:
					if EdgesG1[i][j]:
						s = ""
						s = s + "-" + getvarno(i,k) + " "
						for x in AdjG2_out[k]:
							if (j,x) not in NotPoss:
								s+=getvarno(j,x)+" "
						s+="0\n"
						f.write(s)
					else:
						for x in AdjG2_out[k]:
							if (j,x) not in NotPoss:
								f.write("-" + getvarno(i,k)+" -"+getvarno(j,x)+" 0\n")

for p in NotPoss:
	(x,y) = p
	f.write("-" + getvarno(x,y)+" 0\n")

print time.time() - start_time
				# for l in range(n2):
				# 	if (k != l):
				# 			if EdgesG2[k][l] != EdgesG1[i][j] and (i,k) not in NotPoss and (j,l) not in NotPoss:
				# 				f.write(getvarno(i,k) + ' ' + getvarno(j,l) + ' 0\n')
				# f.flush()
	# print time.time() - start_time
	# print "Loop for i finished"
	# print i
