#!/usr/bin/env python

"""
Script takes three arguments in call:
    ./dragon.py number_iterations square_size draw_speed
"""

import sys
from turtle import *

QUARTER_TURN = 90
RIGHT = 1
LEFT = -1

"""
input: curve, array of "L" and "R" strings representing left and right turns
output: array of "L" and "R" strings representing folding the input array once more
"""
def fold(curve):
	new = [RIGHT, LEFT]
	out = []
	for i in range(len(curve)):
		out.append(new[i % 2])
		out.append(curve[i])
		if i == len(curve) - 1:
			out.append(new[(i + 1) % 2])
	return out

"""
input: num, number of folds
output: array of "L" and "R" strings representing a dragon curve with num folds
"""
def create(num):
	out = [LEFT]
	for i in range(num - 1):
		out = fold(out)
	return out

"""
Uses turtle module to draw dragon curve
input: curve, array of "L" and "R" strings representing dragon curve
		size, number of iterations/folds
output: none
"""
def draw(curve, size):
	forward(size)
	for direction in curve:
		right(direction * QUARTER_TURN)
		forward(size)

"""
Draws dragon curve
input: iter, number of iterations in curve
        size, size of squares in resulting drawing
        speed, draw speed (follows turtle.speed() documentation)
output: none
"""
def dragon(iterations, size, draw_speed):
    curve = create(iterations)
    speed(draw_speed)
    draw(curve, size)

    done()

if __name__ == "__main__":
	num_iter = int(sys.argv[1])
	square_size = int(sys.argv[2])
	draw_speed = int(sys.argv[3])

	dragon(num_iter, square_size, speed)