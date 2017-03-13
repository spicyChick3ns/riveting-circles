## @file Statistics.py
#  @author Melissa Gonzales
#  @date 13/01/2017

import CircleADT as c; 
import numpy as np;

## @brief average function that calculates the average radius
#  @param listCir takes a list of instances of CircleT
#  @return returns a number that represents the average of the radiuses given by the list
def average(listCir):
    return round(np.average(rList(listCir)), 2); 
## @brief stdDev function that calculates the standard deviation between radii
#  @param listCir takes a list of instances of CircleT
#  @return returns a number that represents the standard deviatation between the radii given in the list
def stdDev(listCir):
    return round(np.std(rList(listCir)),2); 
## @brief function that calculates the rank of a cirlce
#  @details the circle with the largest radius is considered the highest rank. Assume radii that are equal have an equal rank
#  @param listCir takes a list of instances of CircleT
#  @return returns a list of numbers that represents the rank of the circles in respective order as parameters
def rank(listCir):
    rad = [];
    d = {}; 
    r = 1;
    rad = rList(listCir);
    for num in sorted(rad, reverse = True):
        if num not in d:
            d[num] = r
            r += 1;
    return [d[i] for i in rad]
## @brief This function collects the radii and puts them in a list
#  @details calls on the radius function in CircleADT.py to get radii
#  @param listCir takes a list of instances of CircleT
#  @return returns a list of numbers that represent the radii of given circle objects 
def rList(l):
    r = [];
    r = [c.CircleT.radius(stuff) for stuff in l];
    return r;
