# -------------------------------------------
# Exercise 2: Input and Arithmetic
# -------------------------------------------
# This exercise explores how to get information from a user and 
# how to perform maths with that data.
#
# Key Concepts to practise:
# - Using input() to capture user data
# - Converting strings to integers using int()
# - Using arithmetic operators (+, -, *, /)
# - Using f-strings to display calculations
# -------------------------------------------
# COLLABORATION & PROBLEM SOLVING
# -------------------------------------------
# You are encouraged to work with your classmates! If you run into 
# an error, try to solve it yourself first, then ask a peer for 
# a second pair of eyes. This helps you build your "problem-solving 
# muscles". Use your teacher as a final resort—let's try to 
# troubleshoot together!
# -------------------------------------------


# -------------------------------------------
# Task 1: Capturing User Data
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Capturing User Data\n"
    + "-------------------------------------------")

# EXPLANATION: The input() function tells the program to stop and 
# wait for the user to type something. Whatever they type is 
# saved as a "String" (text). 
#
# EXAMPLE:
# city = input("Where do you live? ")
# print(f"I hear {city} is a lovely place!")

# TODO:
# 1. Ask the user for their name and store it in a variable.
# 2. Ask the user for their age and store it in a variable called 'age_text'.
# 3. Print: "Hello [name]! You said you are [age_text] years old."

# Write your code below:


# -------------------------------------------
# Task 2: Data Types and Conversion
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 2: Data Types and Conversion\n"
    + "-------------------------------------------")

# EXPLANATION: Python sees "25" from an input() as text, not a number. 
# You cannot do maths with text! We use int() to convert it to an 
# "Integer" (a whole number).
#
# EXAMPLE:
# string_num = "10"
# real_num = int(string_num)
# print(real_num + 5)  # Result is 15

# TODO:
# 1. Convert your 'age_text' variable into an integer using int().
# 2. Store that result in a new variable called 'age'.
# 3. Use an f-string to calculate and print their age next year.
#    Hint: Use {age + 1} inside your f-string.

# Write your code below:


# -------------------------------------------
# Task 3: Customising the Experience
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 3: Customising the Experience\n"
    + "-------------------------------------------")

# EXPLANATION: You can use as many variables as you like in one f-string. 
# You can also use "Methods" like .capitalize() to make sure the 
# first letter is always a capital, even if the user types in lowercase.
#
# EXAMPLE:
# animal = "dog"
# print(f"Your favourite animal is a {animal.capitalize()}.")

# TODO:
# 1. Ask the user for their favourite food and favourite song.
# 2. Print a friendly message that uses the user's name, food, and song.
# 3. Use .capitalize() on the food and song variables.

# Write your code below:


# -------------------------------------------
# CHECKPOINT: GIT COMMIT
# -------------------------------------------
# Professional developers use "Source Control" to save versions of 
# their work. GitHub, GitLab, and Bitbucket are all "Remote 
# Repositories" (cloud storage for code).
#
# - git add: "Stages" the file (gets it ready).
# - git commit: Saves a "Snapshot" with a descriptive message.
# - git push: Sends the snapshot to the cloud (origin main).
#
# RUN IN TERMINAL:
# 1. git add Ex2_input.py
# 2. git commit -m "Completed tasks 1 to 3"
# 3. git push origin main
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: Age in Months
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 1: Age in Months\n"
    + "-------------------------------------------")

# TODO: Ask the user for their age again. Convert it to an int().
# Multiply it by 12 to find out how many months old they are.
# Print: "You are at least [X] months old!"

# Write your code below:


# Extension 2: Name Lengths
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 2: Name Lengths\n"
    + "-------------------------------------------")

# TODO: Ask the user for the name of their favourite city.
# Use the len() function to count the letters.
# Print: "[City] has [X] letters in its name."

# Write your code below:


# Extension 3: The Area Calculator
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 3: The Area Calculator\n"
    + "-------------------------------------------")

# TODO: Ask the user for the width and height of a rectangle.
# Convert both to integers, multiply them together (width * height),
# and print the total area.

# Write your code below:


# -------------------------------------------
# SAVE YOUR EXTENSIONS
# -------------------------------------------
# 1. git add Ex2_input.py
# 2. git commit -m "Added extension maths tasks"
# 3. git push origin main
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY: The Bill Splitter
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "ADVANCED ACTIVITY: The Bill Splitter\n"
    + "-------------------------------------------")

# TODO:
# Create a program that helps friends split a dinner bill.
# 1. Ask for the total cost of the bill (e.g. 60).
# 2. Ask how many people are sharing.
# 3. Ask what percentage tip they want to leave (e.g. 10).
# 4. Calculate the total (Bill + Tip) and tell each person
#    exactly how much they owe.
#
# Hint: To calculate a 10% tip, you can do: bill * 0.10

# Write your code below:


# -------------------------------------------
# FINAL SUBMISSION
# -------------------------------------------
# Your code is now synchronised with your online platform.
# Whether you use GitHub, GitLab or Bitbucket, your work is safe!
#
# 1. git add Ex2_input.py
# 2. git commit -m "Final submission - All tasks complete"
# 3. git push origin main
# -------------------------------------------
