import random


print ("input a positive range only ")
num1 = int(input("Imput the first number: "))
num2 = int(input("Imput the second number: "))
if num1 < 0 or num2 < 0:
	print("Incorrect range ")
else :
	number = int(random.uniform(num1,num2))
	print ("The range is from " +str(num1)+ " to " + str(num2))

	guess = None

	while guess != number:
		guess = int(input("Try a guess "))
		if guess > number :
			print("Too High")
		if guess < number :
			print("Too Low")

print("you win")


