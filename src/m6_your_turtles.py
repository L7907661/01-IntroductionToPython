"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Zeyu Liao.
"""
########################################################################
# done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
a = rg.SimpleTurtle('turtle')
a.pen= rg.Pen('green', 3)
a.speed = 30
size = 300
for k in range(12):
    a.draw_circle(size)
    a.pen_up()
    a.forward(30)
    a.pen_down()
    size= size - 30
#another
window.tracer(50)
b = rg.SimpleTurtle('turtle')
b.pen =rg.Pen('pink', 5)
for k in range(30):
    b.pen_up()
    b.left(20)
    b.forward(20)
    b.pen_down()
    b.draw_regular_polygon(20,60)


