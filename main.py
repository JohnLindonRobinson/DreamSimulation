import random
import matplotlib.pyplot as plt

def pearl_trade():
	return random.randint(0, 109)<2

def sufficient_pearl(aim=42):
	number_of_pearls = 0
	number_of_attempts = 0
	while number_of_pearls<aim:
		if pearl_trade():
			number_of_pearls+=random.choice([2, 3, 4])
		number_of_attempts+=1
	return number_of_attempts, number_of_attempts<=262

# print(sufficient_pearl())


def blaze_drop():
	return random.choice([True, False])

def sufficient_blaze(aim=211):
	number_of_rods = 0
	number_of_attempts = 0
	while number_of_rods<aim:
		if blaze_drop():
			number_of_rods+=1
		number_of_attempts+=1
	return number_of_attempts, number_of_attempts<=305

# print(sufficient_blaze())

def main_loop():
	number_of_tests = 0
	pearl_successes = 0
	blaze_successes = 0
	current_lowest_pearl =99999
	current_lowest_blaze =99999
	while True:
		show = False
		pearl_attempts, pearl_success = sufficient_pearl()
		blaze_attempts, blaze_success = sufficient_blaze()
		if pearl_success:
			pearl_successes+=1
			show = True
		if blaze_success:
			blaze_success+=1
			show = True
		number_of_tests+=1
		if pearl_attempts<current_lowest_pearl:
			current_lowest_pearl= pearl_attempts
			print("New lowest pearl run is test ", str(number_of_tests), " with ", str(current_lowest_pearl), " trades")
		if blaze_attempts<current_lowest_blaze:
			current_lowest_blaze= blaze_attempts
			print("New lowest blaze run is test ", str(number_of_tests), " with ", str(current_lowest_blaze), " kills")
				
		if show:
			print("After test ", str(number_of_tests), " there are ", str(pearl_successes), "pearl successes and ", str(blaze_successes), "blaze successes. Seed", str(pearl_attempts), " and " ,str(blaze_attempts))
			print((pearl_successes*100)/number_of_tests, (blaze_successes*100)/number_of_tests)

main_loop()