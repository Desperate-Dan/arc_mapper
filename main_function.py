from matplotlib import pyplot as plt
import math
from matplotlib.patches import Arc

def circle_mapper(pointA, pointB, offset, XorY, mid=False, flip=False, invert=False):
    # slope of line
    def slope(x1, y1, x2, y2):
        m = (y2 - y1)/(x2 - x1)
        return m

    # midpoint of line
    def midpoint(x1, y1, x2, y2):
        xm = (x1 + x2)/2
        ym = (y1 + y2)/2
        mp = [xm,ym]
        return mp
    
    # y intercept of line (c)
    def intercepty(x1, y1, x2, y2):
        c = ((x2*y1)-(x1*y2))/(x2-x1)
        return c

    # Equation of perpendicular line
    def perp_eq(x1, y1, perp_m):
        perp_c = y1 - (perp_m*x1)
        return perp_c

    # This is a method of choosing the new point on the perpendicular line to draw the arc from.
    # It is currently scaled by n, but there is probably a more user friendly way of doing this...
    def new_point_finder(perp_m,perp_c,mp,n,XorY):
        if XorY.lower() == "x":
            x = mp[0] * n
            y = (perp_m*x) + perp_c
            new_point = [x,y]
        elif XorY.lower() == "y":
            y = mp[1] * n
            x = ((perp_c - y)/perp_m)*-1
            new_point = [x,y]
        return new_point

    # Reflect a point across a line
    # Modified from https://stackoverflow.com/a/3307181
    def reflector(x3, y3, c, m):
        d = (x3 + (y3 - c)*m)/(1 + (m*m))
        x4 = (2*d) - x3
        y4 = (2*d*m) - y3 + (2*c)
        reflected = [x4,y4]
        return reflected

    # Get the acute angle between lines
    # modified from (can't find the original link...)
    def tanAngle(slope1, slope2):    
        # Store the tan value  of the angle
        angle = abs((slope2 - slope1) / (1 + slope1 * slope2))
        # Calculate tan inverse of the angle
        rad = math.atan(angle)
        # Convert the angle from rad to deg
        deg = (rad * 180) / math.pi
        
        return (round(deg, 4))
        
    # Need three points to get the two slopes to get angle ABC
    def angler(pointA,pointB,pointC):
        # All the angles need to be calculated from the x axis (ie. horizontal)...
        # ...and changed depening on the relative positions of the points in question

        slope1 = slope(pointA[0], pointA[1], pointB[0], pointB[1])
        thetaAB = tanAngle(slope1,0)
        if (pointA[0] > pointB[0]) & (pointA[1] > pointB[1]):
            theta1 = thetaAB
        elif (pointA[0] < pointB[0]) & (pointA[1] > pointB[1]):
            theta1 = 180 - thetaAB
        elif (pointA[0] > pointB[0]) & (pointA[1] < pointB[1]):
            theta1 = 360 - thetaAB
        else:
            theta1 = 180 + thetaAB

        slope2 = slope(pointB[0], pointB[1], pointC[0], pointC[1])
        thetaBC = tanAngle(slope2,0)
        if (pointB[0] > pointC[0]) & (pointB[1] > pointC[1]):
            theta2 = 180 + thetaBC
        elif (pointB[0] < pointC[0]) & (pointB[1] > pointC[1]):
            theta2 = 360 - thetaBC
        elif (pointB[0] > pointC[0]) & (pointB[1] < pointC[1]):
            theta2 = 180 - thetaBC
        else:
            theta2 = thetaBC
        
        return theta1, theta2  
        


    # Get slope of line A between two given points
    m = slope(pointA[0], pointA[1], pointB[0], pointB[1])
    # Get slope of line perpendicular to line A
    perp_m = -(1/m)
    # Get the midpoint of line A
    mp = midpoint(pointA[0], pointA[1], pointB[0], pointB[1])
    # Get the y axis intercept of line A
    c = intercepty(pointA[0], pointA[1], pointB[0], pointB[1])
    # Get the y axis intercept of perpendicular line A 
    perp_c = perp_eq(mp[0],mp[1],perp_m)
    # If we just want a full circle...
    if mid:
        new_point = mp
        reflected = mp
    else: 
        # Get point an aribtrary distance along perpendicular line A, X or Y units away (offset) 
        new_point = new_point_finder(perp_m, perp_c, mp, offset, XorY)
        # Reflect that point across the line
        reflected = reflector(new_point[0],new_point[1],c,m)
    # Get diameter of circle (distance between new point and pointA)
    radius = math.dist(new_point,pointB)
    diameter = radius * 2
    # Get angles for drawing arc
    # To make reciprocal arcs, added a simple binary check to reflect the point if (yB) > (yA)
    if not flip:    
        if pointA[1] > pointB[1]:
            theta1, theta2 = angler(pointA, new_point, pointB)
            output_point = new_point
        else:
            theta2, theta1 = angler(pointA, reflected, pointB)
            output_point = reflected
    else:
        if pointA[1] < pointB[1]:
            theta1, theta2 = angler(pointA, new_point, pointB)
            output_point = new_point
        else:
            theta2, theta1 = angler(pointA, reflected, pointB)
            output_point = reflected

    # Swapping thetas depending on the relative postions of points A and B
    if XorY == "y":
        if (pointA[0] < pointB[0]) & (pointA[1] < pointB[1]):
            theta2, theta1 = theta1, theta2
        elif (pointA[0] < pointB[0]) & (pointA[1] > pointB[1]):
            theta2, theta1 = theta1, theta2
    if XorY == "x":
        if (pointA[0] > pointB[0]) & (pointA[1] > pointB[1]):
            theta2, theta1 = theta1, theta2
        elif (pointA[0] < pointB[0]) & (pointA[1] > pointB[1]):
            theta2, theta1 = theta1, theta2
    
    # Add the ability to flip the arcs if you fancy
    if invert:
        theta2, theta1 = theta1, theta2

    return output_point, diameter, theta1, theta2
