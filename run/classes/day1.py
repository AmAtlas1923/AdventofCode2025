#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
   Title:            Python script for Advent of Code 2025 day 1
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
import math

#------------------------------------------------------------------------------
#
#                                   Classes
#
#------------------------------------------------------------------------------  

class run_day1:

    def __init__(self):

        #----------------------------------------------------------------------
        #
        #    init function that initialises the data
        #
        #    inputs: None
        #    return: None
        #
        #----------------------------------------------------------------------

        # get list of rotations
        array_rotations = np.loadtxt("inputs/inputDay1.txt", dtype=str)

        # numpy array to list
        list_rotations = array_rotations.tolist()

        # split list numbers
        self.list_numbers = [int(x.replace("L","-").replace("R",""))\
                              for x in list_rotations]

    def problem1(self):

        #----------------------------------------------------------------------
        #
        #    Function to solve problem 1
        #
        #    inputs: None
        #    return: counter - int
        #
        #----------------------------------------------------------------------

        # start number
        current_number = 50

        # zero counter
        counter = 0

        for number in self.list_numbers:

            # Add rotation
            current_number = (current_number+number)%100

            # add to counter when 0
            if current_number == 0:
                counter += 1
        
        return counter
    
    def problem2(self):

        #----------------------------------------------------------------------
        #
        #    Function to solve problem 2
        #
        #    inputs: None
        #    return: counter - int
        #
        #----------------------------------------------------------------------

        # start number
        current_number = 50

        # zero counter
        counter = 0

        for number in self.list_numbers:

            # get the sign
            sign = math.copysign(1,number)

            # rotation number
            N_rot, __ = divmod(abs(number),100)
            counter += N_rot

            # correct for rotations
            number -= sign*N_rot*100

            # check if passes 0
            if ((current_number+number >= 100) | \
                (current_number+number <= 0)) & (current_number != 0):
                counter += 1

            # Add rotation
            current_number = (current_number+number)%100
            
        return counter

    
#------------------------------------------------------------------------------
#
#                                 Run Program
#
#------------------------------------------------------------------------------

if __name__ == '__main__':

    print("This is not the script you are looking for")