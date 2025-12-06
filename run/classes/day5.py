#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
   Title:            Python script for Advent of Code 2025 day 5
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

import numpy as np

#------------------------------------------------------------------------------
#
#                                   Classes
#
#------------------------------------------------------------------------------  

class run_day5:

    def __init__(self):

        #----------------------------------------------------------------------
        #
        #    init function that initialises the data
        #
        #    inputs: None
        #    return: None
        #
        #----------------------------------------------------------------------

        # Get input of ranges and numbers
        input = np.genfromtxt("inputs/inputDay5.txt", dtype=str, comments=None, delimiter="\n", filling_values="")

        # mask the ranges
        mask = np.char.find(input, '-') >= 0

        # set ranges and numbers
        ranges = input[mask]
        numbers = input[~mask]

        # set range numbers and numbers to int
        self.range_numbers = [tuple(map(int, r.split('-'))) for r in ranges]
        self.range_numbers.sort()
        self.numbers = [int(n) for n in numbers]

    def problem1(self):

        #----------------------------------------------------------------------
        #
        #    Function to solve problem 1
        #
        #    inputs: None
        #    return: counter - int
        #
        #----------------------------------------------------------------------

        # set initial counter
        counter = 0

        # loop over numbers and ranges
        for number in self.numbers:
            for range_n in self.range_numbers:

                # check conditions and break
                if (number >= range_n[0]) & (number <= range_n[1]):
                    counter += 1
                    break

        return counter
    
    def problem2(self):

        #----------------------------------------------------------------------
        #
        #    Function to solve problem 2
        #
        #    inputs: None
        #    return: range_sum - int
        #
        #----------------------------------------------------------------------

        # loop over ranges to check for doubles
        range_final = []
        for start, end in self.range_numbers:

            # check if list ranges_final is empty or start value larger than last end value
            if not range_final or start > range_final[-1][1]:

                # add new range
                range_final.append([start,end])

            else:

                # check if new range extends old range
                if range_final[-1][1] < end:

                    # extend range
                    range_final[-1] = [range_final[-1][0],end]

        # count the lengths of the ranges and sum
        range_final = np.array(range_final)
        range_dif = range_final[:,1]-range_final[:,0]+1
        range_sum = np.sum(range_dif)

        return range_sum
    
#------------------------------------------------------------------------------
#
#                                 Run Program
#
#------------------------------------------------------------------------------

if __name__ == '__main__':

    print("This is not the script you are looking for")