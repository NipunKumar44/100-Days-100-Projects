print("Welcome to the bill calculator!")
a=int(input("What was the total bill?"))
b=int(input("How much % tip would you like to give?"))
c=int(input("How many people should split the bill?"))
print(f"Each person should pay: {(a*(b/100)+a)/c}")