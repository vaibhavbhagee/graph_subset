

f = open('test.satoutput','r')
all_lines = list(f)

f1 = open('var_vals.txt', 'r')
l = f1.readline()
ll = l.split()

n1 = int(ll[0])
n2 = int(ll[1])

f2 = open('test.mapping','w');

if all_lines[0] == "UNSAT\n" :
	f2.write('0\n')
else : 
	vals = all_lines[1].split()

	# Start from line nos n1^2 + n2^2 ->
	i = 0

	while i < len(vals) - 1:
		vv = int(vals[i]) 
		if vv > 0 :
			v = vv
			q = (v/n2)+1;
			r = (v % n2);
			if r == 0:
				r += n2
				q -= 1
			f2.write(str(q)+' '+str(r)+'\n')
		i += 1