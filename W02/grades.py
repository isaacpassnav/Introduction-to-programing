##### Isaac PAsapera ########
#### Purpose: Determine and display letter grades, including +/- 
"""
A >= 90
B >= 80
C >= 70
D >= 60
F < 60
"""

grades =int(input("What is your grades percent?: "))

if grades >= 90:
    letter = "A"
elif grades >=80:
    letter = "B"
elif grades >= 70:
    letter = "C"
elif grades >= 60:
    letter = "D"
elif grades  <= 60:
    letter = "F"
#Stretch challenge  1
sing = ""
last_digit = grades%10

if last_digit >= 7:
    sing = "+"
elif last_digit < 3:
    sing = "-"
else :
    sing = ""
#Stretch Challenge 2
if grades >=93:
    sing = ""
#Streatch Challenge 3
if grades =="F":
    sing = ""
print (f"Your letter grade is: {letter}{sing}")
if grades >= 70:
    print("Congratulation! you passed the class!!! ")
else:
    print("Stay focussed and you'll get it next time")

