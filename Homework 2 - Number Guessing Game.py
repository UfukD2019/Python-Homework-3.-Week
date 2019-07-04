print("********** Number Guessing Game **********\n\n\n")
print("""This is a number guessing program.
Please guess a number from 1 to 100.\n""")
for i in range (1,101):
 guess=int(input("Please guess a number from 1 to 100.\n"))
 number=50
 difference=guess-number
 if difference in range(-50,-30):
     print("Your prediction is too low. Please enter a higher number!")
 elif difference in range (-30,-5):
     print("Your prediction is low. Please enter a higher number!")
 elif difference in range (-5,0):
     print("Your prediction is so close. Please increase your prediciton very little!")   
 elif difference in range (31,51):
     print("Your prediction is too high. Please enter a lower number!")
 elif difference in range (6,31):
     print("Your prediction is high. Please enter a lower number!")
 elif difference in range (1,6):
     print("Your prediction is so close. Please decrease your prediciton very little!")
 elif guess==number:
     print("Congratulations!!! You predict the number in ",i,". trial. Well done.",sep="")
     break


        
    
        
