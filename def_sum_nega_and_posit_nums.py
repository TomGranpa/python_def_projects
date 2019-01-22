def diff_data (nums):
	if not nums: return []
	pos_nums=0
	neg_nums=0
	for num in nums:
		if num>0:
			pos_nums+=1
		elif num<0:
			neg_nums+=num
	return [pos_nums, neg_nums]
	


numery = []
print (diff_data(numery))