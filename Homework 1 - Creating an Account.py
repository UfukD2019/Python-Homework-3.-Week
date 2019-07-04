print("********** Creating an Account **********")
with open("Account and password list.txt","a"):
 while True:
  username=input("Please create a username:")
  with open("Account and password list.txt","r+") as account:
     data=account.read()
     if username in data:
         print("The username is not available. Please chose a different username.")
         continue
     else:
         password=input("Please create a password:")
         print("Username and password have been successfully created.")
         print("Username is: ",username,"\n","Password is: ",password,"\n",sep="",file=account)
  break
