# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 18:00:16 2023

@author: Riley Golar

This program takes a 10-digit number, presented as a 10-wide array of ints,
and performs logic checks on it. 
The 1st digit represents the number of 0s, the 2nd represents the number of 1s,
etc. etc. 

An example of a correct number is 6210001000, as it has 6 0s, 2 1s, 1 2, 0 3s,
0 4s, 0 5s, 1 6, 0 7s, 0 8s, and 0 9s.

The program prints out correct values in the python console and stores them in
a text file named Number_List.txt
"""

def number_sum(number_):
    my_sum = 0
    for n in number_:
        my_sum+=n
    return my_sum

def total(n, number_):
    my_sum = 0
    ii = 0
    while ii < 10:
        if number_[ii] == n:
            my_sum += 1
        ii+=1
    return my_sum

"""
This function takes a 10-integer array and checks to see if it follows the 
rules put forth in the beginning of this file; the 0th space in the array
counts the number of 0s, the 1st counts the number of 1s, the 2nd counts the
number of 2s, the 3rd counts the number of 3s, etc. etc.
"""
def verify(number_):
    # This first check is to save time; the sum of the digits in the number
    # must be 10, as there are 10 digits and they represent the number of 
    # digits represented.
    if number_sum(number_) != 10:
        return False
    i = 0
    # This loop checks that each digit represents the number of digits decided
    # by its placement, as noted above.
    while i < 10:
        if total(i,number_) != number_[i]:
            return False
        i += 1
    return True

"""
This function takes an array of 10 integers, converts it to an integer,
increases the value by 1, and then returns the value as a 10-integer array.
"""
def next_num(number_):
    total = (number_[9] + (10 * number_[8]) + 
             (100 * number_[7]) + 
             (1000 * number_[6]) + 
             (10000 * number_[5]) + 
             (100000 * number_[4]) + 
             (1000000 * number_[3]) + 
             (10000000 * number_[2]) + 
             (100000000 * number_[1]) + 
             (1000000000 * number_[0]))
    if total <= 9999999999:
        total+=1
    i = 0
    new_number = [0,0,0,0,0,0,0,0,0,0]
    while i < 10:
        new_number[i] = int(total/(10**(9-i)))
        total -= new_number[i]*(10**(9-i))
        i+=1
    return new_number

"""
This function creates an array of 0s to act as our starting value. It then 
iterates from 0000000000 to 9999999999, checking each value against the logic
in verify() to see if it matches the requirements given. 
Any valid values are printed on the console and stored in a text file created
by the program.
"""
def main():
    with open("Number_List.txt", 'w') as nl:
        number = [0,0,0,0,0,0,0,0,0,0]
        
        while number != [9,9,9,9,9,9,9,9,9,9]:
            if verify(number):
                nl.write(str(number))
                print(number)
            number = next_num(number)
    return 0

main()