#we want to put the ray into a line
#and then compare that line to the segment
from math import tan,pi

def line_from_segment(seg):
    x1=seg[0][0]
    y1=seg[0][1]
    x2=seg[1][0]
    y2=seg[1][1]
    if x2==x1:
        return [1,0,-x1]
    else:
        m=(y2-y1)/(x2-x1)
        b=y1-m*x1
        lst=[m,-1,b]
        return lst

def line_from_ray(ray):
    point=ray[0]
    angle=ray[1]
    x=point[0]
    y=point[1]
    if angle == pi/2 or angle == -pi/2:
        return [1,0,-x]
    else:
        m=tan(angle)
        c = y-m*x
        return [m,-1,c]

def lines_intersect(line1,line2):
    line1_x=line1[0]
    line1_y=line1[1]
    line1_c=line1[2]
    line2_x=line2[0]
    line2_y=line2[1]
    line2_c=line2[2]
    denom=line1_x*line2_y-line1_y*line2_x
    lst=[]
    if denom==0:
        return "None"
    else:
        num_x=line1_y*line2_c-line1_c*line2_y
        num_y=line1_c*line2_x-line1_x*line2_c
        x=num_x/denom
        y=num_y/denom
        lst.append(x)
        lst.append(y)
        return lst

def point_on_segment(point,seg):
    a=point[0]
    b=point[1]
    c=seg[0][0]
    d=seg[0][1]
    e=seg[1][0]
    f=seg[1][1]
    if a > max(c,e) or a < min(c,e):
        return False
    if b > max(d,f) or b < min(d,f):
        return False
    else:
        return True

#assuming point lies on the line from the ray
def point_on_ray(point,ray):
    x=point[0]
    y=point[1]
    start_x=ray[0][0]
    start_y=ray[0][1]
    angle = ray[1] 
    while angle > pi:
        angle = angle - 2*pi
    while angle < -pi:
        angle = angle + 2*pi
    ray=[ray[0],angle]
    if angle == pi or angle==-pi or angle== pi/2 or angle==-pi/2 or angle==0:
        if angle == pi or -pi:
            if x<start_x and y==start_y:
                return True
            else:
                return False
        if angle == pi/2:
            if x==start_x and y>start_y:
                return True
            else:
                return False
        if angle == -pi/2:
            if x==start_x and y<start_y:
                return True
            else:
                return False
        if angle ==0:
            if x>start_x and y==start_y:
                return True
            else:
                return False
    else:
        if angle>0 and angle<pi/2:
            if x>start_x and y>start_y:
                return True
            else:
                return False
        if angle >pi/2 and angle < pi:
            if x<start_x and y>start_y:
                return True
            else:
                return False
        if angle <0 and angle>-pi/2:
            if x>start_x and y<start_y:
                return True
            else:
                return False
        if angle <-pi/2 and angle >-pi:
            if x<start_x and y<start_y:
                return True
            else:
                return False
    
            
def ray_segment_intersect(ray,seg):
    line1 = line_from_ray(ray)
    line2 = line_from_segment(seg)
    m=lines_intersect(line1,line2)
    if m=="None":
        return "None"
    else:
        if point_on_segment(m,seg) and point_on_ray(m,ray):
            return m
        else:
            return "None"



     


    
    