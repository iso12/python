import bpy 
from bpy.props import (FloatProperty, IntProperty, BoolProperty)
from bpy.types import Operator
from math import (sin, cos, pi)

def angle_point(center, angle, distance):
    cx, cy = center
    x = cos(angle) * distance
    y = sin(angle) * distance
    return x + cx, y + cy

def angle_point (center, angle, distance):
    cx, cy = center
    x = cos(angle) * distance
    y = sin(angle) * distance
    return x + cx, y + cy

def flat_hump(string, mx = 1, mz)