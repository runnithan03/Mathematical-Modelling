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
    c=seg[0][0]
    e=seg[1][0]
    if a > max(c,e) or a < min(c,e):
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

def segments_intersect(seg1,seg2):
    k=line_from_segment(seg1)
    l=line_from_segment(seg2)
    m=lines_intersect(k,l)
    if m=="None":
        return "None"
    else:
        if point_on_segment(m,seg1) and point_on_segment(m,seg2):
            return m
        else:
            return "None"




