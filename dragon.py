#!/usr/bin/env python

import sys
from turtle import *

"""
input: curve, array of "L" and "R" strings representing left and right turns
output: array of "L" and "R" strings representing folding the input array once more
"""
def fold(curve):
	new = ["L", "R"]
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
	out = ["R"]
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
	left(90)
	forward(size)
	for turn in curve:
		if turn == "L":
			left(90)
		else:
			right(90)
		forward(size)

num_iter = int(sys.argv[1])
square_size = int(sys.argv[2])
draw_speed = int(sys.argv[3])

speed(draw_speed)

dragon_curve = create(num_iter)
draw(dragon_curve, square_size)

done()