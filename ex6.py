# determine the variable x with a frase and a string
x = "There are %d types of people." % 10
# assign the name to a variable
binary = "binary"
do_not = "don't"
# determine the variable y with a frase and a string
y = "Those who know %s and those who %s." % (binary, do_not)

# printing x and y
print x
print y

# printing x and y again inside a different string
print "I said: %r." % x
print "I also said: '%s'." % y

# assign the values to the variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# printing the result of the equation
print joke_evaluation % hilarious

# assign values to the variables w and e
w = "This is the left side of..."
e = "a string with a right side."

# printing w and e in a string
print w + e

# Question 1: Explain why adding the two strings w and e with + makes a longer string.
# Answer 1: Because you add the two values forming one.

# Question 2: Find all the places where a string is put inside a string. There are four places. Are you sure there are only four places? How do you know? Maybe I like lying.
# Answer 2: The strings are in line 2, 7, 14 and 15 there is also the string in line 19.
