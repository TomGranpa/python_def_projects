while True:
	reply = input("Wpisz tekst: ")
	if reply == "stop":
		break
	elif not reply.isdigit():
		print ("Źle " * 5)
	else:
		num=int(reply)
		if num>30:
			print ("Za dużo")
		else:
			print (num**2)
print ("KONIEC")


