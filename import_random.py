import random
ceil = input('please enter the upper limit you want: ')
floor = input('please enter the lower limit you want: ')
ceil = int(ceil)
floor = int(floor)

i = random.randint(floor, ceil)
k = 0
while True:
	k += 1
	answer = input('please guess the number: ')
	answer = int(answer)
	if answer == i:
		print('congrats!! you use', k, 'chances')
		break
	elif answer > i:
		print('its high')
	elif answer < i:
		print('its low')
	print('you use', k, 'chance')
		