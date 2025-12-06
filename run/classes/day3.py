#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
   Title:            Python script for Advent of Code 2025 day 3
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

class run_day3:

    def __init__(self):

        #----------------------------------------------------------------------
        #
        #    init function that initialises the data
        #
        #    inputs: None
        #    return: None
        #
        #----------------------------------------------------------------------

        # get list of numbers
        input_array = np.loadtxt("inputs/inputDay3.txt", dtype=str)

        # numpy array to list
        self.input_list = input_array.tolist()

    def problem(self,n):

        #----------------------------------------------------------------------
        #
        #    Function to solve problem 1 and 2
        #
        #    inputs: n - int - range for looping
        #    return: counter - int
        #
        #----------------------------------------------------------------------

        # set count
        counter = 0

        # loop over inputs
        for inp in self.input_list:

            # set initial values for every input
            final_number = ''
            index_char = -1

            # loop over range n
            for i in reversed(range(n)):
            
                # check for slicing errors
                if i == 0:
                    inp_slice = inp[index_char+2:]
                else:
                    inp_slice = inp[index_char+2:-i]

                # set initial values:
                temp_number = inp[index_char+1]
                temp_index = index_char+1

                # loop over characters
                for j, char in enumerate(inp_slice):

                    # Check if number is larger than largest known
                    if int(char) > int(temp_number):
                        temp_number = char
                        temp_index = index_char+2+j

                # set besrt value
                final_number = final_number + temp_number
                index_char = temp_index
            
            # adjust count
            counter += int(final_number)
    
        return counter
    
#------------------------------------------------------------------------------
#
#                                 Run Program
#
#------------------------------------------------------------------------------

if __name__ == '__main__':

    print("This is not the script you are looking for")