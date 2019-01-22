def f (a,g):
	lista_1 = []
	lista_2 = []
	for word in a:
		if g(word): lista_1+=[word]
		else: lista_2+=[word]
	return lista_1, lista_2

cars = ["Audi", "Opel", "Skoda", "VW", "KIA", "Seat"]
anonym_func=lambda x: len (x)==4

print f(cars, anonym_func)