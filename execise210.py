num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
num3 = int(input('Enter a number: '))

sum = num1 + num2 + num3
print(sum)

average = sum / 3
print(average)

product = num1 * num2 * num3
print(product)

if num1 > num2:
	if num1 > num3:
		if num2 > num1:
			if num2 > num3:
				if num3 > num1:
					if num3 > num2:
						print('Largest', num1, num2, num3)	
