def reverse_list(l): #1 wariant
	l.reverse()
	return l  	

x = [1,2,3]

print (reverse_list(x))

def reverse_list(l): #2 wariant
	return l[::-1] 	

x = [1,2,3]

print (reverse_list(x))