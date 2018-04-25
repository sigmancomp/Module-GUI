import random
import math

memory = set()

def get_random_id():
	while True:
		num = random.randint(1000,9999)
		if num in memory:
			continue
		else:
			memory.add(num)
			break
	return num
print("Hello")
print(get_random_id())