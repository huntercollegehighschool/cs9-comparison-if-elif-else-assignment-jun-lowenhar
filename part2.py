'''
______
PART 2
______
In the code below, the user is asked to enter three numbers, and then prints a single statement depending on how many of the input numbers are equal. However, there are (at least) 6 syntax errors in the code that need to be fixed. Even after all the syntax errors are fixed and the code runs without errors, there is still a bug. Fix the code so that it runs the way it should.

(Hint: If you see a red squiggly line in the code, that probably means there is a syntax error there.)
'''

print("Welcome to the peasant's lottery. It seems like you're another foolish peasant who thinks luck will win them enough gold to escape poverty. Why did you become a peasant in the first place, then? Your luck will be decided by whatever three numbers you submit.")

num1 = int(input("Give a number to the attendant: "))

num2 = int(input("Give another number to the attendant: "))

num3 = int(input("Hand over another number, it's three numbers that we asked for ain't it: "))

if(num1 == num2 == num3):
  print("all three numbers are equal! take three sacks of gold.")

elif(num1 == num2 or num2 == num3 or num1 == num3):
  print("exactly two of the numbers are equal. take two sacks of gold.")

else:
  print("none of the numbers are equal. you get one sack of gold for participation, though. you're welcome.")
