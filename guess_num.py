import random
r = random.randint(1,100)
while True:
	num = input('please guess number:')
	num = int(num)
	if num == r:
		print('that is correct')
		break
	elif num > r:
		print('guess lower number')
	elif num < r:
		print('guess higher number')