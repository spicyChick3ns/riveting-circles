## @file CircleADT.py
#  @title CircleT
#  @author Melissa Gonzales
#  @date 16/01/2017

import math
## @brief This class represents a circle
#  @details This class represents a circle as (x,y,r) values representing the 
#  centre of the cirlce with x and y coordinates and r representing the radius
class CircleT:
## @brief constructor that initialises value of object
#  @param x is the x coordinate of the circle
#  @param y is the y coordinate of the circle
#  @param r is the radius of the circle
    def __init__ (self, x, y, r):
        self.r = r;
        self.x = x;
        self.y = y;
## @brief accessor that returns the x coordinate 
#  @return the x coordinate of the circle object
    def xcoord(self):
        return self.x;
## @brief accessor that returns the y coordinate 
#  @return the y coordinate of the circle object
    def ycoord(self):
        return self.y;
## @brief accessor that returns the radius
#  @return the radius of the circle object
    def radius(self):
        return self.r;
## @brief function that calculates the area of given circle
#  @details the Pi constant is used from the math library. This function will only return 2 decimal places
#  @return the area of the circle object
    def area(self):
        return round(math.pi*(self.r**2), 2);
## @brief function that calculates the circumference of given circle
#  @details the Pi constant is used from the math library. This function will only return 2 decimal places
#  @return the circumference of the circle object
    def circumference(self):
        return round(2*math.pi*(self.r), 2) ;
## @brief this function determines whether the circle is inside the box or not
#  @details assume that if the circle is enscribed in the box, returns true.
#  @param xNot top left x coordinate of box
#  @param yNot top left y coordinate of box
#  @param w width of box
#  @param h height of box
#  @return true or false depending if it is in the box
    def insideBox(self, xNot, yNot, w, h):
        x1 = self.x + self.r; #right side of circle, x coordinate
        x2 = self.x - self.r; #left side of circle, x coordinate
        y1 = self.y + self.r; #top side of circle, y coordinate
        y2 = self.y - self.r; #bottom side of circle, y coordinate

        boxX = xNot + w; #outer x coordinate of box
        boxY = yNot - h; #outer y coordinate of box

        areaC = math.pi*(self.r**2);
        areaB = math.fabs(w * h);
        if (areaC < areaB): 
            if (xNot <= x2 <= boxX):
                if (xNot <= x1 <= boxX):
                    if (boxY <= y1 <= yNot ):
                        if (boxY <= y2 <= yNot):
                            return True;
                        else:
                            return False;
                    else:
                        return False;
                else:
                    return False;
            else:
                return False;
        else:
            return False;
            
## @brief This function checks if two circles intersect
#  @details assume that if a circle is a subset of another (i.e. overlaps) they intersect
#  @return true or false depending if the circles interesect
    def intersect(self,c):
        if (math.sqrt(((c.x - self.x)**2)+ (c.y - self.y)**2) <= (self.r + c.r)):
            return True;
        else: 
            return False;
## @brief This function scales the radius
#  @param k number to scale radius by            
    def scale(self,k):
        self.r = self.r * k;
## @brief This function translates the circle
#  @param dx amount to move x coordinate by  
#  @param dy amount to move y coordinate by  
    def translate(self,dx, dy):
        self.x = self.x + dx;
        self.y = self.y + dy;
