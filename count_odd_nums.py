def sums (numb):
#1 sposób:
	new_list=[]
	for n in range (0, numb):
		if n%2 != 0:
			new_list.append(n)
	return len(new_list)

print (sums(15023))

#2 sposób
return sum(1 for i in range(n) if i %2 != 0)

#3 sposób 
return n//2