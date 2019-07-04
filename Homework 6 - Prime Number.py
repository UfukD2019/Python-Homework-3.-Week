print("********** Prime Number **********\n\n\n")
print("""This is a prime number determination program.
This program allows you to find out whether the number you entered is a prime number.
Just enter a number and find out the result.
""")
while True:
 try:
  number=int(input("Please enter a number\n"))
  if number==2 or number==3:
    print(number,"is a prime number.\n")
    operation=input("Would you like to quit the program? If yes, please press 'q'. If no, please press enter.\n")
    if operation=="q" or operation=="Q":
      print("The Program terminated.")
      break
    else:
      continue
  elif number%2==0 or number<=1:
    print(number,"is not a prime number.\n")
    operation=input("Would you like to quit the program? If yes, please press 'q'. If no, please press enter.\n")
    if operation=="q" or operation=="Q":
      print("The Program terminated.")
      break
    else:
      continue
  for digit in range (3,100,2):
   if digit>=number:
    pass
   else:
    result=number%digit
    if result==0:
       print(number,"is not a prime number.\n")
       break
    else:
       print(number,"is a prime number.\n")
       break
  operation=input("Would you like to quit the program? If yes, please press 'q'. If no, please press enter.\n")
  if operation=="q" or operation=="Q":
      print("The Program terminated.")
      break
  else:
      continue
 except ValueError as error:
     print("Please enter only number.")
     print(error)

 
     

