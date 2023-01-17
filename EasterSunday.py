
# File: EasterSunday.py
# Student: Gaytri Riya Vasal
# UT EID: grv377
# Course Name: CS303E
# 
# Date Created: 9/7/2021
# Date Last Modified: 9/10/2021
# Description of Program: The following code computes the date of Easter Sunday for the year entered.

y = int( input("Enter year: ") )
a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32
print("In", y, "Easter Sunday is on month", n, "and day", p)
