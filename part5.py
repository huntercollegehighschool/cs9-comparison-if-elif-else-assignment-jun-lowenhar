'''
______
PART 5
______

Write a program that asks the user to enter the name of a month as a string. The program will then print how many days that month could have in any given year, or print a statement saying that what the user entered is not the name of a month.

(Hint: This should require only four code blocks, but it can be done with 12 or more if you insist. If you are familiar with lists or other container datatypes, you may implement this using those, though it still requires four code blocks)

Four examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a month:  March
31

Enter a month:  June
30

Enter a month:  February
28 or 29

Enter a month:  Saturday
not a month
'''

#start writing your code below

print("Welcome, peasant. I am the great knower. You wish to know how many days are in a month. I shall tell.")

month = input("Please write the month you are inquiring about on this slip of parchment. Feel privileged. A peasant like you should never be allowed to write on court-quality parchment: ")

if month == "January":
  print("ah, the month of january, when we celebrate the rebirth of the world. funny time to do it, seeing as it's so cold and dead all over. it has thirty-one days.")

elif month == "February":
  print("february, my least favorite month. oh, how dark and windy it is! it has twenty-eight days, but not always. i'm sure you wouldn't understand if i tried to explain it to you. after all, you're a peasant.")

elif month == "March":
  print("march! life begins to return to the land. oh, how i always look forward to being able to stroll the grounds without a heavy cloak. it has thirty-one days.")

elif month == "April":
  print("april is an awfully dreary month. the rain makes all impatient for the beauty of summer to begin. it has thirty days.")

elif month == "May":
  print("at last, true spring beauty! may brings an end to the rain, and one can finally enjoy the flowers along every kingdom road. it has thirty-one days.")

elif month == "June":
  print("oh, why must we swelter so in june? all of the beauty of may combined with the intolerable heat of summer. it has thirty days.")

elif month == "July":
  print("though the heat will continue to be unbearable, july brings the unique beauty of summer. the trees grow lush with beautiful deep greens. it has thirty-one days.")

elif month == "August":
  print("by august, the heat has dragged on for too long. the lushness of the trees begins to wilt. it has thirty-one days.")

elif month == "September":
  print("september is a drowsy month. y'all peasants are so lazy during this time, waiting for the cool relief that is right around the corner. it has thirty days.")

elif month == "October":
  print("at last, in october, the cool and the harvest has arrived. the peasants now get off their lazy bums. it has thirty-one days.")

elif month == "November":
  print("in november, the harvest has died down, but the peasants are still forced to toil in the fields. us nobles greatly enjoy watching the peasants tire and die during this month. it has thirty days.")

elif month == "December":
  print("december, a month of festivities. which is strange, because everything is dead during december. it has thirty-one days.")

elif (month == "january") or (month == "february") or (month == "march") or (month == "april") or (month == "may") or (month == "june") or (month == "july") or (month == "august") or (month == "september") or (month == "october") or (month == "november") or (month == "december"):
  print("don't they teach you to capitalize proper nouns?! i knew i shouldn't have wasted this parchment on a peasant.")

else:
  print("that isn't a month! i knew i shouldn't have wasted this parchment on a peasant. thanks a lot.")