import random
i = random.randint(1, 100)
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
		