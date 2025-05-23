from matplotlib import pyplot as plt
from math import pi,tan,sin

def line_from_segment(seg):
    x1=seg[0][0]
    y1=seg[0][1]
    x2=seg[1][0]
    y2=seg[1][1]
    if y2==y1:
        return [0,1,-y1]
    if x2==x1:
        return [1,0,-x1]
    else:
        m=(y2-y1)/(x2-x1)
        b=y1-m*x1
        lst=[m,-1,b]
        return lst

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

def draw_segment(seg, col):
    pt1 = seg [0]
    pt2 = seg [1]
    plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], '-', color=col)

def line_from_ray(ray):
    point=ray[0]
    angle=ray[1]
    x=point[0]
    y=point[1]
    if angle == pi/2 or angle == 3*pi/2:
        return [1,0,-x]
    else:
        m=tan(angle)
        c = y-m*x
        return [m,-1,c]

def point_on_line(point,line):
    x=point[0]
    y=point[1]
    a=line[0]
    b=line[1]
    c=line[2]
    if a*x+b*y+c==0:
        return True
    else:
        return False
    
def point_on_ray(point,ray):
    line = line_from_ray(ray)
    x=point[0]
    y=point[1]
    pt=ray[0]
    angle=ray[1]
    if point_on_line(point,line):
        if angle==pi and pt[0]<x:
            return True
        if angle == pi/2 and pt[1]>y:
            return True
        if angle == 3*pi/2 and pt[1]<y:
            return True
        else:
            if angle>=0 and angle < pi/2 and x>pt[0] and y>pt[1]:
                return True
            if angle>pi/2 and angle < pi and x<pt[0] and y>pt[1]:
                return True
            if angle>pi and angle < -pi/2 and x<pt[0] and y<pt[1]:
                return True
            if angle>-pi/2 and angle <0 and x>pt[0] and y<pt[1]:
                return True
            else:
                return False 
    else:
        return False

def ray_intersect_segment(ray,seg):
    new_line1=line_from_ray(ray)
    new_line2=line_from_segment(seg)
    intersect = lines_intersect(new_line1,new_line2)
    if intersect=="None":
        return "None"
    if point_on_segment(intersect,seg) and point_on_ray(intersect,ray):
        return intersect 
    else:
        return "None"

def point_on_segment(point,seg):
    a=point[0]
    b=point[1]
    c=seg[0][0]
    d=seg[0][1]
    e=seg[1][0]
    f=seg[1][1]
    if a <= max(c,e) and a >= min(c,e) and b<=max(d,f) and b>=min(d,f):
        return True
    else:
        return False

def line_segments_from_window(window):
    x1=window[0][0]
    x2=window[0][1]
    y1=window[1][0]
    y2=window[1][1]
    start_x = min(x1,x2)
    end_x = max(x1,x2)
    start_y = min(y1,y2)
    end_y = max(y1,y2)
    first = [[start_x,start_y],[start_x,end_y]]
    second = [[start_x,end_y],[end_x,end_y]]
    third = [[end_x,end_y],[end_x,start_y]]
    fourth = [[end_x,start_y],[start_x,start_y]]
    return [first,second,third,fourth]

def draw_ray_in_window(ray,window,col):
    #window as multiple segments = was
    was = line_segments_from_window(window)
    i=0
    lst=[]
    while i<len(was):
        test = ray_intersect_segment(ray,was[i])
        if test != "None":
            lst.append(test)
        i=i+1
    if len(lst)==1:
        x1=ray[0]
        x2=lst[0]
        draw_segment([x1,x2],col)
    if len(lst)==2:
        x1=lst[0]
        x2=lst[1]
        draw_segment([x1,x2],col)
    else:
        plt.plot()
        
def draw_segment(seg, col):
    pt1 = seg [0]
    pt2 = seg [1]
    plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], '-', color=col)

def line_segments_from_window(window):
    x1=window[0][0]
    x2=window[0][1]
    y1=window[1][0]
    y2=window[1][1]
    start_x = min(x1,x2)
    end_x = max(x1,x2)
    start_y = min(y1,y2)
    end_y = max(y1,y2)
    first = [[start_x,start_y],[start_x,end_y]]
    second = [[start_x,end_y],[end_x,end_y]]
    third = [[end_x,end_y],[end_x,start_y]]
    fourth = [[end_x,start_y],[start_x,start_y]]
    return [first,second,third,fourth]

def line_from_segment(seg):
    x1=seg[0][0]
    y1=seg[0][1]
    x2=seg[1][0]
    y2=seg[1][1]
    if y2==y1:
        return [0,1,-y1]
    if x2==x1:
        return [1,0,-x1]
    else:
        m=(y2-y1)/(x2-x1)
        b=y1-m*x1
        lst=[m,-1,b]
        return lst

def point_on_segment(point,seg):
    a=point[0]
    b=point[1]
    c=seg[0][0]
    d=seg[0][1]
    e=seg[1][0]
    f=seg[1][1]
    if a <= max(c,e) and a >= min(c,e) and b<=max(d,f) and b>=min(d,f):
        return True
    else:
        return False

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

def line_intersect_segment(line,seg):
    new_line=line_from_segment(seg)
    intersect = lines_intersect(line,new_line)
    if intersect=="None":
        return "None"
    if point_on_segment(intersect,seg):
        return intersect 
    else:
        return "None"
    
def draw_line_in_window(line,window,col):
    #window as multiple segments = was
    was = line_segments_from_window(window)
    i=0
    lst=[]
    while i<len(was):
        test = line_intersect_segment(line,was[i])
        if test != "None":
            lst.append(test)
        i=i+1
    if len(lst)==2:
        draw_segment([lst[0],lst[1]],col)
    else:
        plt.plot() 

win = [[-1,1], [0, 1]]
line1 = [ 1, 1, -1.5]
line2 = [ 0.1, 1, -0.7 ]
ray = [[-0.5, 0.3], pi/4]
ray2 = [[-1.8, 2.1], -pi/4]
draw_line_in_window(line1, win, 'red')
draw_line_in_window(line2, win, 'grey')
draw_ray_in_window(ray, win, 'blue')
draw_ray_in_window(ray2, win, 'pink')
plt.show()
