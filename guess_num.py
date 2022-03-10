import random
r = random.randint(1,100)
count = 0
while True:
	count += 1
	num = input('please guess number:')
	num = int(num)
	if num == r:
		print('that is correct')
		print('this is your', count, 'guess')
		break
	elif num > r:
		print('guess lower number')
	elif num < r:
		print('guess higher number')
	print('this is your', count, 'guess')