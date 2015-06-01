from TurtleWorld import *

def follow(t, S, step=10, angle=90):
    """
    Cause the turtle, t, to interpret the symbols in the string S.

    E, F -- draw forward by step
    L    -- turn left by angle
    R    -- turn right by angle

    All other symbols are ignored.
    """
    for s in S:
        if s == 'E' or s == 'F':
            fd(t, step)
        elif s == 'L':
            lt(t, angle)
        elif s == 'R':
            rt(t, angle)

if __name__ == "__main__":
    S = "FLFFLFFLFFRFFRFFRF"              # Big S shape
            
    world = TurtleWorld()
    world.delay = 0
    bob = Turtle()

    follow(bob, S, 100, angle=80)
    wait_for_user()
