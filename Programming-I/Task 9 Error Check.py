#we want to put the ray into a line
#and then compare that line to the segment
from math import tan,pi
from matplotlib import pyplot as plt

def draw_window(win,col):
    x1=win[0][0]
    x2=win[0][1]
    y1=win[1][0]
    y2=win[1][1]
    draw_segment([[x1,y1],[x2,y1]],col)
    draw_segment([[x1,y2],[x2,y2]],col)
    draw_segment([[x1,y1],[x1,y2]],col)
    draw_segment([[x2,y1],[x2,y2]],col)

def draw_directed_segment(dirseg, col):
    pt1 = dirseg [0]
    pt2 = dirseg [1]
    dx = pt2 [0] - pt1 [0]
    dy = pt2 [1] - pt1 [1]
    # This next line is needed to make sure that the axes of the plot
    # include the full range of the directed segment
    plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], '-', color=col)
    plt.quiver(
        pt1[0], pt1[1], dx, dy,
        scale_units='xy', angles='xy', scale=1,
        width=.004,
        color=col
    )

def draw_segment(seg, col):
    pt1 = seg [0]
    pt2 = seg [1]
    # This next line is needed to make sure that the axes of the plot
    # include the full range of the segment
    plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], '-', color=col)

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

def point_on_ray(point,ray):
    x=point[0]
    y=point[1]
    start_x=ray[0][0]
    start_y=ray[0][1]
    angle = ray[1] 
    rounding=10e-15
    if angle == pi or angle==-pi or angle== pi/2 or angle==-pi/2 or angle==0:
        if angle == pi or angle == -pi:
            if x<start_x and abs(y-start_y)<rounding:
                return True
            else:
                return False
        if angle == pi/2:
            if abs(x-start_x)<rounding and y>start_y:
                return True
            else:
                return False
        if angle == -pi/2:
            if abs(x-start_x)<rounding and y<start_y:
                return True
            else:
                return False
        if angle ==0:
            if x>start_x and abs(y-start_y)<rounding:
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

def ray_window_intersect(ray,win):
    i=0
    m=0
    seg_from_win = line_segments_from_window(win)
    while i<len(seg_from_win):
        inter = ray_segment_intersect(ray,seg_from_win[i])
        if inter != "None":
            m=inter
        i=i+1
    return m
    
def one_bounce(ray,seg,win):
    point=ray[0]
    angle = ray[1]
    while angle > pi:
        angle = angle -2*pi
    while angle < -pi:
        angle = angle + 2*pi
    ray=[point,angle]
    intersect = ray_segment_intersect(ray,seg)
    if intersect == "None":
        leave_win = ray_window_intersect(ray,win)
    else:
        #ir = inital ray 
        #ir = ray
        #ir_in_reverse = [[intersect],angle - pi]
        #rr = reflection ray
        rr = [intersect,-angle - pi/2]
        leave_win = ray_window_intersect(rr,win)
    return [point,intersect,leave_win]

#path means the ray path
#obstacle means the segment
#window is self-explanatory
def draw_one_bounce(path,obstacle,window):
    #here we want to draw one or 2 directed line segment
    #and a window and a segment
    #the behaviour of the path depends on if the path and
    #the obstacle collide
    point=path[0]
    intersect = path[1]
    leave_win=path[2]
    if intersect == "None":
        draw_directed_segment([point,leave_win],"Blue")
    else:
        draw_directed_segment([point,intersect],"Orange")
        draw_directed_segment([intersect,leave_win],"Red")
    draw_segment(obstacle,"Black")
    draw_window(window,"Green")
        
window = [[-1,4] ,[-1,4]]
obstacle = [[0 ,3] , [3,0]]
path = one_bounce ([[2.5,0.4],pi/3] , obstacle , window )
draw_one_bounce(path,obstacle,window)
plt.show()
    
