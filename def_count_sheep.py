def count_sheep(n):
	x=''
	for i in range (1,n+1):
		x+='{} sheep...'.format (i)
	return x
    	
    	

print (count_sheep(6))

