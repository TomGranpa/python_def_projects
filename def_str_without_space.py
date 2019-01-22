# 1 wariant
def no_space(x):
	 return "".join(x.split())

k = "Tra la la"
print (no_space(k))

# 2 wariant
def no_space(x):
	 return x.replace(" ","")