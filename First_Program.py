'''
    This program works like a register 
'''
# Variable
name = input ("Enter your name: ").title()
age = int(input ("Enter your age: "))

# It will check if you are youger than 18
# or older than 18
# and it also prints if you entered a wrong data

if age < 18:
    print ("You are too yourg to keep going!")
elif age > 18:
    print ("You can keep going!")
else:
    print ("wrong answer!")

# Variable
work = input ("What do you do? ").capitalize()

# It will print every information you entered above
print (f"Your name is {name}, you are {age} years old, you're working with {work} and you're gonna be {age+1} next birthday!")