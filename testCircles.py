## @file Statistics.py
#  @author Melissa Gonzales
#  @date 13/01/2017

## importing needed modules to run test cases
import unittest; 
import Statistics as s;
import CircleADT as c; 

## declaration of several CircleT objects
c0 = c.CircleT(0,0,5);
c1 = c.CircleT(8,0,5);
c2 = c.CircleT(-8,0,5);
c3 = c.CircleT(0,0,4);
c4 = c.CircleT(-7,0,3);
l = [c0,c2,c3];
## @brief This class represents testing for a circle
#  @details Uses python's testing methods to ensure that correct values are returned
class testCircles(unittest.TestCase):
## @brief This function represents testing for a circle's x coordinate
#  @details Ensures that the functions return the correct value
    def testXcoord(self):
        self.assertEqual(c0.xcoord(), 0);
        self.assertEqual(c4.xcoord(), -7);
## @brief This function represents testing for a circle's y coordinate
#  @details Ensures that the functions return the correct value
    def testYcoord(self):
        self.assertEqual(c0.ycoord(), 0);
## @brief This function represents testing for a circle's radius
#  @details Ensures that the functions return the correct value
    def testRadius(self):
        self.assertEqual(c0.radius(), 5);
## @brief This function represents testing for a circle's area
#  @details Ensures that the functions return the correct value. Takes up to 2 decimal places
#  the pi constant is imported from python's math module
    def testArea(self):
        self.assertEqual(c3.area(), 50.27);
## @brief This function represents testing for a circle's circumference
#  @details Ensures that the functions return the correct value. Takes up to 2 decimal places
#  the pi constant is imported from python's math module
    def testCircumference(self):
        self.assertEqual(c3.circumference(), 25.13);
## @brief This function represents testing for a circle's intersection with another circle
#  @details Assume that if a circle is a subset of another, they intersect
#  Ensures that the functions return the correct value
    def testIntersect(self):
        self.assertEqual(c0.intersect(c3), True) #subset of another
        self.assertEqual(c2.intersect(c3), True) 
        self.assertEqual(c1.intersect(c3), True) 
        self.assertEqual(c3.intersect(c3), True) #identical circles
        self.assertEqual(c4.intersect(c3), True) 
## @brief This function represents testing if a circle is inside a given box
#  @details Assume that if the circle is ensrcibed (i.e. touches the edges) inside the box, it returns true
#  Ensures that the functions return the correct value
    def testInBox(self):
        self.assertEqual(c3.insideBox(-4,7,10,10), False) #not entire circle is in box
        self.assertEqual(c3.insideBox(-4,7,1,10), False) #not entire circle is in box
        self.assertEqual(c3.insideBox(-4,4,8,8), True) #Circle is enscribed in box
        self.assertEqual(c3.insideBox(-7,10,14,14), True) #Circle is inside box
## @brief This function represents testing for a list of circles' average radius
#  @details This class represents a circle as (x,y,r) values representing the 
#  Ensures that the functions return the correct value
    def testAvg(self):
        self.assertEqual(s.average(l), 4.67);
        self.assertEqual(s.average([c0,c1,c2]), 5.0);
## @brief This function represents testing for a list of circles' standard deviation
#  @details Returns up to 2 decimal places. Uses numpy's standard deviation function
#  Ensures that the functions return the correct value
    def testStdDev(self):
        self.assertEqual(s.stdDev(l), 0.47);
        self.assertEqual(s.stdDev([c0,c1,c2]), 0);
## @brief This function represents testing for a list of circles' rank
#  @details Ensures that the functions return a list of correct value. Assume that if they have the same 
#  radius, they are the same rank
    def testRank(self):
        self.assertEqual(s.rank(l), [1,1,2]);
        self.assertEqual(s.rank([c0,c1,c2]), [1,1,1]);

## @brief runs all the test cases at once 
if __name__ == '__main__':
    unittest.main()
