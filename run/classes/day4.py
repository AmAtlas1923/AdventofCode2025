#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
   Title:            Python script for Advent of Code 2025 day 4
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

class run_day4:

    def __init__(self):

        #----------------------------------------------------------------------
        #
        #    init function that initialises the data
        #
        #    inputs: None
        #    return: None
        #
        #----------------------------------------------------------------------

        # get list of matrices
        input = np.loadtxt('inputs/inputDay4.txt', dtype=str)

        # write to a matrix
        self.input = np.array([list(row) for row in input])

        # number of rows and cols
        self.rows, self.cols = self.input.shape

    def problem1(self):

        #----------------------------------------------------------------------
        #
        #    Function to solve problem 1
        #
        #    inputs: None
        #    return: counter - int
        #
        #----------------------------------------------------------------------

        # set initial count matrix
        counter = 0

        # set positions to check
        positions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,1),(1,0),(1,-1)]

        # loop over rows and cols
        for i in range(self.cols):
            for j in range(self.rows):
                
                # check if . or @
                if self.input[i,j] == '@':
                    
                    # set a temp count
                    temp_count = 0

                    # loop over all positions in the matrix
                    for posy,posx in positions:

                        # find the relative  indices
                        relx, rely = posx+i,posy+j

                        # check if the indeces exist
                        if (0 <= relx < self.cols) and (0 <= rely < self.rows):

                            # check if char is an @
                            if self.input[relx,rely] == '@':
                                temp_count += 1

                    # if there are less than 4 @ count
                    if temp_count < 4:
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

        # set initial count matrix
        counter = 0
        removed = 1

        # set positions to check
        positions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,1),(1,0),(1,-1)]

        # Loop until no rolls are removed
        while removed != 0:

            # set initial removed
            removed = 0

            # loop over rows and cols
            for i in range(self.cols):
                for j in range(self.rows):
                    
                    # check if . or @
                    if self.input[i,j] == '@':
                        
                        # set a temp count
                        temp_count = 0

                        # loop over all positions in the matrix
                        for posy,posx in positions:

                            # find the relative  indices
                            relx, rely = posx+i,posy+j

                            # check if the indeces exist
                            if (0 <= relx < self.cols) and \
                                  (0 <= rely < self.rows):

                                # check if char is an @
                                if self.input[relx,rely] == '@':
                                    temp_count += 1

                        # if there are less than 4 @ count
                        if temp_count < 4:

                            # count the removed @
                            removed += 1

                            # actually remove the @
                            self.input[i,j] = '.'

            # adjust count
            counter += removed

        return counter
    
#------------------------------------------------------------------------------
#
#                                 Run Program
#
#------------------------------------------------------------------------------

if __name__ == '__main__':

    print("This is not the script you are looking for")