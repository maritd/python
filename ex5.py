# -*- coding: utf-8 -*-

name = 'Marília Torchi Daccache'
age = 25 # years
height = 1.63 / 0.3048 # dividing to get the value in feet
weight = 46 * 2.20 # dividing to get the value in pounds
eyes = 'brown'
teeth = 'white'
hair = 'brown'


print "Let's talk about %s." % name
print "She's %.2f feet tall." % height
print "She's %r pounds heavy." % round(weight)
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %.2f, and %r I get %.2f." % (age, height, round(weight), age + height + round(weight))
