"""
This module lets you experience the POWER of FUNCTIONS and PARAMETERS.
Authors: David Mutchler, Vibha Alangar, Mark Hays, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    drawing_speed = 10  # Bigger numbers mean faster drawing
    window = rg.TurtleWindow()
    window.tracer(drawing_speed)

    ###########################################################################
    # When the _TODO_s ask you to test YOUR code,
    # comment-out the following two statements and add code as needed.
    ###########################################################################
    draw_circles(rg.Point(100, 50))
    draw_circles(rg.Point(-200, 0))

    better_draw_circles(rg.Point(100, 50), 5, 40)
    better_draw_circles(rg.Point(-200, 0), 20, 6)

    window.update()
    window.close_on_mouse_click()


def draw_circles(point):
    """
    Constructs a SimpleTurtle, then uses the SimpleTurtle to draw 10 circles
    such that:
      -- Each is centered at the given Point, and
      -- They have radii:  15  30  45  60  75  ..., respectively.
    """
    turtle = rg.SimpleTurtle()

    # --------------------------------------------------------------------------
    # Draw circles centered at the given Point, by telling the SimpleTurtle to:
    #  Step 1: Go to the given Point and point east (towards the right).
    #  Step 2: Go 15 pixels DOWN, with its Pen up.
    #          Then draw a radius R circle.
    #    Note: The circle will be centered at the given Point,
    #    because of the way that the SimpleTurtle  draw_circle  method works.
    #  Step 3: Repeat Step 2, but using 30 pixels instead of 15 (in both places)
    #  Step 4: Repeat Step 2, but using 45 pixels instead of 15
    #  Step 5: Repeat Step 2, but using 60 pixels instead of 15
    #    etc.
    # --------------------------------------------------------------------------

    turtle.pen_up()
    turtle.go_to(point)
    turtle.set_heading(0)  # Point "east" (towards the right)

    for k in range(1, 11):  # k becomes 1, 2, 3, ... 10

        turtle.pen_up()

        # Go DOWN 15 pixels, ending up pointing east again
        turtle.right(90)
        turtle.forward(15)
        turtle.left(90)

        turtle.pen_down()
        turtle.draw_circle(15 * k)  # Radius 15, 30, 45, 60, ...


def better_draw_circles(point, n, radius):
    """ An improved version of draw_circles, per the _TODO_ below. """
    turtle = rg.SimpleTurtle()
    turtle.pen_up()
    turtle.go_to(point)
    turtle.set_heading(0)  # Point "east" (towards the right)

    for k in range(1, n + 1):  # k becomes 1, 2, 3, ... n
        turtle.pen_up()

        # Go DOWN radius pixels, ending up pointing east again
        turtle.right(90)
        turtle.forward(radius)
        turtle.left(90)

        turtle.pen_down()
        turtle.draw_circle(k * radius)


# ----------------------------------------------------------------------
# TODO: 2.
#   First, RUN this program.  You will see that draw_circles draws
#   concentric circles whose radii vary by 15.
#
#   A function that did the same thing as draw_circles, but allowed
#   for the radii to vary by ANY desired amount would be MORE POWERFUL.
#
#   So, implement TWO functions immediately below this comment.
#   They should be called:
#      run_test_better_draw_circles
#      better_draw_circles
#
#   Your   better_draw_circles  function should have a single PARAMETER
#   that is the amount by which the radii of the circles increase.
#   For example, if that parameter is given the value 10,
#   then the circles have radii:  0  10  20  30  40 ... 200, respectively,
#   just as in   draw_circles1.  But if that parameter is given the
#   value 3, the circles have radii:  0  3  6  9  12  ... 60.
#
#   Your  run_test_better_draw_circles function should TEST your new
#   better_draw_circles function, by calling it with different values
#   for its argument.  Don't forget to put a call to
#   run_test_better_draw_circles  in  main.
#
#   You may find that COPY-AND-PASTE of the  draw_circles  and its
#   run_test_draw_circles  may get you started more quickly on your new
#   better_draw_circles  and  run_test_better_draw_circles.
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# TODO: 3.
#   In the previous exercise, you made a MORE POWERFUL version
#   of draw_circles by introducing a PARAMETER for the amount by
#   which the radii of the concentric circles increase.
#
#   In this exercise, implement TWO MORE functions immediately below
#   this comment. They should be called:
#      run_test_even_better_draw_circles
#      even_better_draw_circles
#
#   Your new   even_better_draw_circles  function should have
#   SEVERAL parameters, for allowing the caller to vary what YOU
#   choose to have the caller vary.  For example, you could have
#   parameters for any or all of the following:
#     -- The amount by which the radii vary (as you did above)
#     -- The number of concentric circles drawn
#     -- The center of the concentric circles
#     -- The outline_color of the concentric circles
#     -- The speed at which the animation runs
#    and more.
#
#   A total of any THREE parameters (of your choosing) is enough,
#   although you may have more.
#
#   In testing your even_better_draw_circles function,
#   can you make some fun pictures?
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()