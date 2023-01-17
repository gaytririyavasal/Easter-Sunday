PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

Easter Sunday is the first Sunday after the first full moon of spring. Write a program that computes the date of Easter Sunday for a specified year.
An algorithm to figure this out originally was invented by the mathematician Carl Friedrich Gauss. It has a lot of steps, but they are simple ones.

Hint: when it says to divide or asks for the quotient, that means integer division. And when it asks for the remainder, that means use the remainder operation. So the quotient of 19 divided by 3 is (19 // 3) with a remainder of (19 % 3). If you need both, you'll do that in two steps.

1. Ask the user for the year (such as 2001). Save the year in variable y. See below for how to do this.
2. Divide y by 19 and call the remainder a. Ignore the quotient.
3. Divide y by 100 to get a quotient b and a remainder c.
4. Divide b by 4 to get a quotient d and a remainder e.
5. Divide (8 * b + 13) by 25 to get a quotient g. Ignore the remainder.
6. Divide (19 * a + b - d - g + 15) by 30 to get a remainder h. Ignore the quotient.
7. Divide c by 4 to get a quotient j and a remainder k.
8. Divide (a + 11 * h) by 319 to get a quotient m. Ignore the remainder.
9. Divide (2 * e + 2 * j - k - h + m + 32) by 7 to get a remainder r. Ignore the quotient.
10. Divide (h - m + r + 90) by 25 to get a quotient n. Ignore the remainder.
11. Divide (h - m + r + n + 19) by 32 to get a remainder p. Ignore the quotient.

Then Easter Sunday falls on day p of the month n. For example, if y is 2001:
     a = 6
     b = 20
     c = 1
     d = 5
     e = 0
     g = 6
     h = 18
     j = 0
     k = 1
     m = 0
     r = 6
     n = 4
     p = 15 

Hence in 2001, Easter Sunday was on April 15. (BTW: You might add print statements to print the intermediate results to see if you're on the right track. But remove them or comment them out before you submit.)
In your program you need to prompt the user to enter the year and then write out the date for Easter Sunday.

Ask for user input: The input function is not covered until slideset 3, but it's pretty easy. To get the value of the year into variable y, include the following statement:

y = int( input("Enter year: ") )
This will print the prompt "Enter year: " on the screen, and wait for the user to enter a number. This number will be read by the program as a string, say "2001". Then the function int() will convert that string into an integer which will be stored in the variable y. From there you're good to go.
You can assume that the year entered is a positive integer. Your program doesn't have to check that and doesn't have to work if the user enters a bad value.

Your session must look exactly like the following (assuming the user enters year 2001). Any deviations in the format of the output will result in points being deducted.

Enter year: 2001
In 2001 Easter Sunday is on month 4 and day 15
You can type "Easter 2001" (or any other year) into Google to verify that your program is giving you the correct result.
BTW: we're aware that the Julian calendar changed to the Gregorian calendar by some countries as early as 1582, but not by Britain and its colonies until 1752. I'm pretty sure that Gauss' algorithm only works for the Gregorian calendar. Don't worry about that. We won't test your code for years for any years when that would matter.
