

f = open('test.satoutput','r')
f2 = open('test.mapping','w');
all_lines = list(f)

if all_lines[0] == "UNSAT\n" :
	f2.write('0\n')
else: 

	f1 = open('var_vals.txt', 'r')
	all_nodes = list(f1)

	RevMapG1 = {}
	RevMapG2 = {}

	i = 0
	while (all_nodes[i] != "HEHE\n"):
		nos = all_nodes[i].split()
		x = int(nos[0])
		y = int(nos[1])
		RevMapG2[x] = y
		i += 1

	n2 = i
	i += 1

	while (i < len(all_nodes)):
		nos = all_nodes[i].split();
		x = int(nos[0])
		y = int(nos[1])
		RevMapG1[x] = y
		i += 1

	n1 = i - n2 - 1

	# print str(n1), n2

	vals = all_lines[1].split()

	# Start from line nos n1^2 + n2^2 ->
	i = 0
	while i < len(vals) - 1:
		vv = int(vals[i]) 
		if vv < 0 :
			v = -1*vv
			q = (v/n2);
			r = (v % n2) - 1;
			if r == -1:
				r = n2-1
				q -= 1
			# print str(q), r
			f2.write(str(RevMapG1[q])+' '+str(RevMapG2[r])+'\n')
		i += 1