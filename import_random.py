import random
i = random.randint(1, 100)
while True:
	answer = input('please guess the number: ')
	answer = int(answer)
	if answer == i:
		print('congrats!!')
		break
	elif answer > i:
		print('its high')
	elif answer < i:
		print('its low')
		