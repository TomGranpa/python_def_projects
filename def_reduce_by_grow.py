def grow(arr):
	a=1
	for x in arr:
		a*=x
	return a 

lista = [10,2,3,6]
 
print (grow(lista))