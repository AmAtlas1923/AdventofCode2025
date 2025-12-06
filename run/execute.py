#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
   Title:            Python script for Advent of Code 2025
   Author:           Stefan van der Jagt
   Opdrachtgever:    Stefan van der Jagt
   Date:             2025-05-12
   Laatste update:   2025-05-12
   Version:          1.0
-------------------------------------------------------------------------------
   Description:
   'Advent of Code is an Advent calendar of small programming puzzles for a 
   variety of skill levels that can be solved in any programming language you 
   like.' - Eric Wastl   
===============================================================================
"""

#------------------------------------------------------------------------------
#
#                                   Imports
#
#------------------------------------------------------------------------------

# time imports
import time

# import print class
from classes import prints

# solution classes
from classes import day1
from classes import day2
from classes import day3
from classes import day4
from classes import day5

#------------------------------------------------------------------------------
#
#                                  Functions
#
#------------------------------------------------------------------------------  

def main():

    #--------------------------------------------------------------------------
    #
    #    Main function for running the program
    #
    #    inputs: None
    #    return: None
    #
    #--------------------------------------------------------------------------

    # Print title
    prints.print_block("Solutions to Advent of code 2025", '=')

    # initialise classes
    day1Sol = day1.run_day1()
    day2Sol = day2.run_day2()
    day3Sol = day3.run_day3()
    day4Sol = day4.run_day4()
    day5Sol = day5.run_day5()

    # Day 1 solutions
    prints.print_block("Day 1: Secret Entrance", '-')
    print("Problem 1:")
    print(f"Following solution found: {day1Sol.problem1()}\n")
    print("Problem 2:")
    print(f"Following solution found: {day1Sol.problem2()}\n")

    # Day 2 solutions
    prints.print_block("Day 2: Gift shop", '-')
    print("Problem 1:")
    print(f"Following solution found: {day2Sol.problem1()}\n")
    print("Problem 2:")
    print(f"Following solution found: {day2Sol.problem2()}\n")

    # Day 3 solutions
    prints.print_block("Day 2: Lobby", '-')
    print("Problem 1:")
    print(f"Following solution found: {day3Sol.problem(2)}\n")
    print("Problem 2:")
    print(f"Following solution found: {day3Sol.problem(12)}\n")
    
    # Day 4 solutions
    prints.print_block("Day 4: Printing Department", '-')
    print("Problem 1:")
    print(f"Following solution found: {day4Sol.problem1()}\n")
    print("Problem 2:")
    print(f"Following solution found: {day4Sol.problem2()}\n")

    # Day 5 solutions
    prints.print_block("Day 5: Cafeteria", '-')
    print("Problem 1:")
    print(f"Following solution found: {day5Sol.problem1()}\n")
    print("Problem 2:")
    print(f"Following solution found: {day5Sol.problem2()}\n")
    
#-----------------------------------------------------------------------------
#
#                                 Run Program
#
#-----------------------------------------------------------------------------

if __name__ == '__main__':

    # start timing
    start_time = time.time()

    # Run program and find solutions
    main()

    # print final timing
    print(f"Run time: {round(time.time()-start_time,3)} seconds")
