# CircuitPython-28BYJ-48-ULN2003
"Bitbanging a stepper since 9/25/2021!"
Hope that this code is simple enough, and clear enough that anyone can grok it..

This is a work in progress that currently provides demo code rotating a 28BYJ-48 stepper a number of steps in either direction.
Code currently has an example that turns the stepper 1 rotation in each direction, at different speeds.

TopDO:
function to rotate a number of degrees in each direction.
set rotation direction (is +/- clockwise?)
Objectify it, so that it can be an includable library with methods to define pins, etc...
basically make it as versitile as the Arduino library, and see if Adafruit will polish it and include it, because these steppers are usefull..

