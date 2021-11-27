'''
______
PART 1
______
The code below prompts the user to enter two numbers, and then prints out the smaller of the numbers entered. Modify so that it prompts the user to enter THREE numbers, and then prints the smallest of the three numbers entered in a sentence.

(Hint: You'll need to be careful for the cases when the user enters the same number twice or all three times.)

An example of what should appear on the console when the code is run:

Enter a number: 11
Enter another number: 2
Enter another number: 5

The smallest number is 2
'''

print("Welcome to the kingdom tax booth. Today's tax is three numbers. You will be permitted to keep the smallest of those numbers.")

number1 = int(input("Hand over your first number to the tax collector: "))

number2 = int(input("Hand over your second number to the tax collector: "))

number3 = int(input("Hand over your third number to the tax collector: "))

if number1 < number2:
  smol = number1
  
else:
  smol = number2

if smol < number3:
  smallest = smol

else:
  smallest = number3

print ("The smallest number is", smallest, "only. You may keep it. Take it! Thank you for bowing down to the overlord. Now leave!") 