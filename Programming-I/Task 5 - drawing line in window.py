from matplotlib import pyplot as plt

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
    if a > max(c,e) or a < min(c,e):
        return False
    if b > max(d,f) or b < min(d,f):
        return False
    else:
        return True

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







