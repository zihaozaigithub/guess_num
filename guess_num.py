import random
start = input('please enter start number')
end = input('please enter end number')
start = int(start)
end = int(end)
r = random.randint(start, end)
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
