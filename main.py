print("You, a peasant, have arrived at the peasant's forum, which is literally the only place in the entire kingdom where peasants can get any help from the government. Why have you come here?")

program = input("Enter 1 if you are here to pay your tax, 2 if you wish to enter the lottery, 3 if you want to enter the overlord's contest, 4 if you want to get out of prison, or 5 if you seek knowledge: ")

while program not in ['1', '2', '3', '4', '5']:
  print("Peasants can't go there.")
  program = input("Enter 1 if you are here to pay your tax, 2 if you wish to enter the lottery, 3 if you want to enter the overlord's contest, 4 if you want to get out of prison, or 5 if you seek knowledge: ")
  
if program == '1':
  import part1
  
elif program == '2':
  import part2
  
elif program == '3':
  import part3
  
elif program == '4':
  import part4
  
elif program == '5':
  import part5
