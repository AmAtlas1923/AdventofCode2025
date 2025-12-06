#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
   Title:            Python script for Advent of Code 2025 printing blocks
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
#                                  Functions
#
#------------------------------------------------------------------------------  

def print_block(text,char):

    #--------------------------------------------------------------------------
    #
    #    init function that initialises the data
    #
    #    inputs: text - str
    #    return: None
    #
    #--------------------------------------------------------------------------

    # determine spaces
    spaces = int((60 - len(text))/2)
    
    # print vlock
    print(f"{60*char}")
    print("")
    print(f"{spaces*' '}{text}")
    print("")
    print(f"{60*char}")
    print("")
    
#------------------------------------------------------------------------------
#
#                                 Run Program
#
#------------------------------------------------------------------------------

if __name__ == '__main__':

    print("This is not the script you are looking for")