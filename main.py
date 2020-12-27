import random
import matplotlib

def pearl_trade():
	return random.uniform(0, 1)<20/423

def sufficient_pearl(aim=10):
	number_of_pearls = 0
	number_of_attempts = 0
	while number_of_pearls<aim:
		if pearl_trade():
			number_of_pearls+=1
		number_of_attempts+=1
	return number_of_attempts, number_of_attempts<10.5

print(sufficient_pearl())

#After researching how many trades it took dream each run, I realised it was more complex than I realised. I decided to commit my work and go to bed for the night