#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
   Title:            Python script for Advent of Code 2025 day 2
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
import sympy

#------------------------------------------------------------------------------
#
#                                   Classes
#
#------------------------------------------------------------------------------  

class run_day2:

    def __init__(self):

        #----------------------------------------------------------------------
        #
        #    init function that initialises the data
        #
        #    inputs: None
        #    return: None
        #
        #----------------------------------------------------------------------

        # get list of string ranges
        input_text = np.loadtxt("inputs/inputDay2.txt", dtype=str)

        # get ranges in list
        self.input_ranges = np.char.split(input_text, ',').tolist()

    def problem1(self):

        #----------------------------------------------------------------------
        #
        #    Function to solve problem 1
        #
        #    inputs: None
        #    return: counter - int
        #
        #----------------------------------------------------------------------

        # set initial count
        counter = 0

        # loop over ranges
        for range_n in self.input_ranges:

            # split by -
            range_start_end = range_n.split('-')
            
            # set ranges
            range_list = np.arange(int(range_start_end[0]), \
                                   int(range_start_end[1])+1)

            # give the length of the id
            range_list_str = range_list.astype(str)
            range_list_char_count = np.char.str_len(range_list_str)

            # get the numbers that can be divided by two
            even_list = [x%2 for x in range_list_char_count]
            rlist, clist = [], []
            for r,c,e in zip(range_list_str, range_list_char_count, even_list):
                if e == 0:
                    rlist.append(r)
                    clist.append(c)

            # get divisions
            for i, r in enumerate(rlist):

                # split string
                r_start = r[:int(clist[i]/2)]
                r_end = r[int(clist[i]/2):]

                # check number
                if r_start == r_end:
                    counter += int(r)

        return counter
    
    # split string function
    def split_string(self,x,n):

        #----------------------------------------------------------------------
        #
        #    Function to split strings for problem 2
        #
        #    inputs: x - str
        #            n - int - length of split string
        #    return: counter - int
        #
        #----------------------------------------------------------------------

        return [x[i:i+n] for i in range(0, len(x), n)]
    
    def problem2(self):

        #----------------------------------------------------------------------
        #
        #    Function to solve problem 2
        #
        #    inputs: None
        #    return: counter - int
        #
        #----------------------------------------------------------------------

        # set initial count
        counter = 0

        # loop over ranges
        for range_n in self.input_ranges:

            # split by -
            range_start_end = range_n.split('-')
            
            # set ranges
            range_list = np.arange(int(range_start_end[0]), int(range_start_end[1])+1)

            # give the length of the id
            range_list_str = range_list.astype(str)
            range_list_char_count = np.char.str_len(range_list_str)

            # give a list of divisors
            divisor_list = [[n for n in sympy.divisors(x) if  n != x] for x in range_list_char_count]

            # filter all numbers that have len 0
            index_count_list = [len(x) for x in divisor_list]
            rlist, dlist, ilist = [], [], []
            for r,d,i in zip(range_list_str, divisor_list, index_count_list):
                if i > 0:
                    ilist.append(i)
                    rlist.append(r)
                    dlist.append(d)

            # loop over numbers
            for i, r in enumerate(rlist):
                for d in dlist[i]:
                    splitted_string = self.split_string(r,d)
                    count_dist = len(set(splitted_string))
                    if count_dist == 1:
                        counter += int(r)
                        break

        return counter
    
#------------------------------------------------------------------------------
#
#                                 Run Program
#
#------------------------------------------------------------------------------

if __name__ == '__main__':

    print("This is not the script you are looking for")