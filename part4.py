'''
______
PART 4
______
Write a program that prompts the user to enter two integer inputs. The program prints a string stating if the inputs are both positive, negative, if one of the inputs is zero, or if they have opposite signs. (Hint: this code can be written using only four code blocks, but you may find ways to do this using more.)

Four examples of what should appear on the console when this program runs (note: the test driver is case sensitive):

Enter a number:  3
Enter another number:  7
positive

Enter a number:  -5
Enter another number:  -2
negative

Enter a number:  7
Enter another number:  0
zero

Enter a number:  2
Enter another number:  -2
opposite
'''

#start writing your code below

number1 = int(input("Enter a number into the chalice: "))

number2 = int(input("Enter another number into the chalice if you know what's good for you: "))

if (number1 > 0) and (number2 > 0):
  print("ah! very good! two positive numbers! you are free to go immediately!")

elif ((number1 > 0) and (number2 == 0)) or ((number1 == 0) and (number2 > 0)):
  print("alright, you have submitted a positive number, but the other number is zero. you will be released soon.")

elif ((number1 < 0) and (number2 == 0)) or ((number1 == 0) and (number2 < 0)):
  print("a negative number? you know how we feel about those around here. you put a zero as your other number, but at least it wasn't another negative. very well. you will be able to try again, but only after one year's time.")

elif ((number1 == 0) and (number2 == 0)):
  print("oh, you're really trying to get on my nerves, aren't you. ugh, fine. you shall be allowed to try again, despite your... two zeroes.")

elif ((number1 < 0) and (number2 < 0)):
  print("no! TWO NEGATIVES! guards, throw this prisoner off yonder cliff!!")

elif ((number1 < 0) and (number2 > 0)) or ((number1 > 0) and (number2 < 0)):
  print("a negative... and a positive... i can see why you're in prison. back to your cell!")