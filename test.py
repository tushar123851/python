
#display the welcome message
print("Welcome to the Interactive Personal Data Collector!")
print("\n")
#taken the input from user
name = str(input("Please enter your name:"))
age = int(input("Please enter your age:"))
height = float(input("Please enter your height in meters:"))
fnumber = int(input("Please enter your favourite number:"))
print("\n")

#display thank u  message for giving information
print("Thank you! Here is the information we collected")
print("\n")

#display all the information name,age,height,favourite number

print("Name :","(Type:",name,type(name),",","Memory Address:",id(name),")")
print("Age :","(Type:",age,type(age),",","Memory Address:",id(age),")")
print("Height :","(Type:",height,type(height),",","Memory Address:",id(height),")")
print("Favourite Number :","(Type:",fnumber,type(fnumber),",","Memory Address:",id(fnumber),")")

#calculation
currentyear = 2025
birthyear = currentyear - age
print("\n")

#display birth year based on age
print("your birth year is approximately: ",birthyear ,"(","Based on your age of ",age,")")
print("\n")

#end message
print("Thank you for using the personal data collector.Goodbye!")


