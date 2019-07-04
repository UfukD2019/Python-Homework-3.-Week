print("********** Calculation of Area and Volume **********\n\n\n")
print("""This is an area and volume calculation program.
Please enter the code of operation you would like to do.

The area calculation:
 For triangle, please press  "1"
 For square,  please press   "2"
 For rectangle, please press "3"

The volume calculation:
 For cube, please press      "4"
 For sphere, please press    "5"
 For cone, please press      "6"

""")
while True:
 try:
  operation=input("Please enter the code of operation you would like to do.\n")
  if operation=="1":
    base=float(input("Please enter the base length value of the triangle\n"))
    height=float(input("Please enter the height value of the triangle\n"))
    if base<=0 or height<=0:
        raise Exception("Base lenght or height value can not be less than or equal to zero!!!")
    area=(base*height)/2
    print("The area of the triangle is: ",round((area),5))
    break
  elif operation=="2":
    side=float(input("Please enter the side length value of the square\n"))
    if side<=0:
        raise Exception("Side lenght value can not be less than or equal to zero!!!")
    area=pow(side,2)
    print("The area of the square is: ",round((area),5))
    break
  elif operation=="3":
    long=float(input("Please enter the long side length value of the rectangle\n"))
    short=float(input("Please enter the short side length value of the rectangle\n"))
    if long<=0 or short<=0:
        raise Exception("Long side or short side lenght value can not be less than or equal to zero!!!")
    area=long*short
    print("The area of the rectangle is: ",round((area),5))
    break
  elif operation=="4":
    side=float(input("Please enter the side length value of the cube\n"))
    if side<=0:
        raise Exception("Side lenght value can not be less than or equal to zero!!!")
    volume=pow(side,3)
    print("The volume of the cube is: ",round((volume),5))
    break
  elif operation=="5":
    pi=3.14
    radius=float(input("Please enter the radius value of the sphere\n"))
    if radius<=0:
        raise Exception("Radius value can not be less than or equal to zero!!!")
    volume=(4/3)*(pi)*(pow(radius,3))
    print("The volume of the sphere is: ",round((volume),5))
    break
  elif operation=="6":
    pi=3.14
    radius=float(input("Please enter the radius value of the cone\n"))
    height=float(input("Please enter the height value of the cone\n"))
    if radius<=0 or height<=0:
        raise Exception("Radius or height value can not be less than or equal to zero!!!")
    volume=(1/3)*(pi)*(pow(radius,2))*(height)
    print("The volume of the cone is: ",round((volume),5))
    break
  else:
    print("The operation code you entered is incorrect. Please check and follow the instruction")
 except ValueError as error:
     print("Please enter only number!!!")
     print("The original message of error is",error)
 except BaseException as error:
     print(error)
