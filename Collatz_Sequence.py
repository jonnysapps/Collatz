def even(number):
	return int(number) // 2

def odd(number):
	return 3 * int(number) + 1
	
def collatz():
	number = int(input("Please enter any integer: "))
	while number != 1:
		if(number%2 == 0):
			number = even(number)
			print(number)
			time.sleep(0.1)
		else:
			number = odd(number)
			print(number)
			time.sleep(0.1)
	time.sleep(1)
	print("Collatz stands true!")

def intro():
	print("The Collatz Calculator runs off one integer input")
	time.sleep(3)
	print("")
	print("If the integer is even it will be divided by two")
	time.sleep(3)
	print("")
	print("If it is odd it will be multiplied by three and then have one added to it")
	time.sleep(4)
	print("")
	print("This process is then repeated with the new value")
	time.sleep(3)
	print("")
	print("We should always end up at 1")
	time.sleep(2)
	print("")

import time
start = input("Would you like me to explain the Collatz Sequence? (y/n): ")
if(start == "y"):
	intro()
while True:
		try:
			collatz()
		except ValueError:
			print("Error: Please enter an integer!")
		time.sleep(1)
		tryagain = input("Try again? (y/n): ")
		if(tryagain == "n"):
			print("Okay, until next time!")
			break
time.sleep(1)