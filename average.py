
# [1, 5, 7 ,8 , 4, 3]

def iterate(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]

def average_scores(scores):
	for i in range(0, len(scores)):
		total = (scores[0]+scores[1]+scores[3]+scores[4]+scores[5]):
		average = total / 5
# filter pattern
def congratulations(scores):
	for i in range(0, len(scores)):
		if (scores[i] <= 100):
			print "average test score:" + average 
