'''
______
PART 3
______
Write a program that asks the user to input one integer. The program will then print two strings, one stating if it's positive, negative, or zero, and another that states whether or not is is divisible by 3. (Hint: to check divisibility by 3, you will find using the modulus(%) operation very helpful.)

3 examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a number:  -2
negative
not divisible by 3

Enter a number:  0
zero
divisible by 3

Enter a number:  5
positive
not divisible by 3
'''

#write your code below

number = int(input("Enter a number for your overlord, you lowly peasant: "))

if number < 0:
  print("eugh, a NEGATIVE number?! you're banished!!!")

elif number == 0:
  print("zero? fine, i guess. dismissed. return to your pathetic little village.")

else:
  print("a positive number! well done! you shall be given a sack of gold!")

if ((number < 0) or (number == 0)) and ((number % 3) == 0):
  print("but lo! a number divisible by three? you have redeemed yourself. please accept a sack of gold.")

elif ((number < 0) or (number == 0)) and ((number % 3) > 0):
  print("wait, it's also not divisible by three? good heavens, what an abomination! you shall be thrown in prison to await execution tomorrow at noon.")

elif (number > 0) and ((number % 3) == 0):
  print("AND it is divisible by three! good job! you shall be brought to live at the finest palace in our court!")

elif (number > 0) and ((number % 3) > 0):
  print("alas, it isn't divisible by three. greater rewards were to be offered, but apparently not to you. leave with your gold.")