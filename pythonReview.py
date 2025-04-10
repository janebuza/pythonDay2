# Name : Jane Buza

# print("It worked!");

#------

x = None;

#------

example = "I'm a string"; # The variable example is now holding the string value "I'm a string".
a = 3; # The variable a is now holding the integer value 3.
b = 4.0; # The variable b is now holding the float value 4.0.
c = True; # The variable c is now holding the boolean value True.
d = False; # The variable d is now holding the boolean value False.
e = "Hey!"; # The variable e is now holding the string value "Hey!".
f = None; # The variable f is now holding the None value None.
age = 32; # The variable age is now holding the integer value 32.
name = "Jane"; # The variable name is now holding the string value "Jane".
instrument = "guitar"; # The variable instrument is now holding the string value "guitar".

#------

'''
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
A variable name cannot be any of the Python keywords.


$$$Variable = "bad";

'''

#------

# x = type(3);
# y = type("Hello");
# z = type(True);

#------

# prompt = "Enter your name:\n";
# result = input(prompt);
# print("Hello", result + ",", "how are you?");

#------

# Problem 1:
# userName = input("What is your name?\n");
# userAge = input("What is your age? (int value plz)\n");
# print(userName + ":", type(userName) + ",", userAge + ":", type(userAge));

# Problem 2:
# num1 = int(input("Enter the first number\n"));
# num2 = int(input("Enter the second number\n"));
# if num1 > num2: print(num1, "is greater");
# elif num2 > num1: print(num2, "is greater");
# else: print("Equal");

# Problem 5: 
name = input("Please enter your full name\n");
while " " in name: name = name.replace(" ", "");
nameLength = len(name);
print(nameLength);